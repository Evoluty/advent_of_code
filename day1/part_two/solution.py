# Should print 71892
def first_twice_occurrences_frequency():
    frequency = 0
    seen_frequencies = {frequency}

    with open('input') as f:
        while 1:
            for line in f:
                frequency += int(line)

                if frequency in seen_frequencies:
                    return frequency

                seen_frequencies.add(frequency)

            f.seek(0)


print(first_twice_occurrences_frequency())
