"""
https://www.youtube.com/watch?v=5Y2EiZST97Y&ab_channel=NeetCode

"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        table={}
        cur=head
        while cur !=None:
            table[cur]=Node(cur.val)
            
            cur=cur.next
        
        cur=head
        while cur !=None:
            if cur.next != None:            
                table[cur].next=table[cur.next]
            if cur.random != None:
                table[cur].random=table[cur.random]
            cur=cur.next
            
        return table[head]
       
