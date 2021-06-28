class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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

        l3=l3.next
        return l3 
