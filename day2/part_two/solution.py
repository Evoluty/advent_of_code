# Should return pbykrmjmizwhxlqnasfgtycdv
def get_best_matching_letters():
    best_matching_letters = ''

    with open('input') as file_a, open('input') as file_b:
        for line_a in file_a:
            for line_b in file_b:
                if line_a != line_b:
                    letters = letters_in_common(line_a, line_b)
                    if len(letters) > len(best_matching_letters):
                        best_matching_letters = letters
            file_b.seek(0)
    return best_matching_letters


def letters_in_common(box_a_id, box_b_id):
    common_letters = ''
    for letter_a, letter_b in zip(box_a_id, box_b_id):
        if letter_a == letter_b:
            common_letters = ''.join([common_letters, letter_a])
    return common_letters


print(get_best_matching_letters())
