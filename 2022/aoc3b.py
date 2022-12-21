def read_input(infile='aoc3_input.txt'):
    rucksacks = []
    with open(infile) as f:
        for line in f:
            rucksack = line.strip()
            rucksacks.append(rucksack)
    return rucksacks

def find_repeated_item(elf1, elf2, elf3):
    repeated_item = 0
    for c in elf1:
        match2 = elf2.find(c)
        match3 = elf3.find(c)
        if match2 != -1 and match3 != -1:
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
    i = 0
    while i < len(rucksacks):
        elf1 = rucksacks[i]
        elf2 = rucksacks[i+1]
        elf3 = rucksacks[i+2]
        repeated_item = find_repeated_item(elf1, elf2, elf3)
        priority = convert_to_priority(repeated_item)
        print('{} ({})'.format(repeated_item, priority))
        priority_sum += priority
        i += 3
    print('The sum of priorities of repeated items is: ', priority_sum)

