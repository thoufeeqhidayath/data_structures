
"""
       a
      / \
      b c
     /\
     d e
     binary tree have one left and right children
     leaf - is the last node (d,e)
     root -is the first node (a) where there is no parent linked

"""


class BinaryTree1:
    def __init__(self,root_obj):
        self.root = root_obj
        self.left = None
        self.right = None

    def insert(self,value):
        if self.left ==None:
            self.left = BinaryTree1(value)
        elif self.right ==None:
            self.right = BinaryTree(value)



class BinaryTree:
    def __init__(self,root_obj):
        self.root = root_obj
        self.right = None
        self.left = None

    def insert_at_right(self ,val):
        if self.right is None:
            self.right = BinaryTree(val)
        if self.right:
            self.right.right =BinaryTree(val)

    def insert_at_left(self,val):
        if self.left is None:
            self.left = BinaryTree(val)
        if self.left:
            self.left.left = BinaryTree(val)

    def get_root(self,):
        return self.root

a = BinaryTree('a')
b = BinaryTree('b')
c = BinaryTree('c')
d = BinaryTree('d')
e = BinaryTree('e')
f = BinaryTree('f')
a.left = b
a.right =c
b.left =d
b.right =e
c.left =f


