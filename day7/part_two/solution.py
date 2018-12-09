# should return 1024
def load_data(file_name):
    with open(file_name) as f:
        all_steps = set()
        all_dependencies = []
        for line in f:
            elems = line.split(' ')

            all_dependencies.append((elems[1], elems[7]))

            all_steps.add(elems[1])
            all_steps.add(elems[7])

    return all_steps, all_dependencies


def find_next_steps(all_steps, all_dependencies):
    possibilities = []
    for stp in all_steps:
        found = False
        for dep in all_dependencies:
            if dep[1] == stp:
                found = True
                break
        if not found:
            possibilities.append(stp)
    return possibilities


def mark_done(dep, stp, all_dependencies):
    return set({s for s in stp if s != dep}), [s for s in all_dependencies if s[0] != dep]


def execute_steps(nb_workers, task_flat_duration, stp, dep):
    current_steps = {}
    seconds = 0
    while len(stp) != 0:
        # mark ended tasks as done
        for k, val in {key: value - 1 for key, value in current_steps.items() if value == 1}.items():
            stp, dep = mark_done(k, stp, dep)
        current_steps = {key: value - 1 for key, value in current_steps.items() if value != 1}

        # if all workers are busy : continue
        if len(current_steps) == nb_workers:
            seconds += 1
            continue

        # check steps that can be done and assign new tasks
        next_steps = find_next_steps(stp, dep)
        while next_steps and len(current_steps) != nb_workers:
            selected_step = next_steps.pop()
            if selected_step in current_steps:
                continue
            current_steps[selected_step] = task_flat_duration + ord(selected_step) - ord('A') + 1

        seconds += 1

    return seconds - 1


steps, dependencies = load_data(file_name='input')
result = execute_steps(nb_workers=5, task_flat_duration=60, stp=steps, dep=dependencies)
print(result)
