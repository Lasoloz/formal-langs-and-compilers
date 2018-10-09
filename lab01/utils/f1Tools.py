from utils.automaton import Automaton


class UnreachableRemover:
    new_automaton = Automaton()
    found_stack = []

    def get_algo_start_points(self, automaton):
        return automaton.startPoints

    def add_algo_start_point(self, start_point):
        self.new_automaton.add_start_point(start_point)

    def get_filter(self, item):
        return lambda conn : conn.first == item

    def get_next_point(self, connection):
        return connection.second

    def get_algo_end_points(self, automaton):
        return automaton.endPoints

    def add_algo_end_point(self, end_point):
        self.new_automaton.add_end_point(end_point)


class UnproductiveRemover:
    new_automaton = Automaton()
    found_stack = []

    def get_algo_start_points(self, automaton):
        return automaton.endPoints

    def add_algo_start_point(self, start_point):
        self.new_automaton.add_end_point(start_point)

    def get_filter(self, item):
        return lambda conn : conn.second == item

    def get_next_point(self, connection):
        return connection.first

    def get_algo_end_points(self, automaton):
        return automaton.startPoints

    def add_algo_end_point(self, end_point):
        self.new_automaton.add_start_point(end_point)


def remove_unreachable(automaton):
    return __remove_helper__(automaton, UnreachableRemover())


def remove_unproductive(automaton):
    return __remove_helper__(automaton, UnproductiveRemover())


def __remove_helper__(automaton, remover):
    for item in remover.get_algo_start_points(automaton):
        remover.new_automaton.add_node(item)
        remover.add_algo_start_point(item)

        remover.found_stack.append(item)

        while len(remover.found_stack) > 0:
            current = remover.found_stack.pop()

            __find_connection__(remover, current, automaton)

    return remover.new_automaton


def __find_connection__(remover, current, automaton):
    for connection in filter(remover.get_filter(current), automaton.connections):
        if not(remover.get_next_point(connection) in remover.new_automaton.nodes):
            __add_new_node__(remover, connection, automaton)

        remover.new_automaton.add_connection(
            connection.first, connection.value, connection.second)


def __add_new_node__(remover, connection, automaton):
    next_point = remover.get_next_point(connection)
    remover.found_stack.append(next_point)
    remover.new_automaton.add_node(next_point)
    remover.new_automaton.abc.add(connection.value)

    if next_point in remover.get_algo_end_points(automaton):
        remover.add_algo_end_point(next_point)
