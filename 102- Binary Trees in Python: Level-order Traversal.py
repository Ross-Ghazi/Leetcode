""""
update on June 21, 2021
Rouzbeh

1. The fiest way is from below link with explanining the detail
https://www.youtube.com/watch?v=MBZ-gBkjdMc&list=PL2b9acjRfGcm4qYq5MH9LufsJ67-BgkAI&index=4&ab_channel=DEEPTITALESRA


2. Alternative way which uses list comprehension and it is better but harder to understand:
https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)


3. If you want more info about how to make binary tree
https://github.com/vprusso/youtube_tutorials/blob/master/data_structures/trees/binary_trees/level_order_traversal.py
https://www.youtube.com/watch?v=aM-oswPn19o&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=35&ab_channel=LucidProgramming


"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def levelOrder(self, root):
        Q=[root]
        NextQ=[]
        level=[]
        result=[]
        if root==None: return []
        while Q:
            for node in Q:
                level.append(node.val)
                if node.left is not None:
                  NextQ.append(node.left)
                if node.right is not None:
                  NextQ.append(node.right)
            result.append(level)
            Q=NextQ
            NextQ=[]
            level=[]

        return result

    def levelOrder_alter(self, root):
            ans, level = [], [root]
            while root and level:
                ans.append([node.val for node in level])
                level = [kid for node in level for kid in[node.left, node.right] if kid]
            return ans

    def levelOrderReverse(self, root):
            ans, level = [], [root]
            while root and level:
                ans.append([node.val for node in level])
                level = [kid for node in level for kid \
                         in[node.left, node.right] if kid]
            ans.reverse()
            return ans


"""

                1
              /    \
            2       3
          /  \     /  \
          4   5   6    7



"""
node=Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left= Node(6)
node.right.right= Node(7)





print(node.levelOrder(node))
print(node.levelOrder_alter(node))
print(node.levelOrderReverse(node))






