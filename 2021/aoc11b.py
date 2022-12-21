def read_file(infile='aoc11_input.txt'):
    with open(infile) as f:
        lines = []
        for line in f:
            lines.append(line.strip())
        return lines

def make_grid(lines):
    grid = []
    for line in lines:
        row = []
        for c in line:
            row.append(int(c))
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        temp = ''
        for i in row:
            if i != 0:
                temp += '{:^3}'.format(str(i))
            else:
                temp += '*0*'
        print(temp)

def tick(grid):
    flash_list = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            increment_cell(grid, flash_list, row, col)
    for row, col in flash_list:
        grid[row][col] = 0
    return len(flash_list)

def increment_cell(grid, flash_list, row, col):
    if (row, col) in flash_list:
        return

    grid[row][col] += 1

    if grid[row][col] >= 10:
        flash_list.append((row, col))
        increment_neighbors(grid, flash_list, row, col)

def increment_neighbors(grid, flash_list, row, col):
    if row == 0:
        start_row = row
    else:
        start_row = row - 1

    if row == (len(grid)-1):
        end_row = row
    else:
        end_row = row + 1

    if col == 0:
        start_col = col
    else:
        start_col = col - 1

    if col == (len(grid[0])-1):
        end_col = col
    else:
        end_col = col + 1

    for i in range(start_row, end_row+1):
        for j in range(start_col, end_col+1):
            increment_cell(grid, flash_list, i, j)

if __name__ == '__main__':
    #lines = read_file('aoc11_sample.txt')
    lines = read_file()

    octopuses = make_grid(lines)
    print_grid(octopuses)

    step = 0
    while True:
        flash_count = tick(octopuses)
        print('    {} flashes observed!'.format(flash_count))
        step += 1
        if flash_count == 100:
            break

    print('The answer is', step)

