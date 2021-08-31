
# The list node is based on leetcode structure which does not
# have any head.

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







llist = ListNode("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("E")
#########
llist.print_list()

