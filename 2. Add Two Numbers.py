#2. Add Two Numbers , Leetcode
# Dec 11, 2020
#By Rouzbeh



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



    def addTwoNumbers(self, l1, l2):
        res=ListNode()
        temp=ListNode()
        carry=0
        res=temp
        while l1 or l2 or carry==1:
            temp.next=ListNode(l1.val+l2.val+carry)
            if temp.next.val>9:
                carry=1
                temp.next.val-=10
            else:
                carry=0
            l1=l1.next
            l2=l2.next
            temp=temp.next

        return res.next











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

