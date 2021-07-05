# no refernce was used
# the idea is same as level order traverse 
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        level=[root]
        nLevel=[]
        while level !=[]:
            for i in range(len(level)-1):
                level[i].next=level[i+1]
                if level[i].left != None:
                    nLevel.append(level[i].left)
                if level[i].right != None:
                    nLevel.append(level[i].right)
                    
            level[-1].next=None
            if level[-1].left != None:
                    nLevel.append(level[-1].left)
            if level[-1].right != None:
                    nLevel.append(level[-1].right)
            level=nLevel
            nLevel=[]
        return root
        
            
        
