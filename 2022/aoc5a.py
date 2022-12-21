import re

class Tower:
    def __init__(self, num):
        self.num = num
        self.stack = []

    def __str__(self):
        return 'Tower {}: {}'.format(self.num, str([c for c in self.stack]))

    def push(self, crate):
        self.stack.append(crate)

    def pop(self):
        return self.stack.pop()

    def reverse(self):
        return self.stack[::-1]

    def last_item(self):
        return self.stack[-1]

def read_file(infile='aoc5_input.txt'):
    reading_towers = True
    towers = []
    moves = []
    with open(infile) as f:
        for line in f:
            if reading_towers:
                towers.append(line)
            else:
                moves.append(line)
            if not line.strip():
                _ = towers.pop()
                reading_towers = False
    return (towers, moves)

def init_towers(towers_text):
    max_height = len(towers_text) - 1
    num_towers = int(towers_text[-1].strip().split()[-1])
    parsed_lines = []
    print('Max height: {}'.format(max_height))
    print('Num towers: {}'.format(num_towers))
    towers = [Tower(i) for i in range(num_towers)]
    for t in towers:
        print(t)
    for line in towers_text[:-1]:
        line_items = [line[i:i+4] for i in range(0, len(line), 4)]
        parsed_lines.append(line_items)
    print(parsed_lines)
    for line in parsed_lines:
        tower = 0
        for item in line:
            if item[0] == ' ':
                tower += 1
                continue
            towers[tower].push(item[1])
            tower += 1
            if item[3] == '\n':
                break
    return_towers = [Tower(i) for i in range(num_towers)]
    for t in towers:
        return_towers[t.num].stack = t.reverse()
    return return_towers

def init_moves(moves_text):
    moves = []
    for line in moves_text:
        # Removes all letters from line
        temp_line = re.sub('[a-zA-Z]', '', line)
        print(temp_line)
        count, from_tower, to_tower = temp_line.split()
        moves.append((int(count), int(from_tower), int(to_tower)))
    print(moves)
    return moves

def make_moves(towers, moves):
    for move in moves:
        print(move)
        count, from_tower, to_tower = move
        for _ in range(count):
            towers[to_tower-1].push(towers[from_tower-1].pop())
            for t in towers:
                print(t)
    return towers


if __name__ == '__main__':
    towers_text, moves_text = read_file()
    #towers_text, moves_text = read_file('aoc5_sample.txt')
    print(len(towers_text))
    print(len(moves_text))
    towers = init_towers(towers_text)
    moves = init_moves(moves_text)
    for t in towers:
        print(t)
    final_towers = make_moves(towers, moves)
    for t in final_towers:
        print(t)
    out_str = ''.join([t.last_item() for t in final_towers])
    print('Top items of each stack: {}'.format(out_str))


