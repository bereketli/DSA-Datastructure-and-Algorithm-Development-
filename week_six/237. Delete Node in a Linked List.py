# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        tempo = node
        while tempo.next.next is not None:
            tempo.val = tempo.next.val
            tempo = tempo.next
        tempo.val = tempo.next.val
        tempo.next = None
        
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
