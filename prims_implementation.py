# -*- coding: utf-8 -*-

import sys


# =============================================================================

def extract_min_prims(self, vertices_list, cost_at_vertex):
    # print("extract min called")
    min_cost = sys.maxsize
    min_vertex = ''
    for i, vertex in enumerate(cost_at_vertex):

        if vertex not in vertices_list:
            if min_cost > cost_at_vertex.get(vertex):
                min_cost = cost_at_vertex.get(vertex)
                min_vertex = vertex

    # vertices_list.append(min_vertex)
    return min_vertex


class Graph(object):
    """docstring for Graph"""
    user_defined_vertices = []
    dfs_timer = 0

    def __init__(self, vertices, edges):
        super(Graph, self).__init__()
        n = len(vertices)
        self.matrix = [[0 for x in range(n)] for y in range(n)]
        self.vertices = vertices
        self.edges = edges
        self.adj_dict = {}
        for edge in edges:
            x = vertices.index(edge[0])
            y = vertices.index(edge[1])
            self.matrix[x][y] = edge[2]
            # print(edge)
            # Building adjacency list
            temp = self.adj_dict.get(vertices[x], [])
            temp.append(vertices[y])
            self.adj_dict[vertices[x]] = temp

    def display(self):
        print(self.vertices)
        for i, v in enumerate(self.vertices):
            print(v, self.matrix[i])

    def prim(self, root):

        # to maintain the cost at each vertex
        cost_at_vertex = {}
        # to maintain the parent for each vertex
        parent_at_vertex = {}
        for i, v in enumerate(self.vertices):
            cost_at_vertex.update({v: sys.maxsize})
            parent_at_vertex.update({v: ''})
        # print(val_at_vertex)
        vertices_list = []
        current_vertex = root
        cost_at_vertex.update({current_vertex: 0})
        parent_at_vertex.update({current_vertex: ''})

        while len(vertices_list) != len(self.vertices):

            # Generating output for print_d_and_pi
            # ----------------------------------------------------------------------------
            distance = []
            parent_vertex = []
            iteration = [len(vertices_list)]
            for index, vertex in enumerate(parent_at_vertex):
                parent_vertex.append(parent_at_vertex.get(vertex))
                distance.append(cost_at_vertex.get(vertex))

            self.print_d_and_pi(iteration, distance, parent_vertex)
            # ----------------------------------------------------------------------------

            current_vertex = extract_min_prims(self, vertices_list, cost_at_vertex)
            vertices_list.append(current_vertex)

            # print(self.adj_dict.get(current_vertex))
            for each_vertex in self.adj_dict.get(current_vertex):

                cost_from_edge = self.matrix[self.vertices.index(each_vertex)][self.vertices.index(current_vertex)]
                if cost_at_vertex.get(each_vertex) > cost_from_edge and each_vertex not in vertices_list:
                    # Update cost
                    cost_at_vertex.update({each_vertex: cost_from_edge})
                    # Update parent
                    parent_at_vertex.update({each_vertex: current_vertex})

            # print(vertices_list)
        # print(parent_at_vertex)
        # print(cost_at_vertex)

    def print_d_and_pi(self, iteration, d, pi):
        assert ((len(d) == len(self.vertices)) and
                (len(pi) == len(self.vertices)))

        print("Iteration: {0}".format(iteration))
        for i, v in enumerate(self.vertices):
            print("Vertex: {0}\td: {1}\tpi: {2}".format(v, 'inf' if d[i] == sys.maxsize else d[i], pi[i]))


def main():
    # Thoroughly main your program and produce useful output.

    graph = Graph(['A', 'B', 'C', 'D', 'E', 'G', 'H', 'I', 'J'],
                  [('A', 'B', 5),
                   ('A', 'G', 22),
                   ('A', 'E', 7),
                   ('B', 'G', 1),
                   ('E', 'G', 4),
                   ('B', 'J', 10),
                   ('G', 'J', 8),
                   ('J', 'I', 20),
                   ('G', 'I', 21),
                   ('G', 'C', 2),
                   ('E', 'C', 15),
                   ('E', 'D', 26),
                   ('D', 'C', 9),
                   ('C', 'I', 6),
                   ('D', 'H', 8),
                   ('C', 'H', 3),
                   ('H', 'I', 11),
                   ('B', 'A', 5),
                   ('G', 'A', 22),
                   ('E', 'A', 7),
                   ('G', 'B', 1),
                   ('G', 'E', 4),
                   ('J', 'B', 10),
                   ('J', 'G', 8),
                   ('I', 'J', 20),
                   ('I', 'G', 21),
                   ('C', 'G', 2),
                   ('C', 'E', 15),
                   ('D', 'E', 26),
                   ('C', 'D', 9),
                   ('I', 'C', 6),
                   ('H', 'D', 8),
                   ('H', 'C', 3),
                   ('I', 'H', 11)])
    graph.prim('G')
    # graph.display()


if __name__ == '__main__':
    main()
