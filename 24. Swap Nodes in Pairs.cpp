/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {

    ListNode* cur=head;   
    ListNode *prev=new ListNode();    
    prev->next=head;    
    ListNode *dummy=new ListNode();
    dummy=prev;     
    while (cur!=NULL and cur->next!=NULL ){
        ListNode* temp=cur;
        ListNode* nextPair=cur->next->next;       
        prev->next=cur->next;
        cur->next->next=temp;
        temp->next=nextPair;
        prev=temp;
        cur=nextPair;      
    }        
     return (dummy->next);   
    }
};
