def read_depths(infile='aoc1_input.txt'):
    with open(infile) as f:
        depths = []
        for line in f:
            depths.append(int(line.strip()))
        return depths

if __name__ == '__main__':
    depths = read_depths('aoc1_sample.txt')
    #depths = read_depths()
    depth_triples = [sum(depths[i:i+3]) for i in range(len(depths[:-2]))]
    prev_depth = None
    count = 0
    for t in depth_triples:
        if prev_depth and t > prev_depth:
            count += 1
        prev_depth = t
    print('The answer is {}.'.format(count))
