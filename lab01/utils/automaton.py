from utils.details.connection import Connection
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
        self.nodes = set()
        self.connections = []
        self.startPoints = set()
        self.endPoints = set()

        self.abc = set()

    def add_node(self, node):
        self.nodes.add(node)

    def add_connection(self, first, value, second):
        if first in self.nodes and second in self.nodes and value in self.abc:
            self.connections.append(Connection(first, value, second))
        else:
            raise BaseException("Invalid connection!")

    def add_start_point(self, point):
        self.startPoints.add(point)

    def add_end_point(self, point):
        self.endPoints.add(point)

    def write(self, out):
        for node in self.nodes:
            out.write(str(node) + ' ')
        out.write('\n')

        for item in self.abc:
            out.write(str(item) + ' ')
        out.write('\n')

        for item in self.startPoints:
            out.write(str(item) + ' ')
        out.write('\n')

        for item in self.endPoints:
            out.write(str(item) + ' ')
        out.write('\n')

        for connection in self.connections:
            out.write(str(connection.first) + ' ' +
                      str(connection.value) + ' ' + str(connection.second) + '\n')


def process_input(states, abc, startPoints, endPoints, connections):
    automaton = Automaton()

    for state in states:
        automaton.add_node(state)

    for item in abc:
        automaton.abc.add(item)

    for startPoint in startPoints:
        automaton.add_start_point(startPoint)

    for endPoint in endPoints:
        automaton.add_end_point(endPoint)

    for connection in connections:
        automaton.add_connection(connection[0], connection[1], connection[2])

    return automaton
