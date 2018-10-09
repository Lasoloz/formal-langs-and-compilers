from utils.automaton import Automaton


class RemoveState:
    def __init__(self, automaton):
        self.automaton = automaton
        self.workStack = []
        self.abc = set()
        self.found = set()
        self.startPoints = set()
        self.endPoints = set()


def remove_closed_states(automaton):
    removeState = RemoveState(automaton)
    workStack = removeState.workStack

    for startPointIdx in automaton.startPointIdxs:
        workStack.append(startPointIdx)
        removeState.found.add(automaton.nodes[startPointIdx])
        removeState.startPoints.add(automaton.nodes[startPointIdx])

        while len(workStack) > 0:
            current = workStack.pop()

            __find_connections__(removeState, current)

    return __create_automaton__(removeState)


def __find_connections__(removeState, current):
    for connection in removeState.automaton.connections[current]:
        toNodeIdx = connection.toNode
        toNode = removeState.automaton.nodes[toNodeIdx]
        if not(toNode in removeState.found):
            removeState.found.add(toNode)
            removeState.abc.add(connection.value)
            removeState.workStack.append(toNodeIdx)

            if toNodeIdx in removeState.automaton.endPointIdxs:
                removeState.endPoints.add(toNode)

def __create_automaton__(removeState):
    automaton = Automaton()

    for item in removeState.found:
        automaton.add_node(item)

    for remaining in removeState.found:
        remainingIdx = removeState.automaton.nodes.index(remaining)
        for connection in removeState.automaton.connections[remainingIdx]:
            toNodePoint = removeState.automaton.nodes[connection.toNode]
            if toNodePoint in removeState.found:
                fromNodeIdx = automaton.nodes.index(remaining)
                toNodeIdx = automaton.nodes.index(toNodePoint)
                automaton.add_connection(fromNodeIdx, connection.value, toNodeIdx)

    for point in removeState.startPoints:
        automaton.add_start_point_index(automaton.nodes.index(point))

    for point in removeState.endPoints:
        automaton.add_end_point_index(automaton.nodes.index(point))

    return automaton
