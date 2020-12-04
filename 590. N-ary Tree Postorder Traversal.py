class Node():

    def __init__(self, val):
        self.val = val
        # all children are stored in a list
        self.children = []



def postorder(root):
    res = []
    if root == None: return res

    stack = [root]
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        stack.extend(curr.children)

    return res[::-1]

# Execution Start From here
if __name__ == '__main__':
    # input nodes
    '''

      1
   /  |  \
  /   |   \
 2    3    4
/ \      / | \
/   \    7  8  9
5     6    
/    / | \ 
10   11 12 13

    '''

root = Node(1)
root.children.append(Node(2))
root.children.append(Node(3))
root.children.append(Node(4))
root.children[0].children.append(Node(5))
root.children[0].children[0].children.append(Node(10))
root.children[0].children.append(Node(6))
root.children[0].children[1].children.append(Node(11))
root.children[0].children[1].children.append(Node(12))
root.children[0].children[1].children.append(Node(13))
root.children[2].children.append(Node(7))
root.children[2].children.append(Node(8))
root.children[2].children.append(Node(9))

#preorderTraversal(root)
print(postorder(root))