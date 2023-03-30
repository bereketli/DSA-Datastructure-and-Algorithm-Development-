# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        tempo = head
        maximum,count, i = 0, 1,0
        first_half = []
        while tempo.next != None:
            count += 1
            tempo = tempo.next
        half = count // 2
        tempo = head
        while tempo != None:
            if i < half:
                first_half.append(tempo.val)
            else:
                maximum = max(maximum, first_half[-1] + tempo.val)
                first_half.pop()
            tempo = tempo.next
            i += 1
        return maximum
