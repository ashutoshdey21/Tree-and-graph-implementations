# -*- coding: utf-8 -*-

import sys


# =============================================================================

def extract_min_prims(vertices_list, cost_at_vertex):
    # print("extract min called")
    min_cost = sys.maxsize
    min_vertex = ''
    for i, vertex in enumerate(cost_at_vertex):

        if vertex not in vertices_list:
            if min_cost > cost_at_vertex.get(vertex):
                min_cost = cost_at_vertex.get(vertex)
                min_vertex = vertex

    vertices_list.append(min_vertex)
    return min_vertex, vertices_list


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
        # ToDo

        cost_at_vertex = {}
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
            current_vertex, vertices_list = extract_min_prims(vertices_list, cost_at_vertex)

            # print(self.adj_dict.get(current_vertex))
            for each_vertex in self.adj_dict.get(current_vertex):

                cost_from_edge = self.matrix[self.vertices.index(each_vertex)][self.vertices.index(current_vertex)]
                if cost_at_vertex.get(each_vertex) > cost_from_edge and each_vertex not in vertices_list:
                    # Update cost
                    cost_at_vertex.update({each_vertex: cost_from_edge})
                    # Update parent
                    parent_at_vertex.update({each_vertex: current_vertex})

        print('vertices visited')
        print(vertices_list)
        print('{child: parent}')
        print(parent_at_vertex)
        print('cost at each vertex')
        print(cost_at_vertex)


def main():
    # Thoroughly test your program and produce useful output.

    graph = Graph(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                  [('A', 'H', 6),
                   ('H', 'A', 6),
                   ('A', 'B', 4),
                   ('B', 'A', 4),
                   ('B', 'H', 5),
                   ('H', 'B', 5),
                   ('B', 'C', 9),
                   ('C', 'B', 9),
                   ('G', 'H', 14),
                   ('H', 'G', 14),
                   ('F', 'H', 10),
                   ('H', 'F', 10),
                   ('B', 'E', 2),
                   ('E', 'B', 2),
                   ('G', 'F', 3),
                   ('F', 'G', 3),
                   ('E', 'F', 8),
                   ('F', 'E', 8),
                   ('D', 'E', 15),
                   ('E', 'D', 15)])
    graph.prim('G')
    # graph.display()


if __name__ == '__main__':
    main()
