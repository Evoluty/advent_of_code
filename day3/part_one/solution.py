# Should return 101781
def all_cells(starting_cell_x, starting_cell_y, x_size, y_size):
    for j in range(x_size):
        for i in range(y_size):
            yield (starting_cell_x + j, starting_cell_y + i)


def get_count_overlapping_cells():
    with open('input') as f:
        claimed_cell = {}

        for line in f:
            claim = line.replace(':', '').split(' ')

            (starting_cell_x, starting_cell_y) = map(int, claim[2].split(','))
            (x_size, y_size) = map(int, claim[3].split('x'))

            for cell in all_cells(starting_cell_x, starting_cell_y, x_size, y_size):
                if cell in claimed_cell:
                    claimed_cell[cell] += 1
                else:
                    claimed_cell[cell] = 1

    overlapping_set = {cell for cell, count in claimed_cell.items() if count > 1}
    return len(overlapping_set)


print(get_count_overlapping_cells())
