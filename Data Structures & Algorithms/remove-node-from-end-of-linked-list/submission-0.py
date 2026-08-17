# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or (n == 1 and head.next is None):
            return None

        curr = head
        total = 0
        while curr is not None:
            total += 1
            curr = curr.next

        i = 0
        curr = head
        prev = head
        while curr is not None:
            if total - i == n:
                break
            i += 1
            prev = curr
            curr = curr.next

        if curr == prev:
            head = head.next
            return head

        prev.next = curr.next
        return head