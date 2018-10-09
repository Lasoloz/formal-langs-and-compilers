import sys
from utils import inputUtils
from utils.automaton import Automaton
from utils.f1Tools import remove_closed_states

def main():
    # line = sys.stdin.readline()
    # print(line)

    automaton = Automaton.read_automaton(sys.stdin)
    # automaton.write(sys.stdout)
    corrected = remove_closed_states(automaton)
    corrected.write(sys.stdout)

    # automaton = Automaton()
    # automaton.add_node('a')
    # automaton.add_node('b')
    # automaton.add_node('c')
    # automaton.add_connection(0, 3, 1)
    # automaton.add_connection(1, 4, 0)
    # automaton.add_connection(2, 3, 0)
    # automaton.write(sys.stdout)
    # removeClosedStates.remove_closed_states(automaton)


main()
