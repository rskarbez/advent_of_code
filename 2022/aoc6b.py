from collections import deque

def read_file(infile='aoc6_input.txt'):
    buffers = []
    with open(infile) as f:
        for line in f:
            buffers.append(line.strip())
    return buffers

def is_marker(d):
    while d:
        f = d.popleft()
        if d.count(f):
            return False
    return True

def find_markers(buffer):
    i = 0
    markers = []
    while i < len(buffer):
        if is_marker(deque(buffer[i:i+14], 14)):
            markers.append(i+14)
        i += 1
    return markers


if __name__ == '__main__':
    #buffers = read_file('aoc6_sample.txt')
    buffers = read_file()
    print(buffers)
    print(len(buffers))
    for b in buffers:
        markers = find_markers(b)
        print('Location of first marker is {}'.format(markers[0]))
