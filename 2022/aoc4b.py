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
    partial_contains = 0
    for (elf1, elf2) in elf_pairs:
        # I should really have extracted this logic into a function,
        # or functions. Oh well. An exercise for the reader
        (elf1begin, elf1end) = elf1.split('-')
        (elf2begin, elf2end) = elf2.split('-')
        e1b = int(elf1begin)
        e1e = int(elf1end)
        e2b = int(elf2begin)
        e2e = int(elf2end)
        if e1b <= e2b:
            if not e1e < e2b:
                partial_contains += 1
        else:
            if not e2e < e1b:
                partial_contains += 1
    print('The number of total containments is: ', partial_contains)
