# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visitedNode = set()
        tempo = head
        while tempo:
            if tempo not in visitedNode:
                visitedNode.add(tempo)
            else:
                return tempo
            tempo = tempo.next
        print("eth")
        return None
