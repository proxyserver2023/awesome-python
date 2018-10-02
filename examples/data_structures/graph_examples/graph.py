class Node(object):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_name(obj):
        if isinstance(obj, Node):
            return obj.name
        elif isinstance(obj, str):
            return obj
        return ""

    def __eq__(self, obj):
        return self.name == self.get_name(obj)

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __ne__(self, obj):
        return self.name != self.get_name(obj)

    def __lt__(self, other):
        return self.name < self.get_name(other)

    def __le__(self, other):
        return self.name <= self.get_name(other)

    def __gt__(self, other):
        return self.name > self.get_name(other)

    def __ge__(self, other):
        return self.name >= self.get_name(other)

    def __bool__(self):
        return self.name


class DirectedEdge(object):
    def __init__(self, node_from, node_to):
        self.nf = node_from
        self.nt = node_to

    def __eq__(self, other):
        if isinstance(other, DirectedEdge):
            return self.nf == other.nf and self.nt == other.nt
        return False

    def __repr__(self):
        return (f'{self.nf} -> {self.nt}')


class DirectedGraph(object):
    def __init__(self, vertices={}):
        self.nodes = []
        self.edges = []
        self.direction = []

        if vertices and type(vertices) == dict:
            for v in vertices:
                node_from = self.add_node(v)
                self.direction[v] = []

                for w in vertices[v]:
                    node_to = self.add_node(w)
                    self.direction[node_from].append(node_to)
                    self.add_edge(v, w)


    def add_node(self, node_name):
        pass


    def add_edge(self, node_from, node_to):
        pass

class Graph:
    pass
