import numpy as np

def read_file(infile='aoc8_input.txt'):
    with open(infile) as f:
        temp_mat = []
        for line in f:
            temp_row = [int(c) for c in line.strip()]
            temp_mat.append(temp_row)
    return np.array(temp_mat)

def check_visibility(g, v):
    size = len(g)
    for i in range(size):
        # i = row
        for j in range(size):
            print(i, j, g[i][j])
            # j = column
            if v[i][j]:
                # Already marked as visible
                continue
            if (i == 0) or (j == 0) or (i == (size-1)) or (j == (size-1)):
                # On the edge, so visible by default
                v[i][j] = 1
                continue
            if g[i][j] > max(g[:i, j]):
                print(g[:i+1, j])
                # Visible from the top (all elements in same column, smaller rows)
                v[i][j] = 1
                continue
            if g[i][j] > max(g[i+1:, j]):
                # Visible from the bottom (all elements in same column, larger rows)
                v[i][j] = 1
                continue
            if g[i][j] > max(g[i, :j]):
                # Visible from the left (all elements in same row, smaller columns)
                v[i][j] = 1
                continue
            if g[i][j] > max(g[i, j+1:]):
                # Visible from the right (all elements in same row, larger columns)
                v[i][j] = 1
                continue
    return g, v

if __name__ == '__main__':
    grid = read_file()
    #grid = read_file('aoc8_sample.txt')
    print(grid)
    visible_grid = np.zeros([len(grid), len(grid)])
    grid, visible_grid = check_visibility(grid, visible_grid)
    print(visible_grid)
    print('The answer is: {}'.format(sum(sum(visible_grid))))

