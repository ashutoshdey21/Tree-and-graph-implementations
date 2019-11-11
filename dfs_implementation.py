# -*- coding: utf-8 -*-


# =============================================================================

def dfs_visit(v, vertex_color, self, discover):
    vertex_color.update({v: 'grey'})
    # print({v: 'grey'})
    discover.append(v)
    self.dfs_timer += 1
    vertices_for_v = self.adj_dict.get(v)
    # print(vertices_for_v)
    for each_vertex in vertices_for_v:
        if vertex_color.get(each_vertex) == 'white':
            dfs_visit(each_vertex, vertex_color, self, discover)
    vertex_color.update({v: 'black'})

    # print({v: 'black'})
    self.dfs_timer += 1

    return discover


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
            temp = {}
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

    def dfs_on_graph(self):

        # print(self.adj_dict)
        vertex_color = {}
        for i, v in enumerate(self.vertices):
            # print(v, self.matrix[i])
            vertex_color.update({v: 'white'})
        # print(vertex_color)
        discover = []

        for i, v in enumerate(self.vertices):
            if vertex_color.get(v) == 'white':
                # print('white')
                discover = dfs_visit(v, vertex_color, self, discover)

        print('discovered in order')
        print(discover)
        # print(finish)
        # for i, v in enumerate(self.vertices):
        #     print(v, vertex_color.get(v))


def main():
    # Thoroughly test your program and produce useful output.

    graph = Graph(['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
                  [('q', 's', 1),
                   ('s', 'v', 1),
                   ('v', 'w', 1),
                   ('w', 's', 1),
                   ('q', 'w', 1),
                   ('q', 't', 1),
                   ('t', 'x', 1),
                   ('x', 'z', 1),
                   ('z', 'x', 1),
                   ('t', 'y', 1),
                   ('y', 'q', 1),
                   ('r', 'y', 1),
                   ('r', 'u', 1),
                   ('u', 'y', 1)])
    graph.display()
    graph.dfs_on_graph()


if __name__ == '__main__':
    main()
