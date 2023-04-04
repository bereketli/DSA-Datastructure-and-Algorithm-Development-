# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array_nums = []
        tempo = head
        while tempo.next is not None:
            array_nums.append(tempo.val)
            tempo = tempo.next
        array_nums.append(tempo.val)
        half = int(len(array_nums)/2)
        for i in range(half):
            if array_nums[i] != array_nums[len(array_nums) - 1 - i]:
                return False
        return True
        
