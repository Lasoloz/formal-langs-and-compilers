import sys
from utils.automaton import Automaton
from utils.f1Tools import remove_unreachable, remove_unproductive


def main():
    automaton = Automaton.read_automaton(sys.stdin)
    new_automaton = remove_unproductive(remove_unreachable(automaton))
    new_automaton.write(sys.stdout)


main()
