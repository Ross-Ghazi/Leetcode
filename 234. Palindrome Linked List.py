#No ref was used
# find the midle and reverse it from there
#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head==None or head.next==None:
                          return True

        l=0
        cur1=head
        while cur1!=None:
            l+=1
            cur1=cur1.next
            
        mid=l//2
        cur1=head
        
        prev=None
        for i in range(mid):
            temp=cur1.next
            cur1.next=prev
            prev=cur1
            cur1=temp
            
        head2=temp  
        head1=prev
        if l%2==1:
            head2=head2.next        
        cur1=head1
        cur2=head2  
        while cur1 !=None:
            if cur1.val != cur2.val:
                return False
            cur1=cur1.next
            cur2=cur2.next
        return True
        
        
        
