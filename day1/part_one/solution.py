# Should print 516
def final_frequency():
    frequency = 0

    with open('input') as f:
        for line in f:
            frequency += int(line)

    return frequency


print(final_frequency())
