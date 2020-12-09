"""
589. N-ary Tree Preorder Traversal

"""

"""
below is not working since using mutable defult argument will  mess the program
class Node(object):
    def __init__(self, val=None,children=[]):
                self.val = val                
                self.children = children

"""

class Node(object):
    def __init__(self, val=None,children=None):
                self.val = val
                self.children= children

    def add_child(self, node):
        if self.children==None:
            self.children=[]
        self.children.append(node)

    def preorder(self, root):
        res=[]
        def DFS(node):
            if not node:return
            res.append(node.val)
            # in my code if I do not have this line
            # it will fai, but for some reason (?) it will not fail on Leetcode
            if node.children is None: return
            for item in node.children:
                DFS(item)
        DFS(root)
        return res

"""
                1
            /    |    \
           3     2     1
         /   \
         5    6            
"""
node=Node(1)
child=Node(3)
node.add_child(child)
child=Node(2)
node.add_child(child)
child=Node(1)
node.add_child(child)
child=Node(5)
node.children[0].add_child(child)
child=Node(6)
node.children[0].add_child(child)

a=node.preorder(node)
print(a)


