# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tempo = head
        while tempo:
            if tempo.val == "num":
                return True
            tempo.val = "num"
            tempo = tempo.next
        return False
