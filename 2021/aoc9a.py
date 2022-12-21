from math import inf

def read_file(infile='aoc9_input.txt'):
    with open(infile) as f:
        return f.readlines()

class Cell():
    def __init__(self, value, north, south, east, west):
        self.value = value
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.low = None

    def __str__(self):
        return self.value

    def is_low(self):
        if self.low:
            return self.low
        v = self.value
        if v < self.north.value and v < self.south.value and v < self.east.value and v < self.west.value:
            self.low = True
            return True
        else:
            self.low = False
            return False

if __name__ == '__main__':
    #lines = read_file('aoc9_sample.txt')
    lines = read_file()
    rows = len(lines)
    cols = len(lines[0].strip())

    cells = [[inf for i in range(cols+2)] for j in range(rows+2)]
    for i in range(rows):
        line = lines[i].strip()
        for j in range(cols):
            num = int(line[j])
            cells[i+1][j+1] = num

    for row in cells:
        print(row)

    count = 0
    answer = 0
    for i in range(rows):
        for j in range(cols):
            curr_cell = cells[i+1][j+1]
            north = cells[i][j+1]
            south = cells[i+2][j+1]
            east = cells[i+1][j+2]
            west = cells[i+1][j]

            if curr_cell < min([north, south, east, west]):
                print('Low point found; risk level =', curr_cell+1)
                answer += curr_cell+1
                count += 1

    print('Low points found:', count)
    print('The answer is {}'.format(answer))
