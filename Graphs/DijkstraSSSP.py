from DS.PriorityQueue.AdaptablePriorityQueue import AdaptablePriorityQueue

def shortest_path_length(g, src):
    """Compute shortest-path distances from src to reachable vertices of g.

    Graph g can be undirected or directed, but must be weighted such that e.element()
    returns a numeric weight for each edge e.

    Return dictionary mapping each reachable vertex to its distance from src.
    """

    d = {}                                  # d[v] is upper bound from s to v
    cloud = {}                              # map reachable v to its d[v] value
    pq = AdaptablePriorityQueue()           # vertex v will have key d[v]
    pqlocator = {}                          # map from vertex to its pq locator

    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if v in src:
            d[v] = 0
        else:
            d[v] = float('inf')             # syntax for positive infinity
        pqlocator[v] = pq.add(d[v], v)

    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key                      # its correct d[u] value
        del pqlocator[u]                    # u is no longer in pq
        for e in g.incident_edges(u):       # outgoing edges (u,v)
            v = e.opposite(e)
            if v not in cloud:
                # perform relaxation step on edge (u,v)
                wgt = e.element()
                if d[u] + wgt < d[v]:       # better path to v?
                    d[v] = d[u] + wgt       # update the distance
                    pq.update(pqlocator[v], d[v], v)    # update the pq entry

    return cloud                            # only includes reachable vertices
