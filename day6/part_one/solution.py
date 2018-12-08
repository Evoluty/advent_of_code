# Should return
from collections import Counter


def load_data():
    data = []
    with open('input') as f:
        for line in f:
            x, y = map(int, line.split(','))
            data.append((x, y))
    return data


def get_manhattan_distance(x, y):
    return abs(y[0] - x[0]) + abs(y[1] - x[1])


def get_farest_corner(all_points):
    max_x = max_y = 0
    for point in all_points:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
    return max_x, max_y


def print_board(board):
    for line in board:
        for cell in line:
            print(cell, end=' ')
        print()


def build_board(all_points):
    b = []
    corner = get_farest_corner(all_points)
    for j in range(corner[1] + 1):
        array = []
        for i in range(corner[0] + 1):
            array.append('.')
        b.append(array)

    for i, point in enumerate(all_points):
        b[point[1]][point[0]] = i + 1
    return b


def get_cell_value(j, i, all_points):
    distances = {}

    for p, point in enumerate(all_points):
        key = p + 1
        cur_distance = get_manhattan_distance((i, j), point)
        if key not in distances.keys() or cur_distance < distances[key]:
            distances[p + 1] = cur_distance

    minimum_val = min(distances.values())
    amount_of_time = sum(1 for v in distances.values() if v == minimum_val)
    if amount_of_time != 1:
        return '.'

    return min(distances, key=distances.get)


def fill_board(board, all_points):
    for j, line in enumerate(board):
        for i, cell in enumerate(line):
            if (i, j) not in all_points:
                board[j][i] = get_cell_value(j, i, all_points)
    return board


def get_borders_values(b):
    for j in range(len(b)):
        for i in range(len(b[0])):
            if j == 0 or j == len(b) - 1:
                yield (j, i)
            elif i == 0 or i == len(b[0]) - 1:
                yield (j, i)


def get_non_infinite_coordinates(board):
    borders_values = set()
    for t in get_borders_values(board):
        value = board[t[0]][t[1]]
        if value != '.':
            borders_values.add(value)
    return borders_values


def find_greatest_coordinate_size(board, not_infinite_points):
    cnt = Counter()
    for line in board:
        for cell in line:
            if cell not in not_infinite_points:
                cnt[cell] += 1

    return cnt.most_common(1)[0][1]


points = load_data()
board = build_board(points)
board = fill_board(board, points)
non_infinite_coordinates = get_non_infinite_coordinates(board)
greatest_coordinate = find_greatest_coordinate_size(board, non_infinite_coordinates)

print(greatest_coordinate)
