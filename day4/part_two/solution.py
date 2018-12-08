# Should return 117061
from datetime import datetime
from collections import Counter, defaultdict


def load_actions():
    actions = []
    with open('input') as f:
        for line in f:
            str_date, action = line.replace('[', '').replace('] ', ']').replace('\n', '').split(']')
            date = datetime.strptime(str_date, '%Y-%m-%d %H:%M')

            if 'Guard' in action:
                guard_id, action = action.split('#')[1].split(' ', maxsplit=1)
                guard_id = int(guard_id)
            else:
                guard_id = None

            actions.append({
                'date': date,
                'guard_id': guard_id,
                'action': action
            })

    actions.sort(key=lambda x: x['date'])
    return actions


def get_minutes_between(start, end):
    for i in range(start.minute, end.minute):
        yield i


def find_most_asleep_guard_in_same_minute(actions):
    asleep_minutes = defaultdict(Counter)
    current_guard = None
    last_dates = {}
    for action in actions:
        if action['guard_id']:
            current_guard = action['guard_id']
        elif action['action'] == 'falls asleep':
            last_dates[current_guard] = action['date']
        elif action['action'] == 'wakes up':
            for minute in get_minutes_between(last_dates[current_guard], action['date']):
                asleep_minutes[current_guard][minute] += 1

    guard = None
    cur_most_slept_minute = None
    for cur_guard, guard_asleep_minutes in asleep_minutes.items():
        guard_most_common = guard_asleep_minutes.most_common(1)[0][0]
        if not cur_most_slept_minute or guard_most_common > cur_most_slept_minute:
            cur_most_slept_minute = guard_most_common
            guard = cur_guard

    return guard, cur_most_slept_minute


all_actions = load_actions()
guard_id, most_slept_minute = find_most_asleep_guard_in_same_minute(all_actions)

print(guard_id * most_slept_minute)
