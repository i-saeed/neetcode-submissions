# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def _merge_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if list1 is None and list2 is None:
        return None
    elif list1 is None:
        return list2
    elif list2 is None:
        return list1

    node1 = list1
    node2 = list2
    prev = None
    curr = None
    head = None

    while node1 is not None and node2 is not None:
        if node1.val <= node2.val:
            curr = node1
            node1 = node1.next
        else:
            curr = node2
            node2 = node2.next

        if prev is not None:
            prev.next = curr
        else:
            head = curr

        prev = curr

    if node1 is None:
        curr.next = node2
    else:
        curr.next = node1

    return head

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or lists[0] is None or not lists[0]:
            return None

        n = len(lists)

        if n <= 1:
            return lists[0]

        mid_point = n // 2
        left_lists = self.mergeKLists(lists[0:mid_point])
        right_lists = self.mergeKLists(lists[mid_point:n])

        merged_head = _merge_lists(left_lists, right_lists)
        return merged_head       