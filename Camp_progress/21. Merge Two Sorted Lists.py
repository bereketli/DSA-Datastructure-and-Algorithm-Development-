# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode(None)
        tempoMerged = merged
        tempo1 = list1
        tempo2 = list2
        while tempo1 is not None and tempo2 is not None:
            if tempo1.val < tempo2.val:
                tempoMerged.next = tempo1
                tempo1 = tempo1.next
            else:
                tempoMerged.next = tempo2
                tempo2 = tempo2.next
            tempoMerged = tempoMerged.next
        tempoMerged.next = tempo1 if tempo1 is not None  else tempo2
        return merged.next
