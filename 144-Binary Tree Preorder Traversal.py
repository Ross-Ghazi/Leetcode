""""
Dec 6,2020

https://www.youtube.com/watch?v=pUSy6UZCFKw&t=709s&ab_channel=DEEPTITALESRA


"""
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def preorderTraversal_recursive(self, root):
        if root is None :
            return []
        return [root.val]+\
               self.preorderTraversal_recursive(root.left)+ \
               self.preorderTraversal_recursive(root.right)

    def preorderTraversal_iterative(self, root):
        if root is None :
            return []
        stack=[root]
        res=[]
        while stack != []:
            temp=stack.pop()
            res.append(temp.val)
            if temp.right is not None:
                stack.append(temp.right)
            if temp.left is not None:
                stack.append(temp.left)
        return res

"""

                1
              /    \
            2       3
          /  \     /  \
          4   5   6    7
          
     pre oder =[1,2,4,5,3,6,7]
     in-order=[4,2,5,1,3,6,7]



"""


node=Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left= Node(6)
node.right.right= Node(7)
print(node.preorderTraversal_iterative(node))

