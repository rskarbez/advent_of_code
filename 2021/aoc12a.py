def read_file(infile='aoc12_input.txt'):
    with open(infile) as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    return lines

paths = []

def depth_first_search(current, graph, can_visit, path):
    if not current.isupper():
        can_visit[current] = False

    if current == 'end':
        path.append(current)
        paths.append(path)
        return True

    path.append(current)

    for node in graph[current]:
        if can_visit[node]:
            depth_first_search(node, graph, can_visit.copy(), path.copy())

if __name__ == '__main__':
    #lines = read_file('aoc12_sample.txt')
    lines = read_file()

    list_of_nodes = []
    graph = {}

    # Build graph
    for line in lines:
        source, dest = line.split('-')
        if source not in list_of_nodes:
            list_of_nodes.append(source)
            graph[source] = []
        if dest not in list_of_nodes:
            list_of_nodes.append(dest)
            graph[dest] = []
        graph[source].append(dest)
        graph[dest].append(source)

    path = []

    can_visit = {node:True for node in list_of_nodes}
    depth_first_search('start', graph, can_visit, path)

    print(len(paths))
