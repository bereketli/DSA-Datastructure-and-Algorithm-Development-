# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(mid):
            if not mid or not mid.next:
                return mid

            temp = mid
            temp_fast = mid
            prev = mid
            while temp_fast and temp_fast.next :
                temp_fast = temp_fast.next.next
                prev = temp
                temp = temp.next
            half = prev.next
            prev.next = None

            
            left = mergeSort(mid)
            right = mergeSort(half)
           
            return merge(left, right)
        def merge(left, right):
            dummy = ListNode(None)
            tempo = dummy

            while left and right:
                if left.val <= right.val:
                    tempo.next = left
                    left = left.next
                else:
                    tempo.next = right
                    right = right.next
                tempo = tempo.next
            if left:
                tempo.next = left
            elif right:
                tempo.next = right
           
            return dummy.next

            return dummy.next
        return mergeSort(head)
        
