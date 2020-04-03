
import ast as py_ast
import renpy.ast as ast
import renpy.store as store
from renpy.game import script
from graphviz import Digraph
from fnmatch import fnmatchcase


def event_graphs(filename):

    def event_group(event):
        return event.events[0][0][0][:2] # First event label
        #return event.start_label[:2]

    # events = [x for x in store.__dict__.itervalues() if isinstance(x, store.event_class)]
    # events = sorted(events, key=event_group)
    events = [store.hg_pf_grope]

    g = Digraph()#strict=True)
    g.attr(concentrate="true",pack="36",packmode="array_cu", rankdir="LR") #
    g.attr("node", shape="box", style="rounded")

    for event in events:
        event_graph = get_event_subgraph(event)
        g.subgraph(event_graph)

    print("Rendering graph...")

    g.format = "png"
    g.render(filename, view=True)


def get_event_subgraph(event):
    sg = Digraph("cluster_{}".format(event.start_label))
    sg.attr(label="{} ({})".format(event.start_label, event.title))

    visitor = ScriptVisitor(sg)
    for tier in event.events:
        for start, _ in tier:
            visitor.explore(start, start=True)

    return sg

class ScriptVisitor:

    def __init__(self, graph):
        self.graph = graph
        self.stack = []
        self.visited = set()
        self.start_nodes = set()


    def explore(self, node, start=False):
        if isinstance(node, basestring):
            node = script.lookup(node)

        if start:
            self.start_nodes.add(node)

        if node not in self.visited:
            self.visited.add(node)
            self.stack.append(node)
            node.get_children(self.visit)
            self.stack.pop()


    def visit(self, node):
        start = self.stack[-1]

        if isinstance(start, list):
            blocks = start
            if len(blocks) == 0:
                self.stack.pop()
                start = self.stack[-1]
            else:
                start = blocks[-1][0] # First block node
                if node is blocks[-1][-1]:
                    blocks.pop()
                    if len(blocks) == 0:
                        self.stack.pop()

        if end_node(node):
            end = "{}_end".format(nid(node))
            self.graph.node(end, "end")
            self.graph.edge(nid(start), end)
            return

        if ignore_node(node):
            return

        if isinstance(node, ast.Label):
            if node is not start:
                # Nested label
                self.graph.edge(nid(start), nid(node), arrowhead="none", style="dashed")

            if node in self.start_nodes:
                self.graph.node(nid(node), node.name, style="filled,rounded")
            else:
                self.graph.node(nid(node), node.name)

        if isinstance(node, ast.Jump):
            target = script.lookup(node.target)
            self.graph.edge(nid(start), nid(target))
            self.explore(target)

        if isinstance(node, ast.Call) and not node.expression:
            target = script.lookup(node.label)
            self.graph.edge(nid(start), nid(target), style="bold")
            self.explore(target)

        if isinstance(node, ast.Menu):
            menu_cluster = Digraph("cluster_{}".format(nid(node)))
            menu_cluster.attr(label="")
            bs = []
            for label, condition, block in node.items:
                if block:
                    bs.append(block)
                    name = nid(block[0])
                    menu_cluster.node(name, label)
                    self.graph.edge(nid(start), name, arrowhead="none")

            self.graph.subgraph(menu_cluster)
            bs.reverse()
            self.stack.append(bs)

        if isinstance(node, ast.If):
            pass


def nid(x):
    return hex(id(x))


def end_node(node):
    label_patterns = ["end_*", "too_much"]

    if isinstance(node, ast.Jump):
        label = node.target
        return any(fnmatchcase(label, p) for p in label_patterns)

    if isinstance(node, ast.Call):
        label = node.label
        return any(fnmatchcase(label, p) for p in label_patterns)

    return False


def ignore_node(node):
    label_patterns = [
        "_end_*", "main_room*", "play_*", "update_*", "blk*", "hide*",
        "nar", "bld", "ctc", "reset_*", "chibi_*", "set_*",
        "*_main", "*_walk", "*_chibi", "*_block", "*_chibi_scene",
        "room", "day_start", "night_start",
        "teleport", "increase_house_points", "sly_plus",
        "spit_on_her", "kiss_her", "slap_her", "give_reward", "popup",
    ]

    if isinstance(node, ast.Jump):
        label = node.target
        return any(fnmatchcase(label, p) for p in label_patterns)

    if isinstance(node, ast.Call):
        label = node.label
        return any(fnmatchcase(label, p) for p in label_patterns)

    return False


# Old code (reusable?)


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
