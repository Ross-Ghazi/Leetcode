# 236. Lowest Common Ancestor of a Binary Tree
#By Rouzbeh on Dec 11,2020
# No source was used. IT is running fine on PC but for the same example it will give error on Leetcode.


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

    def lowestCommonAncestor(self,root, p,q):
        parents={}
        def dfs(node):
            if node is None:
                return
            if node.left:
                parents[node.left.val]=node.val
                dfs(node.left)
            if node.right:
                parents[node.right.val] = node.val
                dfs(node.right)

        dfs(root)
        parentP =[]
        key=p
        while key in parents:
            parentP.append(parents[key])
            key=parents[key]

        parentQ = []
        key = q
        while key in parents:
            parentQ.append(parents[key])
            key = parents[key]

        if p in parentQ:
            return p
        if q in parentP:
            return q

        for item in parentP:
           if item in parentQ:
               return item
""""
                3
              /    \
            5       1
          /  \     /  \
          6   2   0    8
             / \
             7   4
"""
node=Node(3)
node.left = Node(5)
node.right = Node(1)
node.left.left = Node(6)
node.left.right = Node(2)
node.left.right.left=Node(7)
node.left.right.right=Node(4)
node.right.left= Node(0)
node.right.right= Node(8)


print(node.lowestCommonAncestor(node,1,5))