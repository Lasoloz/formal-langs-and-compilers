from utils.details import connection
from sys import stdout, stdin


class Automaton:
    @staticmethod
    def read_automaton(inputObj):
        states = stdin.readline().rsplit()
        abc = stdin.readline().rsplit()
        startPoints = stdin.readline().rsplit()
        endPoints = stdin.readline().rsplit()
        connections = []

        possibleConnection = stdin.readline().rsplit()
        while len(possibleConnection) == 3:
            connections.append(possibleConnection)
            possibleConnection = stdin.readline().rsplit()

        return process_input(states, abc, startPoints, endPoints, connections)

    def __init__(self):
        self.nodes = []
        self.connections = []
        self.startPointIdxs = set()
        self.endPointIdxs = set()

        self.abc = set()

    def add_node(self, node):
        self.nodes.append(node)
        self.connections.append([])

    def add_connection(self, firstIdx, value, secondIdx):
        nodes = self.nodes
        if firstIdx < len(nodes) and secondIdx < len(nodes):
            self.connections[firstIdx].append(
                connection.Connection(firstIdx, value, secondIdx))

        self.abc.add(value)

    def add_start_point_index(self, index):
        self.startPointIdxs.add(index)

    def add_end_point_index(self, index):
        self.endPointIdxs.add(index)

    def write(self, out):
        for node in self.nodes:
            out.write(str(node) + ' ')
        out.write('\n')

        for item in self.abc:
            out.write(str(item) + ' ')
        out.write('\n')

        for idx in self.startPointIdxs:
            out.write(str(self.nodes[idx]) + ' ')
        out.write('\n')

        for idx in self.endPointIdxs:
            out.write(str(self.nodes[idx]) + ' ')
        out.write('\n')

        for nodeConnections in self.connections:
            for connection in nodeConnections:
                fNode = self.nodes[connection.fromNode]
                value = connection.value
                tNode = self.nodes[connection.toNode]
                out.write(str(fNode) + ' ' + str(value) +
                          ' ' + str(tNode) + '\n')


def process_input(states, abc, startPoints, endPoints, connections):
    automaton = Automaton()
    abcSet = set()

    for state in states:
        automaton.add_node(state)

    for item in abc:
        abcSet.add(item)

    for startPoint in startPoints:
        pointIdx = automaton.nodes.index(startPoint)
        automaton.add_start_point_index(pointIdx)

    for endPoint in endPoints:
        pointIdx = automaton.nodes.index(endPoint)
        automaton.add_end_point_index(pointIdx)

    for connection in connections:
        value = connection[1]
        if not(value in abcSet):
            raise BaseException("Invalid input: value (" + connection[1] + ") not present in abc!")
        fromPointIdx = automaton.nodes.index(connection[0])
        toPointIdx = automaton.nodes.index(connection[2])
        automaton.add_connection(fromPointIdx, value, toPointIdx)

    return automaton
