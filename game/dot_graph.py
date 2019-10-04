# Generate a graph of the game script in DOT language (for Graphviz)

import re
import os.path
import string
import itertools
import ast as py_ast
import renpy.ast as ast
import renpy.store as store
from renpy.game import script
from renpy.script import ScriptError

def generate_graph(dot_file):

    labels = [x for x in script.namemap.values() if isinstance(x, ast.Label) and not x.name.startswith("_")]

    graph = {}
    subgraphs = {}

    # Explore labels that match a predicate
    for label in labels:
        if node_predicate(label):
            explore_label(label, graph, node_predicate, script)

    targets = set(itertools.chain(*graph.values()))

    # Filter orphaned and excluded labels
    for label in labels:
        if node_predicate(label): # and (len(graph[label.name]) > 0 or label.name in targets):
            subgraph = subgraphs.setdefault(label.filename, set())
            subgraph.add(label.name)

    # Write DOT file
    with open(dot_file, 'w') as f:
        f.write('digraph renpy_script {\n')
        f.write('    overlap = false;\n')
        # Subgraph nodes
        for (subgraph, nodes) in subgraphs.iteritems():
            f.write('    subgraph "cluster_{}" {{\n'.format(subgraph))
            f.write('        label = "{}";\n'.format(subgraph))
            f.write('        {};\n'.format(string.join(nodes,';')))
            f.write('    }\n')
        # Graph edges
        for (src, tgts) in graph.iteritems():
            for tgt in tgts:
                f.write('    {} -> {}\n'.format(src, tgt))
        f.write('}\n')

def node_predicate(node):
    (dir, fname) = os.path.split(node.filename)
    if not dir.startswith("game/__Renpy__/_hermione_"):
        return False
    if any(x in fname for x in ["chibi", "random_face", "equip_labels", "_init", "layering", "chitchat"]):
        return False

    exclude = ["day_start", "night_start", "main_room", "night_main_menu", "day_main_menu"]
    if isinstance(node, ast.Label) and node.name in exclude:
        return False
    if isinstance(node, ast.Jump) and node.target in exclude:
        return False

    return True

def explore_label(node, graph, pred, script):
    if not isinstance(node, ast.Label):
        return
    graph[node.name] = set()
    nodes = node.block
    while len(nodes) > 0:
        n = nodes.pop()
        if isinstance(n, ast.If):
            for condition, block in n.entries:
                nodes.extend(block)
        elif isinstance(n, ast.While):
            nodes.extend(n.block)
        # elif isinstance(n, ast.Call):
        #     if not n.expression:
        #         graph[node.name].add(n.label)
        elif isinstance(n, ast.Menu):
            for _label, _condition, block in n.items:
                if block:
                    nodes.extend(block)
        elif isinstance(n, ast.Jump):
            if not n.expression and pred(n) and pred(script.lookup(n.target)):
                graph[node.name].add(n.target)

def graph_event_vars(dot_file="event_vars.dot"):
    # Generate graph
    events = [(n, v) for n, v in store.__dict__.iteritems() if isinstance(v, store.event_class)]
    graph = {} # start_label -> (load_vars, store_vars)
    for name, ev in events:
        labels = [ev.start_label] if ev.start_label else []
        c = itertools.chain.from_iterable(ev.events)
        c = itertools.chain.from_iterable(c)
        labels.extend(c)
        labels = [x for x in labels if x] # strip False values
        load_vars = []
        store_vars = []
        for label in labels:
            try:
                node = script.lookup(label)
                lv, sv = vars_from_label(node)
                load_vars.extend(lv)
                store_vars.extend(sv)
            except ScriptError as e:
                print "Warning: " + str(e)
        graph[name] = (set(load_vars), set(store_vars))
        print "{}: {}".format(name, ev.title)

    all_vars = set(itertools.chain.from_iterable(itertools.chain.from_iterable(graph.values())))

    # Write graph file
    with open(dot_file, 'w') as f:
        f.write('digraph event_vars {\n')
        f.write('    overlap = false;\n    rankdir = LR;\n    ranksep = 10.0;\n')
        # Events
        f.write('    subgraph cluster_events {\n')
        f.write('        {};\n'.format(string.join(['e_' + e for e in graph.keys()],';')))
        f.write('    }\n')
        # Variables
        f.write('    subgraph cluster_variables {\n')
        f.write('//        {};\n'.format(string.join(['v_' + v for v in all_vars],';')))
        f.write('    }\n')
        # Mapping
        for e, vs in graph.iteritems():
            lv, sv = vs
            for v in lv:
                f.write('    v_{} -> e_{};\n'.format(v, e))
            for v in sv:
                f.write('    e_{} -> v_{};\n'.format(e, v))
        f.write('}\n')

def vars_from_label(start_node):
    if not isinstance(start_node, ast.Label):
        return
    load_vars = []
    store_vars = []
    # Visit game script nodes reachable from start_node
    visited = set()
    visited.add(start_node.name)
    nodes = start_node.block
    while len(nodes) > 0:
        n = nodes.pop()
        if isinstance(n, ast.If):
            # If
            for condition, block in n.entries:
                if block:
                    nodes.extend(block)
                if condition:
                    load_vars.extend(extract_vars(condition, "load"))
                    store_vars.extend(extract_vars(condition, "store"))
        elif isinstance(n, ast.While):
            # While
            if n.block:
                    nodes.extend(n.block)
            if n.condition:
                load_vars.extend(extract_vars(n.condition, "load"))
                store_vars.extend(extract_vars(n.condition, "store"))
        elif isinstance(n, ast.Call):
            # Call
            if not n.expression and not is_ignored_label(n.label) and not n.label in visited:
                visited.add(n.label)
                try:
                    label = script.lookup(n.label)
                    nodes.extend(label.block)
                except ScriptError as e:
                    print "Warning: " + str(e)
        elif isinstance(n, ast.Jump):
            # Jump
            if not n.expression and not is_ignored_label(n.target) and not n.target in visited:
                visited.add(n.target)
                try:
                    label = script.lookup(n.target)
                    nodes.extend(label.block)
                except ScriptError as e:
                    print "Warning: " + str(e)
        elif isinstance(n, ast.Menu):
            # Menu
            for _label, condition, block in n.items:
                if block:
                    nodes.extend(block)
                if condition:
                    load_vars.extend(extract_vars(condition, "load"))
                    store_vars.extend(extract_vars(condition, "store"))
        elif isinstance(n, ast.Python):
            # Python
            if not n.hide:
                source = n.code.source
                load_vars.extend(extract_vars(source, "load"))
                store_vars.extend(extract_vars(source, "store"))
    load_vars = set(load_vars)
    store_vars = set(store_vars)
    return (load_vars, store_vars)

def is_ignored_label(label_name):
    return (label_name.startswith(("play_", "end_", "set_", "update_", "."))
    or label_name in ["nar", "main_room", "main_room_menu", "her_kneel", "transition", "bld", "blkfade", "teleport", "give_reward", "popup"]
    or "chibi" in label_name
    or label_name.endswith(("_main","_walk", "_favor_menu", "_start"))
    or not script.has_label(label_name))

def is_ignored_var(var_name):
    return (var_name.endswith(("_ypos", "_xpos", "_zorder", "_flip", "_name", "_animation", "_head", "cloth_pile"))
    or "chibi" in var_name
    or "_cg_" in var_name
    or var_name in ["True", "False", "None", "renpy"] # Names mistaken for variables
    or var_name.startswith(("g_c_", "s_c_", "h_c_", "menu_", "ccg")))

def extract_vars(code, mode):
    v = NameVisitor(mode)
    v.visit(py_ast.parse(code))
    return [x for x in v.vars if not is_ignored_var(x)]

class NameVisitor(py_ast.NodeVisitor):
    def __init__(self, mode="load"):
        if mode in ["load", "store"]:
            self.mode = mode
        else:
            raise Exception("Bad mode")
        self.vars = set()

    def visit_Name(self, node):
        if (self.mode == "load" and type(node.ctx) is py_ast.Load) or (self.mode == "store" and type(node.ctx) is py_ast.Store):
            self.vars.add(node.id)
