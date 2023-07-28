# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        temp = ListNode(0)
        l3 = temp
        carry = 0

        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            _sum = val1 + val2 + carry
            carry = _sum // 10
            l_digit = _sum % 10

            new_node = ListNode(l_digit)
            l3.next = new_node

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            l3 = l3.next

        if carry > 0:
            node = ListNode(carry)
            l3.next = node
            l3 = l3.next

        return temp.next
