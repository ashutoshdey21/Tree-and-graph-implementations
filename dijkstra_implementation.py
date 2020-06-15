# -*- coding: utf-8 -*-

import sys


# =============================================================================

def extract_min_dijkstra(vertex_traversal_details, vertices_list):
    # print("extract min called")
    min_cost = sys.maxsize
    min_vertex = ''
    for i, vertex in enumerate(vertex_traversal_details):
        # print(vertex)
        if vertex_traversal_details.get(vertex)[0] is False:
            if min_cost > vertex_traversal_details.get(vertex)[1]:
                min_cost = vertex_traversal_details.get(vertex)[1]
                min_vertex = vertex

    # print('min vertex', min_vertex)
    vertex_traversal_details.get(min_vertex)[0] = True
    return min_vertex


class Graph(object):
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

    def dijkstra(self, source):
        # print("implemented yet!")

        vertex_traversal_details = {}
        # for vertex_traversal_details --> 0:visited; 1:Distance from source; 2:Immediate parent
        for i, vertex in enumerate(self.vertices):
            vertex_traversal_details.update({vertex: [False, sys.maxsize, '']})

        # Update cost for source
        vertex_traversal_details.get(source)[1] = 0

        vertices_list = []
        while len(vertices_list) != len(self.vertices):

            # Generating output for print_d_and_pi
            # ----------------------------------------------------------------------------
            distance = []
            parent_vertex = []
            iteration = [len(vertices_list)]
            for index, vertex in enumerate(vertex_traversal_details):
                parent_vertex.append(vertex_traversal_details.get(vertex)[2])
                distance.append(vertex_traversal_details.get(vertex)[1])

            self.print_d_and_pi(iteration, distance, parent_vertex)
            # ----------------------------------------------------------------------------

            current_vertex = extract_min_dijkstra(vertex_traversal_details, vertices_list)
            vertices_list.append(current_vertex)

            # for vertex_traversal_details --> 0:visited; 1:Distance from source; 2:Immediate parent
            # iterate through all adjacent vertices
            for each_vertex in self.adj_dict.get(current_vertex):
                # print(each_vertex)
                cost_from_edge = self.matrix[self.vertices.index(current_vertex)][self.vertices.index(each_vertex)]

                cost_parent_each_vertex = vertex_traversal_details.get(current_vertex)[1]
                # Check cost at vertex
                if vertex_traversal_details.get(each_vertex)[1] > cost_from_edge + cost_parent_each_vertex:
                    # if vertex_traversal_details.get(each_vertex)[0] is False:
                    # Update cost
                    vertex_traversal_details.get(each_vertex)[1] = cost_from_edge + cost_parent_each_vertex
                    # Update parent
                    vertex_traversal_details.get(each_vertex)[2] = current_vertex

        # print(vertices_list)
        # for i, vertex in enumerate(vertex_traversal_details):
        #     print(vertex, vertex_traversal_details.get(vertex))

    def print_d_and_pi(self, iteration, d, pi):
        assert ((len(d) == len(self.vertices)) and
                (len(pi) == len(self.vertices)))

        print("Iteration: {0}".format(iteration))
        for i, v in enumerate(self.vertices):
            print("Vertex: {0}\td: {1}\tpi: {2}".format(v, 'inf' if d[i] == sys.maxsize else d[i], pi[i]))


def main():
    # Thoroughly main your program and produce useful output.

    graph = Graph(['s', 't', 'x', 'y', 'z'],
                  [('s', 't', 3),
                   ('s', 'y', 5),
                   ('t', 'x', 6),
                   ('t', 'y', 2),
                   ('x', 'z', 2),
                   ('y', 't', 1),
                   ('y', 'x', 4),
                   ('y', 'z', 6),
                   ('z', 's', 3),
                   ('z', 'x', 7)])
    graph.dijkstra('s')


if __name__ == '__main__':
    main()
