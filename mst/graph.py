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
        vertices = list(range(0,len(self.adj_mat))) #vertex labels. Length of this is the number of vertices
        visited_vertices = [vertices[0]] #set the first node in the list as the start node
        
        edges = {} #format will be {weight: [start_node, destination_node]}
        
        #get outgoing edges from all visited nodes and add them to the ditionary
        #make sure to store both the edge weight and the destination node
        #maybe change range here to len(self.adj_mat)
        for i in range(0,len(visited_vertices)):
            if(self.adj_mat[visited_vertices[0]][i] != 0):
                edges[self.adj_mat[visited_vertices[0]][i]] = [vertices[0], i]
                
        #convert dictionary into a list
        edges = list(edges.items())
        #heapify the dictionary (really a list now) based on edge weights
        heapq.heapify(edges)
        
        mst_edges = [] #for storing final mst edges and start/destination nodes
        #while not all vertices have been visited...
        while len(visited_vertices)<len(vertices):
            low_wt = heapq.heappop(edges) #pop the lowest weight edge from the queue along with its start and destination nodes
            #if the destination node of the current lowest weight edge has not been visited...
            if low_wt[1][1] not in visited_vertices:
                mst_edges.append(low_wt) #append the lowest weight edge and corresponding nodes to mst_edges
                visited_vertices.append(low_wt[1][1]) #append the destination node to the visited_vertices list
                for i in range(0,length(self.adj_mat)):
                    if(self.adj_mat[low_wt[]]) #this is the line you were on-------------------------------------------------------
                    edges.append(())#add all outgoing edges from the destination node to the priority queue
            
        

        
        #self.mst should be another adjacency matrix
        #duplicate the original adjacency matrix and fill in the cells with new values
        final_mst = self.adj_mat
        self.mst = 'TODO'
