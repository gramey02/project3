import numpy as np
import heapq
from typing import Union

class Graph:
    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """ Unlike project 2, this Graph class takes an adjacency matrix as input. `adjacency_mat` 
        can either be a 2D numpy array of floats or the path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph
        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def construct_mst(self):
        """ Given `self.adj_mat`, the adjacency matrix of a connected undirected graph, implement Prim's 
        algorithm to construct an adjacency matrix encoding the minimum spanning tree of `self.adj_mat`. 
            
        `self.adj_mat` is a 2D numpy array of floats. 
        Note that because we assume our input graph is undirected, `self.adj_mat` is symmetric. 
        Row i and column j represents the edge weight between vertex i and vertex j. An edge weight of zero indicates that no edge exists. 
        
        TODO: 
            This function does not return anything. Instead, store the adjacency matrix 
        representation of the minimum spanning tree of `self.adj_mat` in `self.mst`.
        We highly encourage the use of priority queues in your implementation. See the heapq
        module, particularly the `heapify`, `heappop`, and `heappush` functions.
        """
        vertices = list(range(0,len(self.adj_mat))) #vertex labels
        visited_vertices = [vertices[0]] #set the first node in the list as the start node
        
        edges = []
        edges = [(weight, start_node, end_node)]
        
        #get outgoing edges from all visited nodes and push them onto heap
        #make sure to store both the edge weight and the destination node
        for i in range(0,len(visited_vertices)):
            if(self.adj_mat[visited_vertices[0]][i] != 0):
                d[self.adj_mat[visited_vertices[0]][i]] = i #edge weight is the key, destination node is the value
        
        #now convert dictionary to a list of tuples and heapify it, then convert it back into a dictionary
        d_list = list(d.items())
        edges = heapq.heapify(d_list)
        heapified_edges = dict(edges)
        
        #while not all vertices have been visited...
        while len(visited_vertices)<len(vertices):
            heapq.heappop(heapified_edges) #pop the lowest weight edge from the queue along with its destination node
        
        
        
        
        
        #workshop this later
        #create a min heap using the heapify function
        heap=[]
        heapq.heapify(heap)
        for i in range(0,len(visited_vertices)):
            if(self.adj_mat[visited_vertices[0]][i] != 0):
                heapq.push((heap,self.adj_mat[visited_vertices[0]][i], i))
        
        while len(visited_vertices)<len(vertices):
            
        
        
        #edge_weights = {} #initialize a dictionary for the edge weights
        #start = 
        
        
        self.mst = 'TODO'
        
        
        #start off by storing the weight of the minimum edge of each node in a dictionary ()
