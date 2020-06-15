# -*- coding: utf-8 -*-

import sys


# =============================================================================

def relax_bellman_ford(u, v, weight_u_v, vertex_traversal_details):
    # for vertex_traversal_details --> 0:Distance from source; 1:Immediate parent
    if vertex_traversal_details.get(v)[0] > vertex_traversal_details.get(u)[0] + weight_u_v:
        vertex_traversal_details.get(v)[0] = vertex_traversal_details.get(u)[0] + weight_u_v
        vertex_traversal_details.get(v)[1] = u

    return vertex_traversal_details


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
            # Building adjacency list
            temp = self.adj_dict.get(vertices[x], [])
            temp.append(vertices[y])
            self.adj_dict[vertices[x]] = temp

    def display(self):
        print(self.vertices)
        for i, v in enumerate(self.vertices):
            print(v, self.matrix[i])

    def bellman_ford(self, source):
        print('executing bellman ford')
        vertex_traversal_details = {}
        # visited_list = []
        # for vertex_traversal_details --> 0:Distance from source; 1:Immediate parent
        for i, vertex in enumerate(self.vertices):
            vertex_traversal_details.update({vertex: [sys.maxsize, '']})

        vertex_traversal_details.update({source: [0, '']})

        for i in range(len(self.vertices) - 1):

            # Generating output for print_d_and_pi
            # ----------------------------------------------------------------------------
            distance = []
            parent_vertex = []
            iteration = [i]
            for index, vertex in enumerate(vertex_traversal_details):
                parent_vertex.append(vertex_traversal_details.get(vertex)[1])
                distance.append(vertex_traversal_details.get(vertex)[0])

            self.print_d_and_pi(iteration, distance, parent_vertex)
            # ----------------------------------------------------------------------------

            for edge in self.edges:
                u = edge[0]
                v = edge[1]
                weight_u_v = edge[2]
                # print(u, v, weight_u_v)
                # relaxation
                vertex_traversal_details = relax_bellman_ford(u, v, weight_u_v, vertex_traversal_details)

        # main for solution
        for edge in self.edges:
            u = edge[0]
            v = edge[1]
            weight_u_v = edge[2]
            if vertex_traversal_details.get(v)[0] > vertex_traversal_details.get(u)[0] + weight_u_v:
                print('no solution')
                break

        # Generating final to show the change in output for print_d_and_pi
        # ----------------------------------------------------------------------------
        distance = []
        parent_vertex = []
        iteration = [i]
        for index, vertex in enumerate(vertex_traversal_details):
            parent_vertex.append(vertex_traversal_details.get(vertex)[1])
            distance.append(vertex_traversal_details.get(vertex)[0])

        self.print_d_and_pi(iteration, distance, parent_vertex)
        # ----------------------------------------------------------------------------
        # print(vertex_traversal_details)
        #
        # self.print_d_and_pi(iteration, distance, parent_vertex)

    def print_d_and_pi(self, iteration, d, pi):
        assert ((len(d) == len(self.vertices)) and
                (len(pi) == len(self.vertices)))

        print("Iteration: {0}".format(iteration))
        for i, v in enumerate(self.vertices):
            print("Vertex: {0}\td: {1}\tpi: {2}".format(v, 'inf' if d[i] == sys.maxsize else d[i], pi[i]))


def main():
    # Thoroughly main your program and produce useful output.

    # Q5
    graph = Graph(['s', 't', 'x', 'y', 'z'],
                  [('t', 'x', 5),
                   ('t', 'y', 8),
                   ('t', 'z', -4),
                   ('x', 't', -2),
                   ('y', 'x', -3),
                   ('y', 'z', 9),
                   ('z', 'x', 7),
                   ('z', 's', 2),
                   ('s', 't', 6),
                   ('s', 'y', 7)])
    graph.bellman_ford('z')

    # Q5 alternate
    graph = Graph(['s', 't', 'x', 'y', 'z'],
                  [('t', 'x', 5),
                   ('t', 'y', 8),
                   ('t', 'z', -4),
                   ('x', 't', -2),
                   ('y', 'x', -3),
                   ('y', 'z', 9),
                   ('z', 'x', 4),
                   ('z', 's', 2),
                   ('s', 't', 6),
                   ('s', 'y', 7)])
    graph.bellman_ford('s')


if __name__ == '__main__':
    main()
