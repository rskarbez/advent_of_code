def read_input(infile='aoc2_input.txt'):
    moves_list = []
    with open(infile) as f:
        for line in f:
            (you, outcome) = line.strip().split()
            moves_list.append((you, outcome))
    return moves_list

def score_move(you, outcome):
    innate_score = 0
    outcome_score = 0
    match outcome:
        case 'X':
            outcome_score = 0
            if (you == 'A'):
                innate_score = 3
            elif (you == 'B'):
                innate_score = 1
            elif (you == 'C'):
                innate_score = 2
            else:
                print('{} is not a valid move'.format(you))
        case 'Y':
            outcome_score = 3
            if (you == 'A'):
                innate_score = 1
            elif (you == 'B'):
                innate_score = 2
            elif (you == 'C'):
                innate_score = 3
            else:
                print('{} is not a valid move'.format(you))
        case 'Z':
            outcome_score = 6
            if (you == 'A'):
                innate_score = 2
            elif (you == 'B'):
                innate_score = 3
            elif (you == 'C'):
                innate_score = 1
            else:
                print('{} is not a valid move'.format(you))
        case _:
            print('{} is not a valid move'.format(outcome))

    print('{} + {} = {}'.format(innate_score, outcome_score, innate_score+outcome_score))
    return innate_score + outcome_score

if __name__ == '__main__':
    #moves_list = read_input('aoc2_sample.txt')
    moves_list = read_input()
    score = 0
    for (you, outcome) in moves_list:
        score += score_move(you, outcome)
    print('Your overall score is: ', score)

