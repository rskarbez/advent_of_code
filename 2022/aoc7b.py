from anytree import Node, RenderTree, PostOrderIter

def read_lines(infile='aoc7_input.txt'):
    lines = []
    with open(infile) as f:
        for line in f:
            lines.append(line.strip())
    return lines

def build_tree(lines):
    root = Node('', parent=None)
    curr_node = root
    for line in lines:
        print(line)
        if line[0] == '$':
            command = line[2:]
            # line is a command (input)
            if command[0:2] == 'cd':
                command, param = command.split()
                if param == '/':
                    curr_node = root
                elif param == '..':
                    curr_node = curr_node.parent
                else:
                    for temp_node in curr_node.children:
                        if temp_node.name == param:
                            curr_node = temp_node
            elif line[2:4] == 'ls':
                pass
            else:
                print('illegal command on line "{}"'.format(line))
        else:
            # line is information (output)
            tokens = line.split()
            if tokens[0] == 'dir':
                # dir name
                temp_node = Node(tokens[1], parent=curr_node, size=-1)
            else:
                # size name
                temp_node = Node(tokens[1], parent=curr_node, size=int(tokens[0]))
    return root

def compute_size(tree):
    if tree.is_leaf:
        return tree.size

    tree.size = 0
    for node in tree.children:
        tree.size += compute_size(node)

    return tree.size

def biggest_folder(tree):
    folder = ''
    max_size = -1
    for node in tree.children:
        if not node.is_leaf:
            if node.size > max_size:
                folder = node.name
                max_size = node.size
    return folder, max_size

def compute_answer(tree):
    free_space = 70000000 - tree.size
    needed_space = 30000000 - free_space
    print('Need to free up a folder with size >= {}'.format(needed_space))
    options = []
    for node in PostOrderIter(tree):
        if not node.is_leaf and node is not tree and node.size >= needed_space:
            options.append(node.size)
    return min(options)


if __name__ == '__main__':
    #lines = read_lines('aoc7_sample.txt')
    lines = read_lines()
    print(lines)
    print(len(lines))
    tree = build_tree(lines)
    print(RenderTree(tree))
    total_size = compute_size(tree)
    print(RenderTree(tree))
    folder, folder_size = biggest_folder(tree)
    print('The largest folder is {} (size={})'.format(folder, folder_size))
    print('The answer is {}'.format(compute_answer(tree)))

