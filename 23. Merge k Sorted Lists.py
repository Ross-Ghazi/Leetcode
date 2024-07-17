class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        def merge(l1,l2):           
            cur1=l1
            cur2=l2
            dummy=ListNode()
            cur=dummy
            while cur1 or cur2:
                if cur1 and cur2:
                    if cur1.val<cur2.val:
                        cur.next=cur1
                        cur1=cur1.next
                    else:
                        cur.next=cur2
                        cur2=cur2.next                
                elif cur1:
                    cur.next=cur1
                    cur1=cur1.next
                else:
                    cur.next=cur2
                    cur2=cur2.next
                cur=cur.next
            return dummy.next      
       
        q=collections.deque(lists)
        while len(q)>1:
            l1=q.popleft()
            l2=q.popleft()
            l3=merge(l1,l2)            
            q.appendleft(l3)
        res=q.pop()
        return res
        
