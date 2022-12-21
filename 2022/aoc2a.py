def read_input(infile='aoc2_input.txt'):
    moves_list = []
    with open(infile) as f:
        for line in f:
            (you, me) = line.strip().split()
            moves_list.append((you, me))
    return moves_list

def score_move(you, me):
    innate_score = 0
    outcome_score = 0
    match me:
        case 'X':
            innate_score = 1
            if (you == 'A'):
                outcome_score = 3
            elif (you == 'B'):
                outcome_score = 0
            elif (you == 'C'):
                outcome_score = 6
            else:
                print('{} is not a valid move'.format(you))
        case 'Y':
            innate_score = 2
            if (you == 'A'):
                outcome_score = 6
            elif (you == 'B'):
                outcome_score = 3
            elif (you == 'C'):
                outcome_score = 0
            else:
                print('{} is not a valid move'.format(you))
        case 'Z':
            innate_score = 3
            if (you == 'A'):
                outcome_score = 0
            elif (you == 'B'):
                outcome_score = 6
            elif (you == 'C'):
                outcome_score = 3
            else:
                print('{} is not a valid move'.format(you))
        case _:
            print('{} is not a valid move'.format(me))

    return innate_score + outcome_score

if __name__ == '__main__':
    #moves_list = read_input('aoc2_sample.txt')
    moves_list = read_input()
    score = 0
    for (you, me) in moves_list:
        score += score_move(you, me)
    print('Your overall score is: ', score)

