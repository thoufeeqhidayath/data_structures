
class DisjointSet:
    def __init__(self,vertices):
        self.vertices = vertices
        self.parent = {}

        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(self.vertices,0)


    def find(self,node):
        # print(self.parent)
        # print(type(node))
        return self.parent[node]
        # if self.parent[node] == node:
        #     return node
        # else:
        #     self.find(self.parent[node])
        # return node



    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.rank[x_root]>self.rank[y_root]:
            self.parent[y_root] = x_root
        elif self.rank[y_root] > self.rank[x_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] = self.rank[x_root] +1

    def __repr__(self):
        return str(self.parent)

# d =DisjointSet(["a","b","c"])
# d.union("a","b")
# d.union("b","c")
# print(d)
