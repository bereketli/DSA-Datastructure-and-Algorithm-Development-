# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            dummy = ListNode(None)
            dummy.next = head
            left, right = dummy, dummy
            count,tempo = {}, head
            while tempo != None:
                if tempo.val not in count:
                    count[tempo.val] = 1
                else:
                    count[tempo.val] += 1
                tempo= tempo.next
            
            while right.next != None:
                if count[right.next.val] == 1:
                    right = right.next
                    left.next = right
                    left = right
                    continue
                right = right.next
            
            if count[right.val] != 1 :
                left.next = right.next
            return dummy.next
                
