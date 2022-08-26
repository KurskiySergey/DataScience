from itertools import count, cycle
from functools import partial


def counter(start=3):
    for el in count(start):
        print(el)
        if el > start * 10:
            break


def word_cycle(word="hello", stop_percent=10):
    stop_write = len(word) + len(word) / 100 * stop_percent
    print()
    for letter in cycle(word):
        print(letter)
        stop_write -= 1
        if stop_write <= 0:
            print()
            break


word_cycle_25 = partial(word_cycle, stop_percent=25)

if __name__ == "__main__":
    counter(start=3)
    word_cycle(word="hello", stop_percent=100)
    word_cycle_25(word="world")
