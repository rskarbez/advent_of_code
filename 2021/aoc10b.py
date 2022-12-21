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

def autocomplete(s):
    stack = []
    for c in s:
        if c in '([{<':
            stack.append(c)
        else:
            stack.pop()
    stack_2 = []
    while stack:
        temp = stack.pop()
        match temp:
            case '(':
                stack_2.append(')')
            case '[':
                stack_2.append(']')
            case '{':
                stack_2.append('}')
            case '<':
                stack_2.append('>')

    return ''.join(stack_2)

def score_fixes(fixes):
    temp_list = []
    for fix in fixes:
        score = 0
        for c in fix:
            score *= 5
            match c:
                case ')':
                    score += 1
                case ']':
                    score += 2
                case '}':
                    score += 3
                case '>':
                    score += 4
        temp_list.append(score)
    return temp_list

if __name__ == '__main__':
    #lines = read_file('aoc10_sample.txt')
    lines = read_file()

    fixes = []
    for line in lines:
        corrupted, bad_char = is_corrupted(line.strip())
        if not corrupted:
            new_chars = autocomplete(line.strip())
            fixes.append(new_chars)

    fix_scores = score_fixes(fixes)
    fix_scores.sort()
    print(fix_scores)

    answer = fix_scores[len(fix_scores) // 2]

    print('The answer is {}'.format(answer))

