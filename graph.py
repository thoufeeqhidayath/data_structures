
class Node:
    def __init__(self,name:str):
        self.name = name

    def __repr__(self):
        return self.name

class Edge:
    def __init__(self,from_:str,to_:str,weight =0):
        self.from_ = from_
        self.to = to_
        self.weight = weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight


    def __repr__(self):
        return str(self.from_) +"->" +str(self.to)

class Graph:
    def __init__(self):
        self.node = {}
        self.edges = {}

    def add_node(self,node):
        if node not in self.node:
            self.node[node] =Node(node)

    def add_edges(self,from_,to_,weight=0):
        if (from_,to_) not in self.edges:
            if from_ not in self.node:
                self.add_node(from_)
            if to_ not in self.node:
                self.add_node(to_)

            from_node = self.node[from_]
            to_node   = self.node[to_]
            edge =Edge(from_node,to_node,weight)
        else:
            edge = self.edges.get(from_,to_)
            edge.weight = weight

        self.edges[(from_,to_)] =edge

    def get_edges_in_sorted_order(self):
        edges = list(self.edges.values())
        edges = sorted(edges)
        return edges



    def __repr__(self):
        return str(self.edges)

# g =Graph()
# g.add_edges("a","b",2)
# g.add_edges("b","c",1)
# print(g)
# print(len(g.get_edges_in_sorted_order()))


