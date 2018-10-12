import sys
from utils.automaton import Automaton
from utils.f5Tools import generate_dot_code


def main():
    automaton = Automaton.read_automaton(sys.stdin)
    generate_dot_code(automaton, sys.stdout)


main()
