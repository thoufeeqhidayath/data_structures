from data_structures.binary_tree.binary_tree_implementation import BinaryTree
from queue import Queue


"""
   breadth wise search on the tree
   time complexity - 0(n)
   space complexity - 0(n)
"""

def breasth_first_search(root):
    queue = Queue([root])
    values = []
    while queue and not queue.is_empty():
        item = queue.dequeue()
        values.append(item.root)
        if item.left:
            queue.enqueue(item.left)
        if item.right:
            queue.enqueue(item.right)
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
# depth_first_search(a)
breasth_first_search(a)