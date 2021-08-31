""""
Dec 6,2020

https://www.youtube.com/watch?v=RJhh3Jcc9zw&ab_channel=DEEPTITALESRA

"""
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def InorderTraversal_recursive(self, root):
        if root is None :
            return []
        return self.InorderTraversal_recursive(root.left)+ \
               [root.val] + \
               self.InorderTraversal_recursive(root.right)

    def InorderTraversal_iterative(self, root):

        result=[]
        stack=[]
        while stack != [] or root is  not None:
            while root is not None:
                stack.append(root)
                root=root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
"""
                1
              /    \
            2       3
          /  \     /  \
          4   5   6    7

InorderTraversal_recursive:
[4 2 5 1 6 3 7]

"""


node=Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left= Node(6)
node.right.right= Node(7)



#print(node.InorderTraversal_recursive(node))
print(node.InorderTraversal_iterative(node))

