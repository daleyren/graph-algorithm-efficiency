class Graph:
    def __init__(self):
        '''
        Initializes a completely disconnected graph with no vertices
        '''
        self.adj = {}
        self.n = 0
    
    def randomize_erm_with_random_edge_count(self, n, p):
        '''
        Erdős–Rényi Random Graph Model with n vertices and each edge occuring with probability p.
        
        Every possible edge occurs independently with probability 0 < p < 1. Let N denote all
        possible edges formed within this graph (N = (n choose 2)), and let m be a subset of N.
        As the formation of each edge is an independent and identical draw of a Bernoulli(p), the
        probability that the graph has m edges is (p ^ m) * ((1 - p) ^ (N - m)).
        '''
    
    def randomize_erm_with_nonrandom_edge_count(self, n, M):
        '''
        Erdős–Rényi Random Graph Model with n vertices and exactly M edges.

        Generated as a stochastic process that starts with n vertices and no edges, and with each
        step adds one new edge chosen uniformly from the set of missing edges. There are N choose M
        combinations of M edges within the graph and each edge occurs with probability
        1 /(N choose M). 

        Note: Prove this later - each edge occurs with probability 1 /(N choose M). 
        '''
        pass