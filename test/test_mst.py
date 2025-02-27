# write tests for bfs
import pytest
import numpy as np
from mst import Graph
from sklearn.metrics import pairwise_distances


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
            #check the symmetry of the rounded values (since some decimals are like 0.00000001 off)
            assert round(adj_mat[i,j],6) == round(adj_mat[j,i],6)
            if adj_mat[i,j] != 0:
                adj_mat_set.append(round(adj_mat[i,j], 6)) #add any non-zero values in adj_mat to the set adj_mat_set
    for i in range(mst.shape[0]):
        for j in range(i+1):
            #check the symmetry of the rounded values (since some decimals are like 0.00000001 off)
            assert round(mst[i,j],6) == round(mst[i,j],6)
            if mst[i,j] != 0:
                mst_set.append(round(mst[i,j], 6)) #add any non-zero values in mst to the set mst_set
    
    assert set(mst_set).issubset(set(adj_mat_set)) #check that mst_set is a subset of adj_mat_set

    
    
    #minimum spanning trees are always connected--use a version of the breadth-first search algorithm from last week to check this
    vertices = list(range(0,len(mst))) #vertex labels. Length of this is the number of vertices in mst
    def bfs(start, adj_mat):
        visited = [] #queue to store visited nodes
        queue = [] #general queue
        path = {} #dictionary for storing parent nodes

        queue.append(start) #add start node to the queue
        visited.append(start) #mark the start node as visited

        #while there are still nodes in the queue...
        while queue:
            cur_node = queue.pop(0) #dequeue the current node

            #for each unvisited neighbor of the current node...
            for i in range(0,len(adj_mat)):
                if (adj_mat[cur_node][i] != 0) and (i not in visited): #search the row of the current node to find neighbors
                    queue.append(i) #add neighbor node to the queue
                    visited.append(i) #mark current neighbor as visited
                    path[i] = cur_node #store the parent node of the neighbor in the dictionary path
        return visited #visited returns the order of traversal (and traversal cannot occur if the graph isn't connnected)
            
    
    assert len(bfs(vertices[0], adj_mat))==len(vertices) #length of traversed path should equal the total number of vertices

    



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
    
    #check the mst
    check_mst(adj_mat = adj_mat, mst = mst, expected_weight = 26)
    
    #the mst for the adj_mat above should be unique, so make sure that construct_mst() returns the same mst as shown above
    dummyG = Graph(adj_mat)
    dummyG.construct_mst() #construct mst for dummy network above
    #check that the expected and constructed msts are equal
    comparison = dummyG.mst==mst
    arrays_are_equal = comparison.all() #compares all array values to make sure they are equal at the same indices
    assert arrays_are_equal==True
    
    
    
    
    #for a graph whose mst is NOT unique (like small.csv), check that the mst equals one of two non-unique mst options
    file_path = './data/small.csv'
    
    mst1 = np.array([[0., 0., 0., 5.],
                     [0., 0., 1., 2.],
                     [0., 1., 0., 0.],
                     [5., 2., 0., 0.]])
    
    mst2 = np.array([[0., 5., 0., 0.],
                     [5., 0., 1., 2.],
                     [0., 1., 0., 0.],
                     [0., 2., 0., 0.]])
    
    
    small = Graph(file_path)
    small.construct_mst() #construct mst for small network
    #check that the constructed mst meets certain criteria
    check_mst(adj_mat = small.adj_mat, mst=small.mst, expected_weight = 8)
    #check that one of the expected msts is equal to the constructed one
    comparison1 = small.mst==mst1
    comparison2 = small.mst==mst2
    arrays1_are_equal = comparison1.all() #compares all array values to make sure they are equal at the same indices
    arrays2_are_equal = comparison2.all()
    assert (arrays1_are_equal==True) or (arrays2_are_equal==True)
    
    
    
    
    
    #another edge case is an adjacency matrix that includes negative weights
    adj_mat = np.array([[0, 2, -1, 4],
                        [2, 0, 0, 5],
                        [-1, 0, 0, -2],
                        [4, 5, -2, 0]])
    mst = np.array([[0, 2, -1, 0],
                    [2, 0, 0, 0],
                    [-1, 0, 0, -2],
                    [0, 0, -2, 0]])
    
    negatives = Graph(adj_mat)
    negatives.construct_mst() #construct mst for a network with negative edges
    #check that the constructed mst meets certain criteria
    check_mst(adj_mat=negatives.adj_mat, mst=negatives.mst, expected_weight = -1)
    #check that the (unique, in this case) expected mst for the network is equal to the constructed one
    comparison = negatives.mst==mst
    arrays_are_equal = comparison.all() #compares all array values to make sure they are equal at the same indices
    assert arrays_are_equal==True