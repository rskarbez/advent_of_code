def read_input(infile='aoc3_input.txt'):
    rucksacks = []
    with open(infile) as f:
        for line in f:
            rucksack = line.strip()
            rucksacks.append(rucksack)
    return rucksacks

def find_repeated_item(rucksack):
    sack_size = len(rucksack)
    compartment_size = sack_size // 2
    compartment1 = rucksack[:compartment_size]
    compartment2 = rucksack[compartment_size:]
    repeated_item = 0
    for c in compartment1:
        if c in compartment2:
            return c

def convert_to_priority(c):
    if c.isupper():
        return ord(c) - 38
    elif c.islower():
        return ord(c) - 96
    else:
        print('{} is not a valid character'.format(c))
        return None

if __name__ == '__main__':
    #rucksacks = read_input('aoc3_sample.txt')
    rucksacks = read_input()
    priority_sum = 0
    for rucksack in rucksacks:
        repeated_item = find_repeated_item(rucksack)
        priority = convert_to_priority(repeated_item)
        print('{} ({})'.format(repeated_item, priority))
        priority_sum += priority
    print('The sum of priorities of repeated items is: ', priority_sum)

