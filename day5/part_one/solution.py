# Should return 9172
def get_polymer():
    with open('input') as f:
        return f.readline()


# @todo: need improvement
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


line = get_polymer()
final_polymer = react_polymer(line)

print(final_polymer)
print(len(final_polymer))
