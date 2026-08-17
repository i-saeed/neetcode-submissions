# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        # find middle point linkedlists
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        # reverse the second linked list
        prev = None
        while head2 is not None:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp

        head2 = prev

        # merged 2 linked lists
        node1 = head
        node2 = head2
        while node1 is not None and node2 is not None:
            temp1 = node1.next
            temp2 = node2.next
            node1.next = node2
            node2.next = temp1
            node1 = temp1
            node2 = temp2