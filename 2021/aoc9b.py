def read_file(infile='aoc9_input.txt'):
    with open(infile) as f:
        return f.readlines()

def product(in_list):
    temp = 1
    for i in in_list:
        temp *= i
    return temp

def grow_basin(row, col, basin, cells, basins):
    if cells[row][col] == 9:
        return
    if basins[row][col] != -1:
        return

    #print('({}, {}) in basin {}'.format(row, col, basin))
    basins[row][col] = basin

    grow_basin(row-1, col, basin, cells, basins)
    grow_basin(row+1, col, basin, cells, basins)
    grow_basin(row, col+1, basin, cells, basins)
    grow_basin(row, col-1, basin, cells, basins)

def count_basin(basin, basins):
    count = 0
    for row in basins:
        for col in row:
            if col == basin:
                count += 1
    return count

if __name__ == '__main__':
    #lines = read_file('aoc9_sample.txt')
    lines = read_file()
    rows = len(lines)
    cols = len(lines[0].strip())

    cells = [[9 for i in range(cols+2)] for j in range(rows+2)]
    for i in range(rows):
        line = lines[i].strip()
        for j in range(cols):
            num = int(line[j])
            cells[i+1][j+1] = num

    for row in cells:
        print(row)

    low_points = []
    for i in range(rows):
        for j in range(cols):
            curr_cell = cells[i+1][j+1]
            north = cells[i][j+1]
            south = cells[i+2][j+1]
            east = cells[i+1][j+2]
            west = cells[i+1][j]

            if curr_cell < min([north, south, east, west]):
                low_points.append((i+1, j+1))
                print('Low point found; risk level =', curr_cell+1)

    print(low_points)

    basins = [[-1 for i in range(cols+2)] for j in range(rows+2)]
    for i in range(len(low_points)):
        grow_basin(low_points[i][0], low_points[i][1], i, cells, basins)

    for row in basins:
        print(row)

    basin_sizes = []
    for i in range(len(low_points)):
        basin_sizes.append(count_basin(i, basins))

    basin_sizes.sort(reverse=True)
    print(basin_sizes)

    answer = product(basin_sizes[:3])

    print('The answer is {}'.format(answer))
