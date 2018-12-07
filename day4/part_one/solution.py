# Should return 4716
from datetime import datetime
from collections import Counter


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


def find_most_asleep_guard(actions):
    guard_sleep = Counter()
    current_guard = None
    last_date = None
    for action in actions:
        if action['guard_id']:
            current_guard = action['guard_id']
        elif action['action'] == 'falls asleep':
            last_date = action['date']
        elif action['action'] == 'wakes up':
            sleep_time = action['date'] - last_date
            guard_sleep[current_guard] += sleep_time.total_seconds()

    return guard_sleep.most_common(1)[0][0]


def get_minutes_between(start, end):
    for i in range(start.minute, end.minute):
        yield i


def find_best_minute(actions, guard_id):
    asleep_minutes = Counter()
    current_guard = None
    last_date = None
    for action in actions:
        if action['guard_id']:
            current_guard = action['guard_id']
        if current_guard == guard_id:
            if action['action'] == 'falls asleep':
                last_date = action['date']
            elif action['action'] == 'wakes up':
                for minute in get_minutes_between(last_date, action['date']):
                    asleep_minutes[minute] += 1

    return asleep_minutes.most_common(1)[0][0]


all_actions = load_actions()
guard_most_asleep_id = find_most_asleep_guard(all_actions)
best_minute = find_best_minute(all_actions, guard_most_asleep_id)

print(guard_most_asleep_id * best_minute)
