class AdjacencyList(object):
    def __init__(self):
        self.List = {}

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.List.keys():
            self.List[from_vertex].append(to_vertex)
        else:
            self.List[from_vertex] = [to_vertex]

    def print_list(self):
        for i in self.List:
            print(i, '->', ' -> '.join([str(j) for j in self.List[i]]))

al = AdjacencyList()
al.add_edge(0, 1)
al.add_edge(0, 4)
al.add_edge(4, 1)
al.add_edge(4, 3)
al.add_edge(1, 0)
al.add_edge(1, 4)
al.add_edge(1, 3)
al.add_edge(1, 2)
al.add_edge(2, 3)
al.add_edge(3, 4)

al.print_list()
