# Should return 6550
import string
import sys


def get_polymer():
    with open('input') as f:
        return f.readline()


# @todo: really need to rework this function: this script has 15 minutes runtime...
def react_polymer(chain):
    change_happens = True
    while change_happens:
        change_happens = False
        for pos, polymer in enumerate(chain):
            if pos < len(chain) - 1 and chain[pos+1] == polymer.swapcase():
                change_happens = True
                chain = ''.join([chain[:pos], chain[pos+2:]])
                break
    return chain


def find_best_polymer_length():
    min_length = sys.maxsize

    for letter in string.ascii_lowercase:
        print('check for letter ' + letter)
        line = get_polymer()
        line = line.replace(letter, '').replace(letter.swapcase(), '')
        reacted_polymer = react_polymer(line)

        length = len(reacted_polymer)
        if length < min_length:
            min_length = length

    return min_length


print(find_best_polymer_length())
