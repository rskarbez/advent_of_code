def read_input(infile='aoc4_input.txt'):
    elf_pairs = []
    with open(infile) as f:
        for line in f:
            (elf1, elf2) = line.strip().split(',')
            elf_pairs.append((elf1, elf2))
    return elf_pairs

if __name__ == '__main__':
    #elf_pairs = read_input('aoc4_sample.txt')
    elf_pairs = read_input()
    total_contains = 0
    for (elf1, elf2) in elf_pairs:
        (elf1begin, elf1end) = elf1.split('-')
        (elf2begin, elf2end) = elf2.split('-')
        if ((int(elf1begin) <= int(elf2begin)) and (int(elf1end) >= int(elf2end))) or ((int(elf2begin) <= int(elf1begin)) and (int(elf2end) >= int(elf1end))):
            # Did this manually with relational and boolean operators
            # Alternative clever solution: Use range()s and set()s!
            # (This one is surely faster, but that one is likely cleaner.)
            total_contains += 1
    print('The number of total containments is: ', total_contains)

