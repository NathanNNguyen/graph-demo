class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('nonexistent vertex')

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


g = Graph()

g.add_vertex(1)
g.add_vertex(2)

g.add_edges(1, 2)

print(g.vertices)
