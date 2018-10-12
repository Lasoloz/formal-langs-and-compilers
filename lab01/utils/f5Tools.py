import sys


def generate_dot_code(automaton, out):
    out.write("digraph G{\n")
    __generate_basic_data__(out)
    __add_start_points__(automaton, out)
    __add_end_points__(automaton, out)
    __add_edge_data__(automaton, out)
    out.write("}\n")


def __generate_basic_data__(out):
    out.writelines([
        "ranksep=0.5;\n",
        "nodesep=0.5;\n",
        "rankdir=LR;\n",
        "node [shape=\"circle\",fontsize=\"16\"];\n",
        "fontsize=\"10\";\n",
        "compound=true;\n"
    ])


def __add_start_points__(automaton, out):
    for point in automaton.startPoints:
        out.write("i" + str(point) + " [shape=point, style=invis];\n")


def __add_end_points__(automaton, out):
    for point in automaton.endPoints:
        out.write(str(point) + " [shape=doublecircle];\n")


def __add_edge_data__(automaton, out):
    __add_starting_edge_data__(automaton, out)
    __add_real_edge_data__(automaton, out)


def __add_starting_edge_data__(automaton, out):
    for point in automaton.startPoints:
        out.write("i" + str(point) + " -> " + str(point) + ";\n")


def __add_real_edge_data__(automaton, out):
    for connection in automaton.connections:
        out.write(str(connection.first) + " -> " + str(connection.second) +
                  " [label=" + str(connection.value) + "];\n")
