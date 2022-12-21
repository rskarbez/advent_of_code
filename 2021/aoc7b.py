from math import inf

def mean(data):
    sum_data = count = 0
    for i in data:
        sum_data += i
        count += 1
    return sum_data / count

def eulers_fcn(n):
    return (n * (n + 1)) / 2

def fuel_costs(data):
    data.sort()
    costs = {i:0 for i in range(min(data), max(data)+1)}
    for k in costs:
        for i in data:
            costs[k] += eulers_fcn(abs(i - k))
    return costs

def read_crabs(infile='aoc7_input.txt'):
    with open(infile) as f:
        crabs = []
        for line in f:
            temp = line.strip().split(',')
            crabs = [int(i) for i in temp]
        return crabs

if __name__ == '__main__':
    #crabs = read_crabs('aoc7_sample.txt')
    crabs = read_crabs()
    costs = fuel_costs(crabs)

    min_cost = inf
    min_index = inf
    for k,v in costs.items():
        if v < min_cost:
            min_cost = v
            min_index = k

    print('Minimum fuel is {} at position {}'.format(min_cost, min_index))
