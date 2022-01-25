# write tests for bfs
import pytest
import numpy as np
from mst import Graph
from sklearn.metrics import pairwise_distances
from search import Graph


def check_mst(adj_mat: np.ndarray, 
              mst: np.ndarray, 
              expected_weight: int, 
              allowed_error: float = 0.0001):
    """ Helper function to check the correctness of the adjacency matrix encoding an MST.
        Note that because the MST of a graph is not guaranteed to be unique, we cannot 
        simply check for equality against a known MST of a graph. 

        Arguments:
            adj_mat: Adjacency matrix of full graph
            mst: Adjacency matrix of proposed minimum spanning tree
            expected_weight: weight of the minimum spanning tree of the full graph
            allowed_error: Allowed difference between proposed MST weight and `expected_weight`

        TODO: 
            Add additional assertions to ensure the correctness of your MST implementation
        For example, how many edges should a minimum spanning tree have? Are minimum spanning trees
        always connected? What else can you think of?
    """
    def approx_equal(a, b):
        return abs(a - b) < allowed_error

    total = 0
    mst_edges = 0
    for i in range(mst.shape[0]):
        for j in range(i+1):
            total += mst[i, j]
            if mst[i,j] != 0:
                mst_edges +=1 #increase the number of edges in the mst by 1 if there is a nonzero value in the mst array
                
    #compare total and expected weights. If less than allowed_error, then test will pass
    assert approx_equal(total, expected_weight), 'Proposed MST has incorrect expected weight'
    
    #a minimum spanning tree (without cycles) should have (# vertices - 1) edges, so check this assertion below:
    assert mst_edges==len(adj_mat) - 1 #length of adj_mat should be # vertices, so subtract 1 from this to get # of edges
    
    #check to make sure the adjacency and mst matrices are symmetric, since both are undirected
    #at the same time, check to make sure that the mst weights are a subset of the weights in the original adj_mat
    mst_set = [] #empty list
    adj_mat_set = [] #empty list
    for i in range(adj_mat.shape[0]):
        for j in range(i+1):
            assert adj_mat[i,j] == adj_mat[j,i]
            if adj_mat[i,j] != 0:
                adj_mat_set.append(adj_mat[i,j]) #add any non-zero values in adj_mat to the set adj_mat_set
    for i in range(mst.shape[0]):
        for j in range(i+1):
            assert mst[i,j] == mst[i,j]
            if mst[i,j] != 0:
                mst_set.append(mst[i,j]) #add any non-zero values in mst to the set mst_set
    
    assert set(mst_set).issubset(set(adj_mat_set)) #check that mst_set is a subset of adj_mat_set

    
    #minimum spanning trees are always connected--use a version of the breadth-first search algorithm from last week to check this
    """
    def bfs_from_project3(start):
        visited = [] #queue to store visited nodes
        queue = [] #general queue
        path = {} #dictionary for storing parent nodes

        queue.append(start) #add start node to the queue
        visited.append(start) #mark the start node as visited

        #while there are still nodes in the queue...
        while queue:
            cur_node = queue.pop(0) #dequeue the current node

            #for each unvisited neighbor of the current node...
            for nghbr in set(nx.neighbors(self.graph, cur_node)):
                if nghbr not in visited:
                    queue.append(nghbr) #add current neighbor to the queue
                    visited.append(nghbr) #mark current neighbor as visited
                    path[nghbr] = cur_node #store the parent node of the neighbor in the dictionary
        return visited #visited gives the order of traversal
    """
    
    #get create a sequence of node names


def test_mst_small():
    """ Unit test for the construction of a minimum spanning tree on a small graph """
    file_path = './data/small.csv'
    g = Graph(file_path)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 8)


def test_mst_single_cell_data():
    """ Unit test for the construction of a minimum spanning tree using 
    single cell data, taken from the Slingshot R package 
    (https://bioconductor.org/packages/release/bioc/html/slingshot.html)
    """
    file_path = './data/slingshot_example.txt'
    # load coordinates of single cells in low-dimensional subspace
    coords = np.loadtxt(file_path)
    # compute pairwise distances for all 140 cells to form an undirected weighted graph
    dist_mat = pairwise_distances(coords)
    g = Graph(dist_mat)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 57.263561605571695)


def test_mst_student():
    """ TODO: Write at least one unit test for MST construction """
    #create a dummy network and corresponding mst to test on
    adj_mat = np.array([[0, 20, 8, 0, 0, 0, 1],
                   [20, 0, 0, 4, 0, 0, 10],
                   [8, 0, 0, 6, 2, 5, 0],
                   [0, 4, 6, 0, 0, 0, 0],
                   [0, 0, 2, 0, 0, 0, 0],
                   [0, 0, 5, 0, 0, 0, 0],
                   [1, 10, 0, 0, 0, 0, 0]
                   ])
    mst = np.array([[0., 0., 8., 0., 0., 0., 1.],
       [0., 0., 0., 4., 0., 0., 0.],
       [8., 0., 0., 6., 2., 5., 0.],
       [0., 4., 6., 0., 0., 0., 0.],
       [0., 0., 2., 0., 0., 0., 0.],
       [0., 0., 5., 0., 0., 0., 0.],
       [1., 0., 0., 0., 0., 0., 0.]])
    
    check_mst(adj_mat = adj_mat, mst = mst, expected_weight = 26)
    
    #the mst for the adj_mat above should be unique, so make sure that construct_mst() returns the same mst as shown above
    dummyG = Graph(adj_mat)
    assert dummyG.construct_mst() == mst
    
    #for a graph whose mst is NOT unique (like small.csv), check that the mst equals one of two non-unique mst options
    file_path = './data/small.csv'
    small = Graph(file_path)
    assert small.construct_mst() == np.array([[0., 0., 0., 5.],
                                              [0., 0., 1., 2.],
                                              [0., 1., 0., 0.],
                                              [5., 2., 0., 0.]]) or np.array([[0., 0., 0., 5.],
                                                                              [0., 0., 1., 2.],
                                                                              [0., 1., 0., 0.],
                                                                              [5., 2., 0., 0.]])
    
    #other edge cases?
    
    #try an adjacency matrix that includes negative weights
    