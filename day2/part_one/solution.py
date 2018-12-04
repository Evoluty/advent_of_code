# Should return 6000
from collections import Counter


def checksum():
    with open('input') as f:
        global_counts = {2: 0, 3: 0}
        for line in f:
            occurrences = {2: False, 3: False}
            for letter_occurrence in Counter(line).values():
                if letter_occurrence == 2:
                    occurrences[2] = True
                elif letter_occurrence == 3:
                    occurrences[3] = True

                # Optimisation
                if occurrences.get(2) and occurrences.get(3):
                    break

            if occurrences.get(2):
                global_counts[2] += 1
            if occurrences.get(3):
                global_counts[3] += 1

        return global_counts[2] * global_counts[3]


print(checksum())
