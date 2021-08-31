#2. Add Two Numbers , Leetcode
# Dec 11, 2020




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, val):
        new_node = ListNode(val)

        last_node = self
        while last_node.next:
            last_node= last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self
        while cur_node:
            print(cur_node.val)
            cur_node = cur_node.next

    def prepend(self, val):
        tempNext=self.next
        tempval=self.val
        self.val=val
        newNode=ListNode(tempval)
        newNode.next = tempNext
        self.next=newNode



    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode()
        head=l3
        carry=0
        while l1 or l2 or carry !=0:
            num=carry
            if l1:
                num+=l1.val
                l1=l1.next
            if l2:
                num+=l2.val
                l2=l2.next
            if num<10:
                carry=0
            else:
                carry=1
                num-=10                
            l3.next=ListNode(num)
            l3=l3.next
        return head.next










l1 = ListNode(2)
l1.append(4)
l1.append(3)
l2=ListNode(5)
l2.append(6)
l2.append(4)
#########
a=ListNode()
a=a.addTwoNumbers(l1,l2)
a.print_list()

