# Should return 45290
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


def get_closest_area_size(max_distance, board, all_points):
    area = 0
    for j, line in enumerate(board):
        for i, cell in enumerate(line):
            distance = 0
            for point in all_points:
                distance += get_manhattan_distance((i, j), point)
            if distance < max_distance:
                area += 1
    return area


points = load_data()
board = build_board(points)
board = fill_board(board, points)
area_size = get_closest_area_size(10000, board, points)

print(area_size)
