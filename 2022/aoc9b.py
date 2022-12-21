import numpy as np

def read_input(infile='aoc9_input.txt'):
    with open(infile) as f:
        moves = []
        for line in f:
            direction, distance = line.strip().split()
            moves.append((direction, int(distance)))
        return moves

def compute_limits(moves):
    x_coords = [0]
    y_coords = [0]
    for i, move in enumerate(moves):
        direction, distance = move
        match direction:
            case 'U':
                x_coords.append(x_coords[i])
                y_coords.append(y_coords[i] + distance)
            case 'D':
                x_coords.append(x_coords[i])
                y_coords.append(y_coords[i] - distance)
            case 'L':
                x_coords.append(x_coords[i] - distance)
                y_coords.append(y_coords[i])
            case 'R':
                x_coords.append(x_coords[i] + distance)
                y_coords.append(y_coords[i])
    return min(x_coords), max(x_coords), min(y_coords), max(y_coords)

def is_adjacent(head, tail):
    return (abs(head[0] - tail[0]) <= 1) and (abs(head[1] - tail[1]) <= 1)

def print_head_and_tail(head, tail):
    print('Head coords: ({}, {})'.format(head[0], head[1]))
    print('Tail coords: ({}, {})'.format(tail[0], tail[1]))

def visit_coord(x, y, visited, start):
    visited[start[0] + x][start[1] + y] = 1
    return visited

def move_knot(lead, follow):
    if is_adjacent(lead, follow):
        return follow
    x_diff = lead[0] - follow[0]
    y_diff = lead[1] - follow[1]
    if x_diff == 0:
        # Same column
        if y_diff < 0:
            follow[1] -= 1
        else:
            follow[1] += 1
    elif y_diff == 0:
        # Same row
        if x_diff < 0:
            follow[0] -= 1
        else:
            follow[0] += 1
    else:
        # Diagonal
        if x_diff < 0:
            follow[0] -= 1
        else:
            follow[0] += 1
        if y_diff < 0:
            follow[1] -= 1
        else:
            follow[1] += 1
    return follow


def make_moves(moves, visited, start):
    head = [0, 0]
    knots = [[0, 0] for _ in range(9)]
    visited = visit_coord(0, 0, visited, start)
    for direction, distance in moves:
        print(direction, distance)
        for i in range(distance):
            match direction:
                case 'U':
                    head[1] += 1
                case 'D':
                    head[1] -= 1
                case 'L':
                    head[0] -= 1
                case 'R':
                    head[0] += 1
            prev_knot = head
            for knot in knots:
                knot = move_knot(prev_knot, knot)
                prev_knot = knot
            visited = visit_coord(knots[-1][0], knots[-1][1], visited, start)
        print_head_and_tail(head, knots[-1])
    return visited

if __name__ == '__main__':
    #moves = read_input('aoc9_sample2.txt')
    moves = read_input()
    x_min, x_max, y_min, y_max = compute_limits(moves)
    print(x_min, x_max, y_min, y_max)
    visited = np.zeros([(x_max - x_min) + 1, (y_max - y_min) + 1])
    print(visited)
    start = (-x_min, -y_min)
    print(start)
    visited = make_moves(moves, visited, start)
    print(visited)
    print('The answer is {}'.format(sum(sum(visited))))
