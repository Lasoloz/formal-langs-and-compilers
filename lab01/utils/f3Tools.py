from utils.automaton import Automaton


class Checker:
    def __init__(self, automaton, current, word):
        self.automaton = automaton
        self.current = current
        self.word = word
        self.level = 0


def check_word_in_automaton(automaton, word):
    for start_point in automaton.startPoints:
        if __check_character_in_automaton__(
                Checker(automaton, start_point, word), 0):
            return True

    return False


def __check_character_in_automaton__(checker, char_index):
    if char_index == len(checker.word):
        return checker.current in checker.automaton.endPoints

    conns = filter(lambda conn: conn.first == checker.current,
                   checker.automaton.connections)

    for conn in conns:
        if conn.value == checker.word[char_index]:
            if __check_character_in_automaton__(Checker(checker.automaton, conn.second, checker.word), char_index + 1):
                return True

    return False
