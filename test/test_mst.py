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
    for i in range(adj_mat.shape[0]):
        for j in range(i+1):
            assert adj_mat[i,j] == adj_mat[j,i]
    for i in range(mst.shape[0]):
        for j in range(i+1):
            assert mst[i,j] == mst[i,j]
    
    #minimum spanning trees are always connected--use a version of the breadth-first search algorithm from last week to check this
    

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
    #create a dummy networks to test on
    adj_mat = np.array([[0, 20, 8, 0, 0, 0, 1],
                   [20, 0, 0, 4, 0, 0, 10],
                   [8, 0, 0, 6, 2, 5, 0],
                   [0, 4, 6, 0, 0, 0, 0],
                   [0, 0, 2, 0, 0, 0, 0],
                   [0, 0, 5, 0, 0, 0, 0],
                   [1, 10, 0, 0, 0, 0, 0]
                   ])
    check
    
    #create another dummy network that is an edge case, i.e. that has a cycle in it
    
    pass
