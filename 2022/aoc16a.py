import numpy as np
import igraph as ig
import itertools
import copy

def read_valves(infile='aoc16_input.txt'):
    with open(infile) as f:
        valves = []
        for line in f:
            tokens = line.strip().split()
            valve_name = tokens[1]
            flow_rate = int(tokens[4].split('=')[1][:-1])
            tunnels = []
            for i in range(9, len(tokens)):
                if i == len(tokens) - 1:
                    tunnels.append(tokens[i])
                else:
                    tunnels.append(tokens[i][:-1])
            valves.append(Valve(valve_name, flow_rate, tunnels))
        return valves

class Valve:
    def __init__(self, name, rate, tunnels):
        self.name = name
        self.rate = rate
        self.tunnels = tunnels

    def __str__(self):
        return 'Valve {} has flow rate {} and tunnels to {}'.format(self.name, self.rate, self.tunnels)

def make_graph_from_valve_list(valves):
    size = len(valves)
    names = []
    flows = []
    tunnels = []
    valve_dict = {}
    for i, v in enumerate(valves):
        valve_dict[v.name] = i
        names.append(v.name)
        flows.append(v.rate)
        for t in v.tunnels:
            tunnels.append([v.name, t])
    edges = [(valve_dict[a], valve_dict[b]) for a, b in tunnels]
    graph = ig.Graph(n=size, edges=edges, directed=False)
    graph.vs['name'] = names
    graph.vs['flow'] = flows
    graph.simplify()
    return graph, valve_dict

def remove_and_reweight(g, valve_dict):
    vertices_to_delete = []
    edges_to_add = []
    for v in g.vs:
        if v['name'] == 'AA':
            # cannot delete AA because it is the start node
            continue
        if v['flow'] == 0:
            connected_valves = []
            for e in v.incident():
                if valve_dict[v['name']] == e.source:
                    connected_valves.append(e.target)
                elif valve_dict[v['name']] == e.target:
                    connected_valves.append(e.source)
            edges_to_add.append(list(itertools.combinations(connected_valves, 2)))
            vertices_to_delete.append(valve_dict[v['name']])
    fixed_edges = []
    for i in edges_to_add:
        fixed_edges.append(i[0])
        print(i[0])
    print(fixed_edges)
    g.add_edges(fixed_edges)
    for e in fixed_edges:
        g[e] = 2
    g.delete_vertices(vertices_to_delete)
    return g.simplify()

if __name__ == '__main__':
    valves = read_valves('aoc16_sample.txt')
    #valves = read_valves
    for v in valves:
        print(v)
    g, valve_dict = make_graph_from_valve_list(valves)
    print(g)
#    g = remove_and_reweight(g, valve_dict)
#    print(g)
