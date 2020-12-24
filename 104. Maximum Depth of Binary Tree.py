# 104. Maximum Depth of Binary Tree
# no reference was used.
# Here are list of my bugs:
# did not call dfs on the main function
# call dfs but without return
# had right = 1 + dfs(root.left) rather than root.right

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # recursive
    def maxDepth(self,root):
        def dfs(root):
            if root == None:
                return 0
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            return (max(left, right))
        return dfs (root)


    # iterative
    def maxDepth2(self,root):
        if root==None:
            return 0
        m=0
        stack=[root]
        stack_counter=[1]
        while stack!=[]:
            temp=stack.pop()
            counter=stack_counter.pop()
            m=max(counter,m)
            if temp.left !=None:
                stack.append(temp.left)
                stack_counter.append(counter+1)
            if temp.right !=None:
                stack.append(temp.right)
                stack_counter.append(counter+1)

        return m






"""
                3
              /    \
            9       20
                   /  \
                  15    7
"""
node=Node(3)
node.left = Node(9)
node.right = Node(20)
node.right.left= Node(15)
node.right.right= Node(7)
print(node.maxDepth(node))

node1=Node(1)
node1.right = Node(2)
print(node.maxDepth2(node))






