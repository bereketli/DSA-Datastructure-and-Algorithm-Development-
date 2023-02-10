# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:       
        if head is not None:
            self.dummy = ListNode(None)
            temp = head 
            while temp.next is not None:
                 wasFirst = self.dummy.next
                 newNext = temp.next
                 temp.next = wasFirst
                 self.dummy.next = temp
                 temp = newNext
            wasFirst = self.dummy.next
            temp.next = wasFirst
            self.dummy.next = temp
            return self.dummy.next
            
        else:
            return head
        