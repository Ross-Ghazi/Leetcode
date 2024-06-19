class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head     
        prev=None
        cur=head       
        while cur:
            Next=cur.next 
            cur.next=prev 
            prev=cur
            cur=Next
        return prev

