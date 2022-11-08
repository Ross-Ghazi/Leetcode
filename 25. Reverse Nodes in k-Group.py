# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def findKth(root):
            for i in range(k):
                if root:
                    root=root.next
            return root
        dummy=ListNode()
        dummy.next=head
        prevGroupEnd=dummy
        while True:            
            Kth=findKth(prevGroupEnd)
            if not Kth:
                break            
            nextGroupStart=Kth.next
            prev=None
            cur=prevGroupEnd.next
            for i in range (k):
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
            prevGroupEnd_temp=prevGroupEnd.next
            prevGroupEnd.next.next=nextGroupStart
            prevGroupEnd.next=prev
            prevGroupEnd=prevGroupEnd_temp           
        
        return dummy.next
        
        
