# https://www.youtube.com/watch?v=XHx4OQ5BLoE
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack=[]
        prev=TreeNode(-float("INF"))
        abnormal=[]
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            temp=stack.pop()            
            if prev.val>temp.val:
                abnormal.append((prev,temp))
            prev=temp
            root=temp.right       
        if len(abnormal)==1:
            prev, temp=abnormal[0]
            abnormal[0][0].val, abnormal[0][1].val=abnormal[0][1].val, abnormal[0][0].val
        else:           
            abnormal[0][0].val, abnormal[1][1].val=abnormal[1][1].val, abnormal[0][0].val
            
            
            
            
