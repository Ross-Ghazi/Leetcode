class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        stack=[root]
        Round=0  
        res=[]
        while stack:
            newStack=[]
            reslevel=[]
            for node in stack:
                reslevel.append(node.val)
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
            if Round%2:
                reslevel.reverse()
            res.append(reslevel)
            stack=newStack
            Round+=1
        return res
            
                    
                    


""""
Dec 6,2020


look at 102 level order to get this one
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def zigzagLevelOrder(self, root):
        Q=[root]
        NextQ=[]
        level=[]
        result=[]
        flag = 1
        if root==None: return []
        while Q:
            for node in Q:
                    level.append(node.val)
                    if node.left is not None:
                      NextQ.append(node.left)
                    if node.right is not None:
                      NextQ.append(node.right)
            if flag==-1: level.reverse()
            flag=flag*-1

            result.append(level)
            Q=NextQ
            NextQ=[]
            level=[]

        return result



"""

                1
              /    \
            2       3
          /  \     /  \
          4   5   6    7




node=Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left= Node(6)
node.right.right= Node(7)
"""
node=Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)




print(node.zigzagLevelOrder(node))






