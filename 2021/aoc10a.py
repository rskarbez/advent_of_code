def read_file(infile='aoc10_input.txt'):
    with open(infile) as f:
        return f.readlines()

def is_corrupted(s):
    stack = []
    for i in range(len(s)):
        c = s[i]
        if c in '([{<':
            stack.append(c)
        else:
            curr_open = stack.pop()
            match curr_open:
                case '(':
                    if c != ')':
                        return (True, c)
                case '[':
                    if c != ']':
                        return (True, c)
                case '{':
                    if c != '}':
                        return (True, c)
                case '<':
                    if c != '>':
                        return (True, c)
                case _:
                    print('ERROR')
    return (False, -1)

def score_bad_chars(bad_chars):
    score = 0
    for c in bad_chars:
        match c:
            case ')':
                score += 3
            case ']':
                score += 57
            case '}':
                score += 1197
            case '>':
                score += 25137
    return score

if __name__ == '__main__':
    #lines = read_file('aoc10_sample.txt')
    lines = read_file()

    bad_chars = []
    for line in lines:
        corrupted, bad_char = is_corrupted(line.strip())
        print(corrupted, bad_char)
        if corrupted:
            bad_chars.append(bad_char)

    answer = score_bad_chars(bad_chars)

    print('The answer is {}'.format(answer))

