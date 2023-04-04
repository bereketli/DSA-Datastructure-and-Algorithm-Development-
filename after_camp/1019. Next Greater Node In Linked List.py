# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        length = 0
        tempo = head
        while tempo:
            length += 1
            tempo = tempo.next
        output = [0] * length
        tempo = head 
        mono_stack = []
        i = 0
        while tempo:

            while mono_stack and mono_stack[-1][1] < tempo.val:
                popped = mono_stack.pop()
                output[popped[0]] = tempo.val
            mono_stack.append([i, tempo.val])
            tempo = tempo.next
            i += 1
        return output

                  
