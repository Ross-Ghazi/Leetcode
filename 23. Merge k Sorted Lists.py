# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def merge2list(l1,l2):
            l3=ListNode()
            temp=l3
            while l1 and l2:
                if l1.val<=l2.val:
                    temp.next=l1
                    l1=l1.next
                else:
                    temp.next=l2
                    l2=l2.next
                temp=temp.next
        
            if l1:
                temp.next=l1
            else:
                temp.next=l2
            return l3.next  
   
        if len(lists)==0:
            return None       
        while len(lists)>1:
            newList=[]
            while len(lists)>1:                          
                l1=lists.pop()
                l2=lists.pop()
                newList.append(merge2list(l1,l2))   
            lists.extend(newList)             
        return lists.pop()    
