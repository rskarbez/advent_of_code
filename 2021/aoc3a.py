def read_numbers(infile='aoc3_input.txt'):
    with open(infile) as f:
        numbers = []
        for line in f:
            numbers.append((int(line.strip(), base=2), line.strip()))
        return numbers

if __name__ == '__main__':
    #numbers = read_numbers('aoc3_sample.txt')
    numbers = read_numbers()
    one_counts = [0 for _ in range(len(numbers[0][1]))]
    for b, s in numbers:
        for i, c in enumerate(s):
            if c == '1':
                one_counts[i] += 1
    print('# of 1s for each bit:')
    print(one_counts)
    gamma = 0
    epsilon = 0
    thresh = len(numbers) // 2
    for i, count in enumerate(one_counts[::-1]):
        if count >= thresh:
            gamma += (2**i)
        else:
            epsilon += (2**i)
    print('Gamma: {}'.format(gamma))
    print('Epsilon: {}'.format(epsilon))
    print('The power consumption rate is {}'.format(gamma * epsilon))


