from anytree import Node, RenderTree, PreOrderIter

def read_packet_pairs(infile='aoc13_input.txt'):
    with open(infile) as f:
        packet_pairs = []
        while True:
            packet1 = f.readline().strip()
            if not packet1:
                break
            packet2 = f.readline().strip()
            blank = f.readline().strip()
            packet_pairs.append((packet1, packet2))
        return packet_pairs

def make_tree(packet):
    stack = []
    for c in packet:
        if c == '[':
            stack.append('list_begin')
        elif c == ']':
            stack.append('list_end')
        else:
            # c is number or comma
            stack.append(c)
    root = Node('')
    curr_node = root
    num_builder = []
    prev = ''
    while stack:
        temp = stack.pop(0)
        if temp == 'list_begin':
            new_node = Node('list', parent=curr_node)
            curr_node = new_node
        elif temp == 'list_end':
            if num_builder:
                new_node = Node(''.join(num_builder), parent=curr_node)
                num_builder = []
            curr_node = curr_node.parent
        elif temp == ',':
            if prev != 'list_end':
                new_node = Node(''.join(num_builder), parent=curr_node)
                num_builder = []
        else:
            num_builder.append(temp)
        prev = temp
    return root

def compare_trees(t0, t1):
    if not t0.name and not t1.name:
        return compare_trees(t0.children[0], t1.children[0])
    if not t0:
        return True
    if t0.name == 'list':
        # the root of t0 is a parent
        if t1.name == 'list':
            # the root of t1 is also a parent
            for i, _ in enumerate(t0.children):
                if i >= len(t1.children):
                    # t1 has fewer children
                    # by definition, this means that inputs are NOT in the right order
                    return False
                ret_val = compare_trees(t0.children[i], t1.children[i])
                if ret_val is not None:
                    return ret_val
            if len(t1.children) > len(t0.children):
                return True
        else:
            # the root of t1 is a number
            new_list_node = Node('list')
            new_child_node = Node(t1.name, parent=new_list_node)
            return compare_trees(t0, new_list_node)
    else:
        # the root of t0 is a number
        if t1.name == 'list':
            # the root of t1 is a list, though
            new_list_node = Node('list')
            new_child_node = Node(t0.name, parent=new_list_node)
            return compare_trees(new_list_node, t1)
        else:
            # the root of t1 is also a number
            n0 = int(t0.name)
            n1 = int(t1.name)
            if n0 == n1:
                return None
            else:
                return n0 < n1

if __name__ == '__main__':
    #packet_pairs = read_packet_pairs('aoc13_sample.txt')
    packet_pairs = read_packet_pairs()
    answer = 0
    for i, pair in enumerate(packet_pairs, start=1):
        print('Pair {}'.format(i))
        t0 = make_tree(pair[0])
        t1 = make_tree(pair[1])
        # [1:] to account for root node
        right_order = compare_trees(t0, t1)
        print(right_order)
        if right_order:
            answer += i
    print('The answer is {}'.format(answer))

