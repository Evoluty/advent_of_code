# Should return 909
def all_cells(starting_cell_x, starting_cell_y, x_size, y_size):
    for j in range(x_size):
        for i in range(y_size):
            yield (starting_cell_x + j, starting_cell_y + i)


def is_claim_non_overlapped(claimed_cells, starting_cell_x, starting_cell_y, x_size, y_size):
    for cell in all_cells(starting_cell_x, starting_cell_y, x_size, y_size):
        if claimed_cells[cell] != 1:
            return False
    return True


def get_non_overlapped_claim_id():
    with open('input') as f:
        claimed_cells = {}

        for line in f:
            claim = line.replace(':', '').split(' ')

            (starting_cell_x, starting_cell_y) = map(int, claim[2].split(','))
            (x_size, y_size) = map(int, claim[3].split('x'))

            for cell in all_cells(starting_cell_x, starting_cell_y, x_size, y_size):
                if cell in claimed_cells:
                    claimed_cells[cell] += 1
                else:
                    claimed_cells[cell] = 1

        f.seek(0)
        for line in f:
            claim = line.replace(':', '').split(' ')

            claim_id = int(claim[0].replace('#', ''))
            (starting_cell_x, starting_cell_y) = map(int, claim[2].split(','))
            (x_size, y_size) = map(int, claim[3].split('x'))

            if is_claim_non_overlapped(claimed_cells, starting_cell_x, starting_cell_y, x_size, y_size):
                return claim_id
    return None


print(get_non_overlapped_claim_id())
