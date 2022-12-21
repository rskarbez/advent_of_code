import numpy as np

def read_file(infile='aoc8_input.txt'):
    with open(infile) as f:
        temp_mat = []
        for line in f:
            temp_row = [int(c) for c in line.strip()]
            temp_mat.append(temp_row)
    return np.array(temp_mat)

def compute_scenic_score(g, s):
    size = len(g)
    for i in range(size):
        # i = row
        for j in range(size):
            # j = column
            me = g[i, j]
            print(i, j, me)
            if i == 0 or j == 0 or i == size-1 or j == size-1:
                # On the edge, so one dimension is 0: Scenic score is 0
                s[i, j] = 0
                continue

            north, south, west, east = 0, 0, 0, 0
            for temp in g[:i, j][::-1]:
                north += 1
                if temp >= me:
                    break
            for temp in g[i+1:, j]:
                south += 1
                if temp >= me:
                    break
            for temp in g[i, :j][::-1]:
                west += 1
                if temp >= me:
                    break
            for temp in g[i, j+1:]:
                east += 1
                if temp >= me:
                    break

            s[i, j] = north * south * east * west
    return g, s

if __name__ == '__main__':
    grid = read_file()
    #grid = read_file('aoc8_sample.txt')
    print(grid)
    scenic_score = np.zeros([len(grid), len(grid)])
    grid, scenic_score = compute_scenic_score(grid, scenic_score)
    print(scenic_score)
    print('The answer is {}'.format(scenic_score.max()))

