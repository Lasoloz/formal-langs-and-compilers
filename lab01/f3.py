import sys
from utils.automaton import Automaton
from utils.f3Tools import check_word_in_automaton


def main():
    word = sys.stdin.readline().rstrip()
    automaton = Automaton.read_automaton(sys.stdin)
    if check_word_in_automaton(automaton, word):
        print("Word is present!")
    else:
        print("word is not present!")


main()
