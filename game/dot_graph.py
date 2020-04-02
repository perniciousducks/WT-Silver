
import ast as py_ast
import renpy.ast as ast
import renpy.store as store
from renpy.game import script
from graphviz import Digraph


def event_graphs(filename):

    def event_group(event):
        return event.events[0][0][0][:2] # First event label
        #return event.start_label[:2]

    events = [x for x in store.__dict__.itervalues() if isinstance(x, store.event_class)]
    events = sorted(events, key=event_group)

    g = Digraph()
    g.attr(concentrate="true", pack="36",packmode="array_cu", rankdir="LR")

    for event in events:
        event_graph = get_event_subgraph(event)
        g.subgraph(event_graph)

    print("Rendering graph...")

    g.format = "png"
    g.render(filename, view=True)


def get_event_subgraph(event):
    sg = Digraph("cluster_{}".format(event.start_label))
    sg.attr(label="{} ({})".format(event.start_label, event.title))

    visited = set()
    for tier in event.events:
        for start, _ in tier:
            sg.node(start, style="filled")

            node = script.lookup(start)
            visited.add(start)
            visitor = ast_visitor(start, sg, visited)
            node.get_children(visitor)

    return sg


def ast_visitor(start, graph, visited):
    def visit(node):
        target = None

        if ignore_node(node):
            return

        if isinstance(node, ast.Jump):
            target = node.target
            graph.edge(start, target)

        if isinstance(node, ast.Call) and not node.expression:
            target = node.label
            graph.edge(start, target, style="bold")

        if target and target not in visited:
            visited.add(target)
            visitor = ast_visitor(target, graph, visited)
            script.lookup(target).get_children(visitor)

    return visit


def ignore_node(node):
    label_startswith = tuple([
        "end_", "main_room", "play_", "play_", "update_", "blkfade", "hide", "nar", "bld",
        "ctc", "reset_", "room", "day_", "night_", "common_", "chibi_", "set_", "blk",
        "sly_plus", "give_reward", "teleport", "too_much", "increase_house_points",
        "popup", "spit_on_her", "kiss_her", "slap_her"
    ])
    label_endswith = tuple(["_main", "_walk", "_chibi", "_block", "_chibi_scene"])

    if isinstance(node, ast.Jump):
        label = node.target
        return label.startswith(label_startswith) or label.endswith(label_endswith)

    if isinstance(node, ast.Call):
        label = node.label
        return label.startswith(label_startswith) or label.endswith(label_endswith)

    return False


# Old code (reusable?)


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
