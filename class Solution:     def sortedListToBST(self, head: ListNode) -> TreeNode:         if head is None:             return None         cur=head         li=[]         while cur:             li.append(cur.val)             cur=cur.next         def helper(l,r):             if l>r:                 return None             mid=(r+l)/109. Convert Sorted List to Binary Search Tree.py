# used 108 leetocde idea 
#https://www.youtube.com/watch?v=0K0uCMYq5ng&ab_channel=NeetCode

#https://www.youtube.com/watch?v=FnDth46DAMI&ab_channel=HappyCoding
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        cur=head
        li=[]
        while cur:
            li.append(cur.val)
            cur=cur.next
        def helper(l,r):
            if l>r:
                return None
            mid=(r+l)//2
            root=TreeNode(li[mid])
            root.left=helper(l,mid-1)
            root.right=helper(mid+1,r)
            return root
        return helper(0,len(li)-1)
            
        
