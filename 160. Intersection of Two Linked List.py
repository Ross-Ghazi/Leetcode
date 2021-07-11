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
