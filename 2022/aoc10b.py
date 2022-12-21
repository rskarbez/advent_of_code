def read_file(infile='aoc10_input.txt'):
    with open(infile) as f:
        commands = []
        for line in f:
            commands.append(line.strip())
        return commands

def fill_queue(commands):
    q = []
    for cmd in commands:
        if cmd == 'noop':
            q.append(0)
        else:
            _, value = cmd.split()
            q.append(0)
            q.append(int(value))
    return q

def run_queue(q):
    register = 1
    screen = []
    line = []
    for i, value in enumerate(q):
        pixel = i % 40
        if pixel == 0:
            screen.append(line)
            line = []
        if register in [pixel-1, pixel, pixel+1]:
            line.append('#')
        else:
            line.append('.')
        register += value
    screen.append(line)
    for line in screen:
        print(''.join(line))

if __name__ == '__main__':
    #commands = read_file('aoc10_sample.txt')
    commands = read_file()
    print(len(commands))
    q = fill_queue(commands)
    run_queue(q)
