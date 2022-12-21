def read_file(infile='aoc8_input.txt'):
    with open(infile) as file:
        temp = []
        for line in file:
            temp.append(line.strip())
    return temp

def process_line(line):
    signals, outputs = line.split('|')
    s = signals.strip().split()
    o = outputs.strip().split()
    return (s, o)

def sort_pattern_list(pattern_list):
    temp_dict = {i:'' for i in range(10)}
    for pattern in pattern_list:
        pattern = list(pattern)
        pattern.sort()
        if len(pattern) == 2:
            # 2 segments on ==> digit is 1, put first in list
            temp_dict[0] = pattern
        elif len(pattern) == 3:
            # 3 segments on ==> digit is 7, put second in list
            temp_dict[1] = pattern
        elif len(pattern) == 4:
            # 4 segments on ==> digit is 4, put third in list
            temp_dict[2] = pattern
        elif len(pattern) == 5:
            # 5 segments on ==> digit can be 2, 3, or 5
            #    add to list in appearance order
            if not temp_dict[3]:
                temp_dict[3] = pattern
            elif not temp_dict[4]:
                temp_dict[4] = pattern
            else:
                temp_dict[5] = pattern
        elif len(pattern) == 6:
            # 5 segments on ==> digit can be 0, 6, or 9
            #    add to list in appearance order
            if not temp_dict[6]:
                temp_dict[6] = pattern
            elif not temp_dict[7]:
                temp_dict[7] = pattern
            else:
                temp_dict[8] = pattern
        elif len(pattern) == 7:
            # 6 segments on ==> digit is 8, put last in list
            temp_dict[9] = pattern

    return list(temp_dict.values())

def solve_wires(pattern_list):
    zero = []
    one = pattern_list[0]
    two = []
    three = []
    four = pattern_list[2]
    five = []
    six = []
    seven = pattern_list[1]
    eight = pattern_list[9]
    nine = []

    twothreefive = pattern_list[3:6]
    zerosixnine = pattern_list[6:9]
    all_on = eight

    wires = Wires()
    reverse_wires = Wires()

    # The only difference between 1 and 7 is segment A
    for c in seven:
        if c not in one:
            wires.mapping[c] = 'a'
            reverse_wires.mapping['a'] = c
            break
    # Segment A is solved

    # With knowledge of segment A, it is possible to identify 3
    #    (3 is the only digit with five characters containing both C and F)
    for pattern in twothreefive:
        if one[0] in pattern and one[1] in pattern:
            three = pattern
            break
    # Digit 3 is uniquely identified

    # With knowledge of digit 3, it is possible to identify 9
    #    (9 is the only digit with six characters containing all segments in 3)
    for pattern in zerosixnine:
        nine_found = True
        for c in three:
            if c not in pattern:
                nine_found = False
                break
        if nine_found:
            nine = pattern
            break
    # Digit 9 is uniquely identified

    # With knowledge of digit 9, it is possible to identify segment B
    #    (Segment B is on in digit 9, but off in digit 3)
    for c in nine:
        if c not in three:
            wires.mapping[c] ='b'
            reverse_wires.mapping['b'] = c
            break
    # Segment B is solved

    # With knowledge of digit 9, it is possible to identify segment E
    #    (The only difference between 9 and 8 is segment E)
    for c in eight:
        if c not in nine:
            wires.mapping[c] = 'e'
            reverse_wires.mapping['e'] = c
            break
    # Segment E is solved

    # With knowledge of segment E, it is possible to distinguish 2 and 5
    #    (2 and 5 both have five segments on, but 2 contains E and 5 does not)
    for pattern in twothreefive:
        if pattern == three:
            continue

        if reverse_wires.mapping['e'] in pattern:
            two = pattern
        else:
            five = pattern
    # Digits 2 and 5 are uniquely identified

    # With knowledge of digits 2 and 5, it is possible to distinguish segments C and F
    #    (C is on in 2 and off in 5; F is off in 2 and on in 5)
    #    (C and F are exactly the segments that are on in digit 1)
    if one[0] in two and one[0] not in five:
        wires.mapping[one[0]] = 'c'
        wires.mapping[one[1]] = 'f'
        reverse_wires.mapping['c'] = one[0]
        reverse_wires.mapping['f'] = one[1]
    else:
        wires.mapping[one[0]] = 'f'
        wires.mapping[one[1]] = 'c'
        reverse_wires.mapping['f'] = one[0]
        reverse_wires.mapping['c'] = one[1]
    # Segments C and F are solved

    # With knowledge of segments C and F, it is possible to identify segment D
    #    (D is the only remaining unknown segment in digit 4)
    for c in four:
        if c not in [reverse_wires.mapping['b'], reverse_wires.mapping['c'],
                     reverse_wires.mapping['f']]:
            wires.mapping[c] = 'd'
            reverse_wires.mapping['d'] = c
            break
    # Segment D is solved

    # The only remaining segment is segment G
    for c in all_on:
        if c not in [reverse_wires.mapping['a'], reverse_wires.mapping['b'],
                     reverse_wires.mapping['c'], reverse_wires.mapping['d'],
                     reverse_wires.mapping['e'], reverse_wires.mapping['f']]:
            wires.mapping[c] = 'g'
            reverse_wires.mapping['g'] = c
            break
    # Segment G is solved
    # All segments are solved!

    return wires

def get_digit_pattern(pattern, wires):
    temp = []
    for c in pattern:
        temp.append(wires.mapping[c])
    temp.sort()
    return ''.join(temp)

DIGIT_PATTERNS = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

def get_digit_from_pattern(pattern):
    digit = None

    for i in range(len(DIGIT_PATTERNS)):
        if pattern == DIGIT_PATTERNS[i]:
            digit = str(i)
            break

    return digit

class Wires():
    def __init__(self):
        self.mapping = {c: False for c in 'abcdefg'}

    def __str__(self):
        temp = ''
        for k,v in self.mapping.items():
            temp += '{} -> {}\n'.format(k, v)
        return temp

if __name__ == '__main__':
    #lines = read_file('aoc8_sample.txt')
    lines = read_file()

    signal_patterns = []
    scrambled_outputs = []
    for line in lines:
        s, o = process_line(line)
        signal_patterns.append(s)
        scrambled_outputs.append(o)

    sum = 0

    for i in range(len(signal_patterns)):
        pattern_list = signal_patterns[i]
        sorted_list = sort_pattern_list(pattern_list)
        wires = solve_wires(sorted_list)

        output_list = scrambled_outputs[i]
        temp_str = ''
        for output in output_list:
            fixed_output = get_digit_pattern(output, wires)
            digit = get_digit_from_pattern(fixed_output)
            temp_str += digit

        temp_int = int(temp_str)
        sum += temp_int

    print('The sum of the output values is {}'.format(sum))
