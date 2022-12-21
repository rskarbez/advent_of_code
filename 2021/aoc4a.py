class BingoNumber():
    def __init__(self, num):
        self.number = num
        self.hit = False

    def __str__(self):
        if self.hit:
            return '*' + str(self.number) + '*'
        else:
            return str(self.number)

class BingoCard():
    def __init__(self, card):
        self.hit_count = 0
        self.card = card
        self.nums = []
        for row in card:
            for bn in row:
                self.nums.append(bn.number)

    def __str__(self):
        temp = ''
        for row in self.card:
            for col in row:
                temp += '{} '.format(col)
            temp += '\n'
        return temp

    def on_card(self, num):
        return num in self.nums

    def mark(self, num):
        for row in self.card:
            for bn in row:
                if bn.number == num:
                    self.hit_count += 1
                    bn.hit = True
                    return
        return None

    def check(self):
        if self.hit_count < 5:
            return False

        if self.check_rows() or self.check_columns() or self.check_diagonals():
            return True
        else:
            return False

    def check_rows(self):
        for row in self.card:
            temp = True
            for column in row:
                if column.hit == False:
                    temp = False
                    break
            if temp:
                return True
        return False

    def check_columns(self):
        for i in range(5):
            temp = True
            for row in self.card:
                if row[i].hit == False:
                    temp = False
                    break
            if temp:
                return True
        return False

    def check_diagonals(self):
        temp = True
        for i in range(5):
            if self.card[i][i].hit == False:
                temp = False
                break
        if temp:
            return True

        temp = True
        i = 4
        while i >= 0:
            if self.card[i][i].hit == False:
                temp = False
                break
            i -= 1
        if temp:
            return True

        return False

    def score(self):
        temp = 0
        for row in self.card:
            for bn in row:
                if not bn.hit:
                    temp += bn.number
        return temp

def read_bingo(infile='aoc4_input.txt'):
    numbers = []
    cards = []
    with open(infile) as f:
        for i, line in enumerate(f):
            if i == 0:
                temp_list = line.split(',')
                numbers = [int(num) for num in temp_list]
                continue
            if not line.strip():
                # Blank line before bingo card
                temp_card = []
                continue

            bingo_line = [BingoNumber(int(num)) for num in line.split()]
            temp_card.append(bingo_line)

            if len(temp_card) == 5:
                cards.append(BingoCard(temp_card))
        return numbers, cards

if __name__ == '__main__':
    #numbers, cards = read_bingo('aoc4_sample.txt')
    numbers, cards = read_bingo()

    winner = False
    winning_card = None
    winning_number = -1
    for number in numbers:
        print('Calling {}...'.format(number))
        card_index = 0
        for card in cards:
            if card.on_card(number):
                print('{} hits on card {}'.format(number, card_index))
                card.mark(number)

            if card.check():
                print('WE HAVE A WINNER ON CARD ', card_index)
                print(card)
                winner = True
                winning_card = card
                break;
            card_index += 1
        if winner:
            winning_number = number
            break

    print('Sum of unmarked numbers on card: ', winning_card.score())
    print('Last called number: ', winning_number)
    print('THE ANSWER: ', winning_card.score() * winning_number)
