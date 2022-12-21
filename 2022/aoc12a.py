import numpy as np
import igraph as ig

def read_map(infile='aoc12_input.txt'):
    start = None
    end = None
    ret_map = None
    temp = []
    with open(infile) as f:
        for row, line in enumerate(f):
            line = line.strip()
            temp_row = []
            for col, c in enumerate(line):
                if c == 'S':
                    start = (row, col)
                    temp_row.append(ord('a') - 97)
                elif c == 'E':
                    end = (row, col)
                    temp_row.append(ord('z') - 97)
                else:
                    temp_row.append(ord(c) - 97)
            temp.append(temp_row)
        return np.array(temp), start, end

class Cell:
    def __init__(self, row, col, my_val, n_val, s_val, e_val, w_val):
        self.row = row
        self.col = col
        self.value = my_val
        self.fscore = np.inf
        self.n = (my_val + 1) >= n_val
        self.s = (my_val + 1) >= s_val
        self.e = (my_val + 1) >= e_val
        self.w = (my_val + 1) >= w_val
        self.exits = int(self.n) + int(self.s) + int(self.e) + int(self.w)

    def __str__(self):
        return '{} ({}, {})'.format(self.value, self.row, self.col)

    def valid_steps(self):
        temp = []
        if self.n:
            temp.append('N')
        if self.s:
            temp.append('S')
        if self.e:
            temp.append('E')
        if self.w:
            temp.append('W')
        return temp

    def neighbor(self, direction):
        temp_cell = None
        match direction.lower():
            case 'n':
                if self.n:
                    temp_cell = (self.row-1, self.col)
            case 's':
                if self.s:
                    temp_cell = (self.row+1, self.col)
            case 'e':
                if self.e:
                    temp_cell = (self.row, self.col+1)
            case 'w':
                if self.w:
                    temp_cell = (self.row, self.col-1)
        return temp_cell

class Grid:
    def __init__(self, array):
        self.array = array
        self.init_cells()

    def init_cells(self):
        self.cells = []
        for i, row in enumerate(self.array):
            cell_row = []
            for j, val in enumerate(row):
                if i == 0:
                    # Top row
                    n = np.inf
                else:
                    n = self.array[i-1, j]
                if i == len(self.array) - 1:
                    s = np.inf
                else:
                    s = self.array[i+1, j]
                if j == 0:
                    w = np.inf
                else:
                    w = self.array[i, j-1]
                if j == len(row) - 1:
                    e = np.inf
                else:
                    e = self.array[i, j+1]
                cell_row.append(Cell(i, j, val, n, s, e, w))
            self.cells.append(cell_row)

    def get_cell(self, coords):
        return self.cells[coords[0]][coords[1]]

    def print_exits(self):
        for row in self.cells:
            temp_row = [str(cell.exits) for cell in row]
            print(''.join(temp_row))

def vertex_number(i, j, width, height):
    return (i * width) + j

def make_graph(grid, width, height):
    size = width * height
    graph = ig.Graph(n=size, directed=True)
    for i in range(height):
        for j in range(width):
            cell = grid.get_cell((i, j))
            curr_vertex = vertex_number(i, j, width, height)
            for d in cell.valid_steps():
                match d:
                    case 'N':
                        neighbor = vertex_number(i-1, j, width, height)
                        graph.add_edge(curr_vertex, neighbor)
                    case 'S':
                        neighbor = vertex_number(i+1, j, width, height)
                        graph.add_edge(curr_vertex, neighbor)
                    case 'E':
                        neighbor = vertex_number(i, j+1, width, height)
                        graph.add_edge(curr_vertex, neighbor)
                    case 'W':
                        neighbor = vertex_number(i, j-1, width, height)
                        graph.add_edge(curr_vertex, neighbor)
    print(graph)
    return graph

if __name__ == '__main__':
    #array, start, end = read_map('aoc12_sample.txt')
    array, start, end = read_map()
    print(array)
    print(start)
    print(end)
    height = len(array)
    width = len(array[0])
    grid = Grid(array)
    g = make_graph(grid, width, height)
    start_vertex = vertex_number(start[0], start[1], width, height)
    end_vertex = vertex_number(end[0], end[1], width, height)
    path = g.get_shortest_paths(start_vertex, to=end_vertex)
    print('Path length: {}'.format(len(path[0]) - 1))
    print(path)
