from kruskal_algorith.dijoint_set import DisjointSet
from kruskal_algorith.graph import Graph


class KruskalAlgorithm:
    def __init__(self,graph:Graph):
        self.graph = graph
        self.mst = []



    def execute(self):
        i,e = 0,0
        disjoint_set = DisjointSet(self.graph.node)
        sorted_edges = self.graph.get_edges_in_sorted_order()
        while e<len(self.graph.node)-1:
            edge = sorted_edges[i]
            print("___________________")
            print(edge.from_.name,edge.to.name)
            print("value of x")
            x_root=disjoint_set.find(edge.from_.name)
            print("xroot : ",x_root)
            print("value of y")
            y_root =disjoint_set.find(edge.to.name)
            print("yroot : ", y_root)
            print(x_root,y_root)
            i=i+1
            if x_root!=y_root:
                e =e+1
                disjoint_set.union(edge.from_.name,edge.to.name)
                print(disjoint_set.parent)
                self.mst.append([edge.from_.name,edge.to.name,edge.weight])
        print(self.mst)


g =Graph()
g.add_edges("a","b",1)
g.add_edges("a","c",2)
g.add_edges("b","c",2)
g.add_edges("b","d",6)
g.add_edges("b","e",5)
g.add_edges("c","d",3)
g.add_edges("d","e",2)
k =KruskalAlgorithm(g)
k.execute()