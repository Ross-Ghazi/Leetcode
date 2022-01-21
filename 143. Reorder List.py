from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head==None:
            return None
        cur=head
        q=deque()
        while cur!= None:
            q.append(cur)
            cur=cur.next
        cur=q.popleft()        
        while len(q)>0:
            temp=q.pop()
            cur.next=temp
            cur=cur.next
            if len(q)>0:
                temp=q.popleft()   
                cur.next=temp
                cur=cur.next 
        cur.next=None
                
            
