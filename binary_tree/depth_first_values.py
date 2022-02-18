from data_structures.binary_tree.binary_tree_implementation import BinaryTree
from stack import Stack


def depth_first_search(root):

    stack = Stack([root])
    values = []
    while stack :
        item = stack.pop()
        values.append(item.root)
        if item.right:
            stack.push(item.right)
        if item.left:
            stack.push(item.left)
    print(values)

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
depth_first_search(a)