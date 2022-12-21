def read_file(infile='aoc12_input.txt'):
    with open(infile) as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    return lines

paths = []

def depth_first_search(current, graph, can_visit, visited_smalls, small_repeated, path):
    if current.islower():
        # start and end can only be visited once
        if current == 'start' or current == 'end':
            can_visit[current] = False
        elif small_repeated:
            # if there is already a repeated small cave, this cave cannot be revisited
            visited_smalls.append(current)
            can_visit[current] = False
        elif current in visited_smalls:
            # if this cave has already been visited (it is in visited_smalls), it can
            #    be visited exactly once more (this time)
            small_repeated = current
            can_visit[current] = False
        else:
            # This cave has not yet been visited, and it has not been repeated
            #    Just add it to the visited list
            visited_smalls.append(current)

    if current == 'end':
        path.append(current)
        paths.append(path)
        return

    path.append(current)

    for node in graph[current]:
        if can_visit[node]:
            #print('Trying {}->{}'.format(current, node))
            depth_first_search(node, graph, can_visit.copy(), visited_smalls.copy(), small_repeated, path.copy())

def prune_paths():
    temp = []
    for path in paths:
        visited_smalls = {}
        for cave in path:
            if cave.islower() and cave != 'start' and cave != 'end':
                # We're looking at a small cave
                if cave in visited_smalls:
                    visited_smalls[cave] += 1
                else:
                    visited_smalls[cave] = 1

        found_repeat = False
        good_path = True
        for key, value in visited_smalls.items():
            if value > 1:
                if found_repeat:
                    good_path = False
                else:
                    found_repeat = True

        if good_path:
            temp.append(path)

    return temp

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
    visited_smalls = []
    small_repeated = None
    depth_first_search('start', graph, can_visit, visited_smalls, small_repeated, path)

    print(len(paths))

    good_paths = prune_paths()

    print(len(good_paths))
