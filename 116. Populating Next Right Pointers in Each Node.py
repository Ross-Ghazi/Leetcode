# no refernce was used
# the idea is same as level order traverse 

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root==None:
            return None
        stack=[root]
        while stack!=[]:
            newLevel=[]
            for item in stack[::-1]:
                if item.left!=None:
                    newLevel.append(item.left)            
                if item.right!=None:
                    newLevel.append(item.right)           
            while stack!=[]:               
                temp=stack.pop()               
                if len(stack)>=1:
                    temp.next=stack[-1]
                else:
                    temp.next=None
            stack=newLevel[::-1]
        
        return root
                

# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if root is None:
#             return None
#         level=[root]
#         nLevel=[]
#         while level !=[]:
#             for i in range(len(level)-1):
#                 level[i].next=level[i+1]
#                 if level[i].left != None:
#                     nLevel.append(level[i].left)
#                 if level[i].right != None:
#                     nLevel.append(level[i].right)
                    
#             level[-1].next=None
#             if level[-1].left != None:
#                     nLevel.append(level[-1].left)
#             if level[-1].right != None:
#                     nLevel.append(level[-1].right)
#             level=nLevel
#             nLevel=[]
#         return root
        
            
        
