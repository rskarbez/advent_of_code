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


def make_moves(moves, visited, start):
    head_x, head_y = (0, 0)
    tail_x, tail_y = (0, 0)
    visited = visit_coord(tail_x, tail_y, visited, start)
    for direction, distance in moves:
        print(direction, distance)
        for i in range(distance):
            match direction:
                case 'U':
                    head_y += 1
                    if not is_adjacent((head_x, head_y), (tail_x, tail_y)):
                        # tail must move
                        if head_x < tail_x:
                            # move UL
                            tail_x -= 1
                            tail_y += 1
                        elif head_x > tail_x:
                            # move UR
                            tail_x += 1
                            tail_y += 1
                        else:
                            # move U
                            tail_y += 1
                case 'D':
                    head_y -= 1
                    if not is_adjacent((head_x, head_y), (tail_x, tail_y)):
                        # tail must move
                        if head_x < tail_x:
                            # move DL
                            tail_x -= 1
                            tail_y -= 1
                        elif head_x > tail_x:
                            # move DR
                            tail_x += 1
                            tail_y -= 1
                        else:
                            # move D
                            tail_y -= 1
                case 'L':
                    head_x -= 1
                    if not is_adjacent((head_x, head_y), (tail_x, tail_y)):
                        # tail must move
                        if head_y < tail_y:
                            # move DL
                            tail_x -= 1
                            tail_y -= 1
                        elif head_y > tail_y:
                            # move UL
                            tail_x -= 1
                            tail_y += 1
                        else:
                            # move L
                            tail_x -= 1
                case 'R':
                    head_x += 1
                    if not is_adjacent((head_x, head_y), (tail_x, tail_y)):
                        # tail must move
                        if head_y < tail_y:
                            # move DR
                            tail_x += 1
                            tail_y -= 1
                        elif head_y > tail_y:
                            # move UR
                            tail_x += 1
                            tail_y += 1
                        else:
                            # move R
                            tail_x += 1
            visited = visit_coord(tail_x, tail_y, visited, start)
        print_head_and_tail((head_x, head_y), (tail_x, tail_y))
    return visited

if __name__ == '__main__':
    #moves = read_input('aoc9_sample.txt')
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
