# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #prev-->p-->q-->Next  to 
        #prev-->q-->p-->Next
        cur=head        
        prev=ListNode()
        head1=prev
        while cur:
            if cur.next:
                p=cur
                q=cur.next
                Next=q.next
                prev.next=q                
                q.next=p
                p.next=Next
                cur=Next
                prev=p 
            else:
                prev.next=cur
                cur=cur.next        
        return head1.next
