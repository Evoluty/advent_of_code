# should return GDHOSUXACIMRTPWNYJLEQFVZBK
def load_data():
    with open('input') as f:
        all_steps = set()
        all_dependencies = []
        for line in f:
            elems = line.split(' ')

            all_dependencies.append((elems[1], elems[7]))

            all_steps.add(elems[1])
            all_steps.add(elems[7])

    return all_steps, all_dependencies


def find_first(all_steps, all_dependencies):
    possibilities = []
    for stp in all_steps:
        found = False
        for dep in all_dependencies:
            if dep[1] == stp:
                found = True
                break
        if not found:
            possibilities.append(stp)

    return min(possibilities, key=ord)


def remove(dep, all_dependencies):
    return [s for s in all_dependencies if s[0] != dep]


def get_correct_order(stp, dpd):
    res = ''
    for i in range(len(stp)):
        step = find_first(stp, dpd)

        steps.remove(step)
        dpd = remove(step, dpd)

        res = ''.join([res, step])

    return res


steps, dependencies = load_data()
response = get_correct_order(steps, dependencies)

print(response)
