# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            dummy = ListNode(None)
            dummy.next = head
            left, right = dummy, head
            while right.next != None:
                if left.val != right.val:
                    left.next = right
                    left = right
                right = right.next
            if left.val == right.val:
                left.next = right.next
            else:
                left.next = right

            return dummy.next
