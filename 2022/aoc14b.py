from numpy import inf

def read_lines(infile='aoc14_input.txt'):
    with open(infile) as f:
        lines = []
        for line in f:
            endpoints = line.strip().split('->')
            for i in range(len(endpoints) - 1):
                endpoint1 = endpoints[i]
                endpoint2 = endpoints[i+1]
                coords1 = [int(i) for i in endpoint1.strip().split(',')]
                coords2 = [int(i) for i in endpoint2.strip().split(',')]
                lines.append([coords1, coords2])
        return lines

def solve_sand(lines):
    filled_cells = {}
    max_y = -inf
    for e1, e2 in lines:
        x1, y1 = e1
        x2, y2 = e2
        if max(y1, y2) > max_y:
            max_y = max(y1, y2)
        if x1 < x2:
            for x in range(x1, x2+1):
                filled_cells[(x, y1)] = 'R'
        elif x1 > x2:
            for x in range(x2, x1+1):
                filled_cells[(x, y1)] = 'R'
        else:
            if y1 < y2:
                for y in range(y1, y2+1):
                    filled_cells[(x1, y)] = 'R'
            if y1 > y2:
                for y in range(y2, y1+1):
                    filled_cells[(x1, y)] = 'R'
    done = False
    while not done:
        done, filled_cells = drop_sand(filled_cells, max_y+2)
    return filled_cells

def drop_sand(cell_dict, floor_y, sand_x=500, sand_y=0):
    sand_moving = True
    entrance_blocked = False
    while sand_moving:
        #print('Sand at ({}, {})'.format(sand_x, sand_y))
        if sand_y == floor_y-1:
            # sand settles
            cell_dict[(sand_x, sand_y)] = 'S'
            print('Sand settles at {}'.format((sand_x, sand_y)))
            sand_moving = False
            continue
        if (sand_x, sand_y+1) not in cell_dict:
            # Try moving straight down
            sand_y += 1
        elif (sand_x-1, sand_y+1) not in cell_dict:
            # Try moving down-left
            sand_x -= 1
            sand_y += 1
        elif (sand_x+1, sand_y+1) not in cell_dict:
            # Try moving down-right
            sand_x += 1
            sand_y += 1
        else:
            # sand settles
            if sand_x == 500 and sand_y == 0:
                entrance_blocked = True
            cell_dict[(sand_x, sand_y)] = 'S'
            print('Sand settles at {}'.format((sand_x, sand_y)))
            sand_moving = False
    return entrance_blocked, cell_dict

def count_sand(cell_dict):
    count = 0
    for k, v in cell_dict.items():
        if v == 'S':
            count += 1
    return count

if __name__ == '__main__':
    #lines = read_lines('aoc14_sample.txt')
    lines = read_lines()
    cell_dict = solve_sand(lines)
    print('The answer is {}'.format(count_sand(cell_dict)))
