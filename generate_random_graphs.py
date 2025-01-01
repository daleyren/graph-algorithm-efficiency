import random
import math
    
def randomize_erm_with_random_edge_count_undirected(n: int, p: int) -> dict:
    '''
    Erdős–Rényi Random Graph Model with n vertices and each edge occuring with probability p.
    
    Every possible edge occurs independently with probability 0 < p < 1. Let N denote all
    possible edges formed within this graph (N = (n choose 2)), and let m be a subset of N.
    As the formation of each edge is an independent and identical draw of a Bernoulli(p), the
    probability that the graph has m edges is (p ^ m) * ((1 - p) ^ (N - m)). No self-loop edges
    considered (i.e. (v_i, v_i) is never an element of the edges set)
    '''
    if p < 0 or p > 1:
        raise Exception("Probability p must lie inbetween 0 and 1...")

    adj = {}
    for node1 in range(n):
        if node1 not in adj:
            adj[node1] = []

        for node2 in range(node1 + 1, n):
            if node2 not in adj:
                adj[node2] = []

            success = random.random() <= p # random.random() ~ Uniform[0,1)

            if success:
                adj[node1].append(node2)
                adj[node2].append(node1)
    return adj


def randomize_erm_with_nonrandom_edge_count_undirected(n: int, M: int) -> dict:
    '''
    Erdős–Rényi Random Graph Model with n vertices and exactly M edges.

    Generated as a stochastic process that starts with n vertices and no edges, and with each
    step adds one new edge chosen uniformly from the set of missing edges. There are N choose M
    combinations of M edges within the graph and each edge occurs with probability
    1 /(N choose M). 

    Note: Prove this later - each edge occurs with probability 1 /(N choose M). 
    '''
    N = math.comb(n, 2)
    if M > N:
        raise Exception("Can't have more edges than possible: M exceeds n choose 2. dummy :P")

    adj = {}
    unselected_edges = []
    for node1 in range(n):
        adj[node1] = []
        for node2 in range(node1 + 1, n):
            unselected_edges.append((node1, node2))
    
    # print(len(all_possible_edges))
    random.shuffle(unselected_edges)

    # Iterative uniform selection from remaining edges
    for _ in range(M):
        a, b = unselected_edges.pop()
        adj[a].append(b)
        adj[b].append(a)
    
    return adj