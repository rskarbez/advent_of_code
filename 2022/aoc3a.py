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
    # // 2, instead of / 2, to make sure we get an integer value
    # (a float would result in an IndexError)
    compartment1 = rucksack[:compartment_size]
    # First half
    compartment2 = rucksack[compartment_size:]
    # Second half
    repeated_item = 0
    for c in compartment1:
        if c in compartment2:
        # Surely a faster way to do this than nested loops, but it works
            return c

def convert_to_priority(c):
    # The ord function, applied to a single character, returns its ASCII
    # code
    # ASCII Table: https://www.asciitable.com/
    # Note that in the ASCII Table, uppercase characters come before
    # lowercase characters (and there's some stuff in between)
    # This doesn't neatly map to our item priority values! But at least
    # we can still rely on the fact that letters appear in order...
    if c.isupper():
        return ord(c) - 38
    elif c.islower():
        return ord(c) - 96
    else:
        # Added a wee tiny bit of error checking here, not strictly
        # necessary
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

