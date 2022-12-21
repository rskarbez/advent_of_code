def read_commands(infile='aoc2_input.txt'):
    with open(infile) as f:
        commands = []
        for line in f:
            cmd, val = line.strip().split()
            commands.append((cmd, int(val)))
        return commands

if __name__ == '__main__':
    #commands = read_commands('aoc2_sample.txt')
    commands = read_commands()
    sub_x = 0
    sub_y = 0
    for cmd, val in commands:
        if cmd == 'forward':
            sub_x += val
        elif cmd == 'down':
            sub_y += val
        elif cmd == 'up':
            sub_y -= val
    print('The answer is {}.'.format(sub_x * sub_y))
