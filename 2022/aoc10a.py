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
    answer = 0
    for i, value in enumerate(q, 1):
        if i % 40 == 20:
            print('During cycle {}, register value is {}'.format(i, register))
            answer += (i * register)
        register += value
    return answer

if __name__ == '__main__':
    #commands = read_file('aoc10_sample.txt')
    commands = read_file()
    print(len(commands))
    q = fill_queue(commands)
    answer = run_queue(q)
    print('The answer is {}'.format(answer))
