def read_file(infile='aoc13_input.txt'):
    coordinate_lines = []
    fold_lines = []
    with open(infile) as f:
        coordinates = True
        for line in f:
            if not line.strip():
                coordinates = False
                continue
            if coordinates:
                coordinate_lines.append(line.strip())
            if not coordinates:
                fold_lines.append(line.strip())
    return (coordinate_lines, fold_lines)

def make_grid(coordinates, max_x, max_y):
    grid = [[False for col in range(max_x+1)] for row in range(max_y+1)]
    for x, y in coordinates:
        grid[y][x] = True
    return grid

def print_grid(grid):
    for row in grid:
        row_str = ''
        for col in row:
            if col:
                row_str += ' # '
            else:
                row_str += ' . '
        print(row_str)

def make_folds(grid, folds, max_x, max_y):
    if not folds:
        return grid

    axis, value = folds.pop(0)

    new_grid = []
    new_max_x = max_x
    new_max_y = max_y

    if axis == 'x':
        new_max_x = value
        new_grid = [[False for col in range(new_max_x+1)] for row in range(max_y+1)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                new_col = -1
                if j <= new_max_x:
                    new_col = j
                else:
                    new_col = abs(j - (2 * new_max_x))
                if grid[i][j]:
                    new_grid[i][new_col] = True
    elif axis == 'y':
        new_max_y = value
        new_grid = [[False for col in range(max_x+1)] for row in range(new_max_y+1)]

        for i in range(len(grid)):
            new_row = -1
            if i <= new_max_y:
                new_row = i
            else:
                new_row = abs(i - (2 * new_max_y))
            for j in range(len(grid[i])):
                if grid[i][j]:
                    new_grid[new_row][j] = True

    return make_folds(new_grid, folds, new_max_x, new_max_y)

if __name__ == '__main__':
    #coordinate_lines, fold_lines = read_file('aoc13_sample.txt')
    coordinate_lines, fold_lines  = read_file()

    coordinates = []
    max_x = -1
    max_y = -1
    for line in coordinate_lines:
        x,y = line.split(',')
        x = int(x)
        y = int(y)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        coordinates.append((x, y))

    folds = []
    for line in fold_lines:
        temp = line.removeprefix('fold along')
        axis, value = temp.split('=')
        folds.append((axis.strip(), int(value)))

    grid = make_grid(coordinates, max_x, max_y)

    result_grid = make_folds(grid, folds, max_x, max_y)

    print_grid(result_grid)
