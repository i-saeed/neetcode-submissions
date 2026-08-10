# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node_1 = list1
        node_2 = list2
        h = None
        p = None
        node = None
        end_loop = False
        while node_1 is not None or node_2 is not None:
            if node_1 is None:
                node = node_2
                end_loop = True
            elif node_2 is None:
                node = node_1
                end_loop = True
            else:
                if node_1.val < node_2.val:
                    node = node_1
                    node_1 = node_1.next
                else:
                    node = node_2
                    node_2 = node_2.next

            if h is None:
                h = node

            if p is not None:
                p.next = node

            p = node

            if end_loop:
                break

        return h