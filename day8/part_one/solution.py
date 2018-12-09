# Should return 35911
import sys
sys.setrecursionlimit(3000)


def load_data(file_name):
    with open(file_name) as f:
        line = f.readline()
    return list(map(int, line.split()))


# @todo: does not work
def decode_metadata(code):
    if len(code) == 0:
        print(code)
        return 0

    node_childs_number, node_metadata_number = code[0], code[1]

    node_metadata_sum = 0
    if node_childs_number == 0:
        node_metadata_sum += sum(code[2: 2 + node_metadata_number])
        nxt = 2 + node_metadata_number
        end = len(code)
    else:
        node_metadata_sum = sum(code[len(code) - node_metadata_number:])
        nxt = 2
        end = len(code) - node_metadata_number

    return node_metadata_sum + decode_metadata(code[nxt:end])


chain = load_data('input')
result = decode_metadata(chain)

print(result)
assert(result == 35911)
