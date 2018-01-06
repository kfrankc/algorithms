# The Bellman-Ford algorithm
# This algorithm computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.
# It is slower than Dijkstra's algorithm for the same problem, but more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers.

# Graph API:
# iter(graph) gives all nodes
# iter(graph[u]) gives neighbours of u
# graph[u][v] gives weight of edge (u, v)

# This is notes taken from this helpful Gist: https://gist.github.com/joninvski/701720

def initialize(graph, source):
    d = {} # destination 
    p = {} # predecessor
    for node in graph:
        d[node] = float('Inf') # We assume the rest of the nodes are far
        p[node] = None
    d[source] = 0 # the source we know how to reach
    return d, p

def relax(node, neighbor, graph, d, p):
    if d[neighbor] > d[node] + graph[node][neighbor]:
        d[neighbor] = d[node] + graph[node][neighbor]
        p[neighbor] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)

    # check for negative weight cycles
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p

def test():
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'd':  2, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
        }

    d, p = bellman_ford(graph, 'a')

    assert d == {
        'a':  0,
        'b': -1,
        'c':  2,
        'd': -2,
        'e':  1
        }

    assert p == {
        'a': None,
        'b': 'a',
        'c': 'b',
        'd': 'e',
        'e': 'b'
        }

if __name__ == '__main__': test()
