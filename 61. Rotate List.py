# no refernce was used
# first find length. then notice that k rotation is same as k%l rotation. 
# this  is good refernce just in case: https://www.youtube.com/watch?v=fqZYZK3OCXQ&ab_channel=SaiAnishMalla
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head is None:
            return
            
        counter=0
        temp=head       
        
        while temp !=None:        
            temp=temp.next
            counter+=1
        l=counter
        k=k%l
        if k==0:
            return head 
        temp=head       
        for counter in range(1,l-k):
          temp=temp.next
        
        head2=temp.next
        temp.next=None
        temp=head2
        
        while temp.next !=None:
            temp=temp.next
        temp.next=head
       
        
        
        
        return head2
                
