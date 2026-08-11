# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = fast = head
        fast = slow.next
        while slow is not None and fast is not None:
            if slow == fast:
                return True

            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                fast = None

        return False   