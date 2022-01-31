# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
            if headA==None or headB==None:
                return None
            dic=set()
            cur=headA
            while cur!=None:
                dic.add(cur)
                cur=cur.next
            cur=headB
            while cur!=None:
                if cur not in dic:
                    cur=cur.next
                else:
                    return cur
            
            return None

#     or 
#     class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         cur1=headA
#         cur2=headB
#         set1=set()
#         set2=set()
#         while cur1 or cur2:
#             if cur1:
#                 if cur1 in set2:
#                     return cur1
#                 set1.add(cur1)
#                 cur1=cur1.next
            
#             if cur2:
#                 if cur2 in set1:
#                     return cur2
#                 set2.add(cur2)
#                 cur2=cur2.next
        
#         return None
