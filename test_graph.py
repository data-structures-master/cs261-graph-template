# DO NOT MODIFY THIS FILE
# Run me via: python3 -m unittest test_graph

import unittest
import time
import operator
from graph import Graph

class TestGraph(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A Graph exists.
        """
        try:
            Graph()
        except NameError:
            self.fail("Could not instantiate Graph.")

#     def test_internal(self):
#         """
#         A graph uses an 'adjacency list' to represent vertices and edges.
#         """
#         g = Graph()
#         self.assertEqual(dict, type(g.data))

#     """
#     Empty graphs.
#     """

#     def test_adjacent_empty(self):
#         """
#         An empty graph has no vertices, so adjacent returns false.
#         """
#         g = Graph()
#         self.assertFalse(g.adjacent('A', 'B'))

#     def test_neighbors_empty(self):
#         """
#         Asking for the neighbors of any vertex in an empty graph returns an empty
#         list.
#         """
#         g = Graph()
#         self.assertEqual([], g.neighbors('A'))

#     def test_add_vertex_empty(self):
#         """
#         When storing a new vertex, the graph associates an empty list of neighbors.
#         """
#         g = Graph()
#         g.add_vertex('A')
#         self.assertEqual([], g.data['A'])

#     def test_remove_vertex_nonexistent(self):
#         """
#         When removing a vertex that does not exist, nothing happens.
#         Hint: Just pass for now.
#         """
#         g = Graph()
#         try:
#             g.remove_vertex('A')
#         except KeyError:
#             self.fail('Removing a key raised an error.')
#         self.assertEqual({}, g.data)

#     def test_add_edge_nonexistent(self):
#         """
#         Adding an edge between two vertices that do not exist does nothing.
#         Hint: Just pass for now.
#         """
#         g = Graph()
#         try:
#             g.add_edge('A', 'B')
#         except KeyError:
#             self.fail("Adding invalid edge raised a KeyError")

#     def test_remove_edge_nonexistent(self):
#         """
#         Removing an edge that does not exist does nothing.
#         Hint: Just pass for now.
#         """
#         g = Graph()
#         try:
#             g.remove_edge('A', 'B')
#         except KeyError:
#             self.fail("Removing nonexistent edge raised a KeyError")

#     """
#     Single-vertex graph.
#     """

#     def test_adjacent_one(self):
#         """
#         A graph with one vertex has no neighbors, so adjacent returns false.
#         """
#         g = Graph()
#         g.data['A'] = []
#         self.assertFalse(g.adjacent('A', 'B'))
#         self.assertFalse(g.adjacent('A', 'FAKE'))

#     def test_neighbors_one(self):
#         """
#         Asking for the neighbors of a vertex in an graph with just one vertex
#         returns an empty list.
#         """
#         g = Graph()
#         g.data['A'] = []
#         self.assertEqual([], g.neighbors('A'))

#     def test_add_vertex_one(self):
#         """
#         When storing a new vertex in a graph with a single vertex, the graph
#         adds the new vertex and associates an empty list of neighbors.
#         """
#         g = Graph()
#         g.data['A'] = []
#         g.add_vertex('B')
#         self.assertEqual([], g.data['B'])
#         self.assertEqual([], g.data['A'])

#     def test_add_vertex_existing(self):
#         """
#         When adding a vertex that already exists, the graph does not modify the
#         existing vertex.
#         """
#         g = Graph()
#         g.data['A'] = ['FAKE']
#         g.add_vertex('A')
#         self.assertEqual(['FAKE'], g.data['A'])

#     def test_remove_vertex_one(self):
#         """
#         Removing a vertex from a graph removes its entry from the graph's
#         adjacency list.
#         """
#         g = Graph()
#         g.data['A'] = []
#         g.remove_vertex('A')
#         self.assertRaises(KeyError, operator.itemgetter('A'), g.data)

#     def test_add_edge_one(self):
#         """
#         Adding an edge between an existing vertex and one that does not exist
#         does nothing.
#         """
#         g = Graph()
#         g.data['A'] = []
#         try:
#             g.add_edge('A', 'B')
#         except KeyError:
#             self.fail("Adding invalid edge raised a KeyError")

#     def test_remove_edge_one(self):
#         """
#         Removing an edge that does not exist does nothing.
#         """
#         g = Graph()
#         g.data['A'] = []
#         try:
#             g.remove_edge('A', 'B')
#         except KeyError:
#             self.fail("Removing nonexistent edge raised a KeyError")

#     """
#     Graphs with two vertices.
#     """

#     def test_adjacent_two(self):
#         """
#         A vertex, v2, is a neighbor of v1 when v2 is present in v1's list of neighbors.
#         Note: Neighbors should indeed be present in each others' list of neighbors,
#         but this isn't the job of the `adjacent` method.
#         """
#         g = Graph()
#         g.data['A'] = ['B']
#         g.data['B'] = []  # Intentionally minimal. See the Note above.
#         self.assertTrue(g.adjacent('A', 'B'))
#         self.assertFalse(g.adjacent('A', 'FAKE'))
#         self.assertFalse(g.adjacent('B', 'A'))

#     def test_neighbors_two(self):
#         """
#         Asking for the neighbors of any vertex returns a list of its neighbors.
#         """
#         g = Graph()
#         g.data['A'] = ['B', 'FAKE']
#         g.data['B'] = ['A']
#         self.assertEqual(['B', 'FAKE'], g.neighbors('A'))
#         self.assertEqual(['A'], g.neighbors('B'))
#         self.assertEqual([], g.neighbors('FAKE'))

#     def test_remove_vertex_two(self):
#         """
#         Removing a vertex also removes it from all vertex neighbors lists.
#         """
#         g = Graph()
#         g.data['A'] = ['B']
#         g.data['B'] = ['A']
#         g.remove_vertex('A')
#         self.assertRaises(KeyError, operator.itemgetter('A'), g.data)
#         self.assertEqual([], g.data['B'])

#     def test_add_edge_two(self):
#         """
#         Adding an edge between two vertices adds each vertex to both of their
#         neighbor lists.
#         """
#         g = Graph()
#         g.data['A'] = []
#         g.data['B'] = []
#         g.add_edge('A', 'B')
#         self.assertEqual(['B'], g.data['A'])
#         self.assertEqual(['A'], g.data['B'])
#         g.data['A'] = []
#         g.data['B'] = []
#         g.add_edge('B', 'A')
#         self.assertEqual(['B'], g.data['A'])
#         self.assertEqual(['A'], g.data['B'])

#     def test_add_edge_existing_two(self):
#         """
#         Adding an edge to vertices that already share and edge does not create a
#         second edge.
#         """
#         g = Graph()
#         g.data['A'] = ['B']
#         g.data['B'] = ['A']
#         g.add_edge('A', 'B')
#         self.assertEqual(['B'], g.data['A'])
#         self.assertEqual(['A'], g.data['B'])

#     def test_remove_edge_two(self):
#         """
#         Removing an edge between two vertices removes each vertex from both
#         neighbors lists.
#         """
#         g = Graph()
#         g.data['A'] = ['B']
#         g.data['B'] = ['A']
#         g.remove_edge('A', 'B')
#         self.assertEqual([], g.data['A'])
#         self.assertEqual([], g.data['B'])
#         g.data['A'] = ['B']
#         g.data['B'] = ['A']
#         g.remove_edge('B', 'A')
#         self.assertEqual([], g.data['A'])
#         self.assertEqual([], g.data['B'])
 
#     def test_remove_edge_nonexisting_two(self):
#         """
#         Removing an edge that does not exist does nothing.
#         """
#         g = Graph()
#         g.data['A'] = ['FAKE']
#         g.data['B'] = ['FAKE 2']
#         g.remove_edge('A', 'B')
#         g.remove_edge('B', 'A')
#         self.assertEqual(['FAKE'], g.data['A'])
#         self.assertEqual(['FAKE 2'], g.data['B'])

#     """
#     Larger graphs
#     """

#     def test_adjacent(self):
#         """
#         Two vertices are adjacent if they share an edge.
#         """
#         g = larger_graph()
#         self.assertTrue(g.adjacent('A', 'B'))
#         self.assertTrue(g.adjacent('B', 'A'))
#         self.assertTrue(g.adjacent('A', 'C'))
#         self.assertTrue(g.adjacent('C', 'A'))
#         self.assertTrue(g.adjacent('A', 'D'))
#         self.assertTrue(g.adjacent('D', 'A'))
#         self.assertTrue(g.adjacent('B', 'C'))
#         self.assertTrue(g.adjacent('C', 'B'))
#         self.assertFalse(g.adjacent('B', 'D'))
#         self.assertFalse(g.adjacent('D', 'B'))
#         self.assertFalse(g.adjacent('C', 'D'))
#         self.assertFalse(g.adjacent('D', 'C'))

#     def test_neighbors(self):
#         """
#         Vertices that share an edge are neighbors.
#         """
#         g = larger_graph()
#         self.assertEqual(['B', 'C', 'D'], g.neighbors('A'))
#         self.assertEqual(['A', 'C'], g.neighbors('B'))
#         self.assertEqual(['A', 'B'], g.neighbors('C'))
#         self.assertEqual(['A'], g.neighbors('D'))

#     def test_add_vertex(self):
#         """
#         Adding a vertex to a graph only creates a new entry in the adjacency list.
#         """
#         g = larger_graph()
#         g.add_vertex('E')
#         self.assertEqual([], g.data['E'])
#         self.assertEqual(['B', 'C', 'D'], g.data['A'])
#         self.assertEqual(['A', 'C'], g.data['B'])
#         self.assertEqual(['A', 'B'], g.data['C'])
#         self.assertEqual(['A'], g.data['D'])

#     def test_remove_vertex(self):
#         """
#         Removing a vertex also removes its edges.
#         Hint: Be efficient. Traversing all the vertices (keys) is inefficient.
#         """
#         g = larger_graph()
#         g.remove_vertex('A')
#         self.assertEqual(['C'], g.data['B'])
#         self.assertEqual(['B'], g.data['C'])
#         self.assertEqual([], g.data['D'])

#     def test_add_edge(self):
#         """
#         Adding an edge between two vertices connects them as adjacent neighbors.
#         """
#         g = larger_graph()
#         g.add_edge('D', 'B')
#         self.assertEqual(['A', 'C', 'D'], g.data['B'])
#         self.assertEqual(['A', 'B'], g.data['D'])
#         self.assertTrue(g.adjacent('B', 'D'))
#         self.assertTrue(g.adjacent('D', 'B'))
#         self.assertEqual(['B', 'C', 'D'], g.data['A'])
#         self.assertEqual(['A', 'B'], g.data['C'])

#     def test_remove_edge(self):
#         """
#         Removing an edge disconnects two vertices.
#         """
#         g = larger_graph()
#         g.remove_edge('A', 'B')
#         self.assertEqual(['C', 'D'], g.data['A'])
#         self.assertEqual(['C'], g.data['B'])
#         self.assertFalse(g.adjacent('A', 'B'))
#         self.assertFalse(g.adjacent('B', 'A'))
#         self.assertEqual(['A', 'B'], g.data['C'])
#         self.assertEqual(['A'], g.data['D'])

#     """
#     Properties
#     """

#     def test_v(self):
#         """
#         |V| is the number of vertices in a graph.
#         """
#         g = Graph()
#         g.add_vertex('A')
#         self.assertEqual(1, g.v())
#         g.add_vertex('B')
#         g.add_vertex('C')
#         self.assertEqual(3, g.v())

#     def test_e(self):
#         """
#         |E| is the number of edges in a graph.
#         Hint: There's an easy way - read or look it up?
#         Bonus: Try reduce.
#         """
#         g = larger_graph()
#         self.assertEqual(4, g.e())
#         g.add_edge('D', 'B')
#         self.assertEqual(5, g.e())

#     """
#     Breadth-First Search Traversal
#     """

#     def test_bfs_empty_graph(self):
#         """
#         BFS on an empty graph or from a non-existent vertex returns an empty list.
#         """
#         g = Graph()
#         self.assertEqual([], g.bfs('A'))

#     def test_bfs_nonexistent_start_vertex(self):
#         """
#         Starting DFS from a vertex not in the graph returns an empty list.
#         """
#         g = Graph()
#         g.add_vertex('A')
#         g.add_vertex('B')
#         self.assertEqual([], g.bfs('C'))
    
#     def test_bfs_single_vertex(self):
#         """
#         BFS on a graph with one isolated vertex returns a list containing only that vertex.
#         """
#         g = Graph()
#         g.add_vertex('A')
#         self.assertEqual(['A'], g.bfs('A'))

#     def test_bfs_two_connected_vertices(self):
#         """
#         BFS on two connected vertices returns both vertices in breadth-first order.
#         """
#         g = Graph()
#         g.add_vertex('A')
#         g.add_vertex('B')
#         g.add_edge('A', 'B')
#         self.assertEqual(['A', 'B'], g.bfs('A'))

#     def test_bfs_linear_chain(self):
#         """
#         BFS on a chain of vertices (A--B--C) returns all vertices in breadth-first order.
#         Hint: add a queue to your implementation.
#               from queue import Queue
#         Hint 2: Remember to check if a neighbor has already been visited
#                 before adding it to the queue!
#         """
#         g = Graph()
#         g.add_vertex('A')
#         g.add_vertex('B')
#         g.add_vertex('C')
#         g.add_edge('A', 'B')
#         g.add_edge('B', 'C')
#         self.assertEqual(['A', 'B', 'C'], g.bfs('A'))

#     def test_bfs_discovers_all_neighbors_first(self):
#         r"""
#           A
#          / \
#         B   C
#         |  / \
#         D  E  F

#        BFS visits all direct neighbors of the start vertex before vertices at depth 2.
#        """
#         g = Graph()
#         g.add_vertex('A')
#         g.add_vertex('B')
#         g.add_vertex('C')
#         g.add_vertex('D')
#         g.add_vertex('E')
#         g.add_vertex('F')
#         g.add_edge('A', 'B')
#         g.add_edge('A', 'C')
#         g.add_edge('B', 'D')
#         g.add_edge('C', 'E')
#         g.add_edge('C', 'F')
#         self.assertEqual(['A', 'B', 'C', 'D', 'E', 'F'], g.bfs('A'))

#     def test_bfs_with_multiple_paths(self):
#         r"""
#          A
#         / \
#        B   C
#         \ /
#          D

#         BFS handles graphs where a vertex can be reached by multiple paths
#         and visits it once.
#         """
#         g = Graph()
#         g.add_vertex('A')
#         g.add_vertex('B')
#         g.add_vertex('C')
#         g.add_vertex('D')
#         g.add_edge('A', 'B')
#         g.add_edge('A', 'C')
#         g.add_edge('B', 'D')
#         g.add_edge('C', 'D')
#         self.assertEqual(['A', 'B', 'C', 'D'], g.bfs('A'))

#     def test_bfs_with_largest_graph(self):
#         """
#         BFS handles graphs where a vertex can be reached by multiple paths
#         and visits it once.
#         """
#         g = largest_graph()
#         self.assertEqual([1, 2, 3, 4, 7, 8, 5, 6, 9], g.bfs(1))

# """
#     Depth-First Search Traversal
# """

# def test_dfs_empty_graph(self):
#     """
#     An empty graph has no vertices, so dfs returns an empty list.
#     """
#     g = Graph()
#     self.assertEqual([], g.dfs('A'))

# def test_dfs_nonexistent_start_vertex(self):
#     """
#     Starting DFS from a vertex not in the graph returns an empty list.
#     """
#     g = Graph()
#     g.add_vertex('A')
#     g.add_vertex('B')
#     self.assertEqual([], g.dfs('C'))

# def test_dfs_single_vertex(self):
#     """
#     DFS on a single isolated vertex returns just that vertex.
#     """
#     g = Graph()
#     g.add_vertex('A')
#     self.assertEqual(['A'], g.dfs('A'))

# def test_dfs_linear_chain(self):
#     """
#     DFS on a chain of vertices (A--B--C) returns all vertices in depth-first order.
#     Hint: Use a stack (LIFO) instead of a queue.
#           from collections import deque (and use LIFO) or just use a list
#     Hint 2: Remember to pop a vertex from them stack once all its neighbors
#             have been visited
#     """
#     g = Graph()
#     g.add_vertex('A')
#     g.add_vertex('B')
#     g.add_vertex('C')
#     g.add_edge('A', 'B')
#     g.add_edge('B', 'C')
#     result = g.dfs('A')
#     self.assertEqual(['A', 'B', 'C'], result) 

# def test_dfs_reverse_direction(self):
#     """
#     DFS starting from the end of a chain traverses backwards.
#     """
#     g = Graph()
#     g.add_vertex('A')
#     g.add_vertex('B')
#     g.add_vertex('C')
#     g.add_edge('A', 'B')
#     g.add_edge('B', 'C')
#     result = g.dfs('C')
#     self.assertEqual(['C', 'B', 'A'], result) # C is visited first

# def test_dfs_explores_depth_first(self):
#     r"""
#       A
#      / \
#     B   C
#     |
#     D

#     DFS explores depth first before backtracking.
#     Starting from A, DFS should go deep into B's branch before exploring C.
#     """
#     g = Graph()
#     g.add_vertex('A')
#     g.add_vertex('B')
#     g.add_vertex('C')
#     g.add_vertex('D')
#     g.add_edge('A', 'B')
#     g.add_edge('A', 'C')
#     g.add_edge('B', 'D')
#     result = g.dfs('A')
#     self.assertEqual(4, len(result))
#     self.assertEqual(['A','B','D','C'], result)

# def test_dfs_with_cycle(self):
#     r"""
#     A---B
#     |   |
#     D---C

#     DFS handles cycles without infinite loops.
#     """
#     g = Graph()
#     g.add_vertex('A')
#     g.add_vertex('B')
#     g.add_vertex('C')
#     g.add_vertex('D')
#     g.add_edge('A', 'B')
#     g.add_edge('A', 'D')
#     g.add_edge('B', 'C')
#     g.add_edge('C', 'D')
#     result = g.dfs('A')
#     # All vertices should be visited exactly once
#     self.assertEqual(4, len(result))
#     self.assertEqual(4, len(set(result)))  # No duplicates
#     self.assertEqual(['A','B','C','D'], result)


# def test_dfs_vs_bfs_finds_same_vertices(self):
#     """
#     DFS and BFS should visit the same vertices (same reach),
#     but potentially in different orders.
#     """
#     g = Graph()
#     g.add_vertex('A')
#     g.add_vertex('B')
#     g.add_vertex('C')
#     g.add_vertex('D')
#     g.add_edge('A', 'B')
#     g.add_edge('A', 'C')
#     g.add_edge('B', 'D')
#     g.add_edge('C', 'D')
    
#     dfs_result = set(g.dfs('A'))
#     bfs_result = set(g.bfs('A'))
    
#     self.assertEqual(dfs_result, bfs_result)

# def test_dfs_with_largest_graph(self):
#     """
#     DFS handles larger graphs with complex connectivity.
#     """
#     g = largest_graph()
#     result = g.dfs(1)
#     # Should visit all 9 vertices
#     self.assertEqual(9, len(result)) #no duplicates
#     self.assertEqual(set(range(1, 10)), set(result)) #all vertices are visited
#     self.assertEqual([1, 2, 4, 9, 7, 8, 3, 5, 6], result)


def larger_graph():
    r"""
       B
       | \
    D--A--C
    """
    g = Graph()
    g.data['A'] = ['B', 'C', 'D']
    g.data['B'] = ['A', 'C']
    g.data['C'] = ['A', 'B']
    g.data['D'] = ['A']
    return g

def largest_graph():
    r"""
    1 -- 2 -- 4 -- 9
    |    |         |
    3    7 --------+
   / \   |
  5   6  8
    """
    g = Graph()
    g.data[1] = [2, 3]
    g.data[2] = [1, 4, 7, 8]
    g.data[3] = [1, 5, 6]
    g.data[4] = [2, 9]
    g.data[5] = [3]
    g.data[6] = [3]
    g.data[7] = [2, 9]
    g.data[8] = [2]
    g.data[9] = [4, 7]
    return g

def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
