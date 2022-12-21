class Grid():
    def __init__(self, max_x=1000, max_y=1000):
        self.max_x = max_x
        self.max_y = max_y
        self.grid = []
        for i in range(max_x):
            temp_row = []
            for j in range(max_y):
                temp_row.append(0)
            self.grid.append(temp_row)

    def __str__(self):
        return '{} by {} Grid() object'.format(self.max_x, self.max_y)

    def draw_line(self, seg):
        # seg is a vertical line
        if seg.x1 == seg.x2:
            start_y = min(seg.y1, seg.y2)
            end_y = max(seg.y1, seg.y2)
            for y in range(start_y, end_y+1):
                self.grid[seg.x1][y] += 1
        # seg is a horizontal line
        elif seg.y1 == seg.y2:
            start_x = min(seg.x1, seg.x2)
            end_x = max(seg.x1, seg.x2)
            for x in range(start_x, end_x+1):
                self.grid[x][seg.y1] += 1
        # seg is a 45-degree diagonal line
        else:
            pass

    def count_intersections(self):
        count = 0
        for i in range(self.max_x):
            for j in range(self.max_y):
                if self.grid[i][j] > 1:
                    count += 1
        return count

class LineSegment():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return '({}, {}) -> ({}, {})'.format(self.x1, self.y1, self.x2, self.y2)

    def __repr__(self):
        return self.__str__()

def read_segments(infile='aoc5_input.txt'):
    with open(infile) as f:
        segments = []
        for line in f:
            l1, l2 = line.split('->')
            x1, y1 = l1.split(',')
            x2, y2 = l2.split(',')
            segments.append(LineSegment(int(x1), int(y1), int(x2), int(y2)))
        return segments

if __name__ == '__main__':
    #segments = read_segments('aoc5_sample.txt')
    segments = read_segments()
    grid = Grid()
    for seg in segments:
        grid.draw_line(seg)
    print("The number of intersections is ", grid.count_intersections())

