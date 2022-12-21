def read_depths(infile='aoc1_input.txt'):
    with open(infile) as f:
        depths = []
        for line in f:
            depths.append(int(line.strip()))
        return depths

if __name__ == '__main__':
    #depths = read_depths('aoc1_sample.txt')
    depths = read_depths()
    prev_depth = None
    count = 0
    for depth in depths:
        if prev_depth and depth > prev_depth:
            count += 1
        prev_depth = depth
    print('The answer is {}.'.format(count))
