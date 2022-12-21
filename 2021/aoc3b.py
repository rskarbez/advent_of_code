def read_numbers(infile='aoc3_input.txt'):
    with open(infile) as f:
        numbers = []
        for line in f:
            #numbers.append((int(line.strip(), base=2), line.strip()))
            numbers.append(line.strip())
        return numbers

def count_ones_in_column(numbers, flags, column):
    ones = 0
    for i, s in enumerate(numbers):
        if flags[i] and s[column] == '1':
            ones += 1
    return ones

if __name__ == '__main__':
    #numbers = read_numbers('aoc3_sample.txt')
    numbers = read_numbers()
    oxygen_flags = [1 for _ in range(len(numbers))]
    co2_flags = [1 for _ in range(len(numbers))]
    oxygen_index = -1
    co2_index = -1
    for column in range(len(numbers[0])):
        oxygen_ones = count_ones_in_column(numbers, oxygen_flags, column)
        co2_ones = count_ones_in_column(numbers, co2_flags, column)
        oxygen_thresh = sum(oxygen_flags) / 2
        co2_thresh = sum(co2_flags) / 2
        oxygen_val = 1
        co2_val = 0
        if oxygen_ones < oxygen_thresh:
            oxygen_val = 0
        if co2_ones < co2_thresh:
            co2_val = 1
        for i, num in enumerate(numbers):
            if oxygen_index == -1 and int(num[column]) != oxygen_val:
                oxygen_flags[i] = 0
            if co2_index == -1 and int(num[column]) != co2_val:
                co2_flags[i] = 0
        if sum(oxygen_flags) <= 1:
            for i, flag in enumerate(oxygen_flags):
                if flag:
                    print('Oxygen value for index {}: {} ({})'.format(i, int(numbers[i], base=2), numbers[i]))
                    oxygen_index = i
        if sum(co2_flags) <= 1:
            for i, flag in enumerate(co2_flags):
                if flag:
                    print('CO2 value for index {}: {} ({})'.format(i, int(numbers[i], base=2), numbers[i]))
                    co2_index = i
        if oxygen_index != -1 and co2_index != -1:
            break

    oxygen = int(numbers[oxygen_index], base=2)
    co2 = int(numbers[co2_index], base=2)
    #print('Oxygen: {}'.format(oxygen))
    #print('CO2: {}'.format(co2))
    print('The life support rating is {}'.format(oxygen * co2))


