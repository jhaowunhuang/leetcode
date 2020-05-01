# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        node1 = node2 = head
        while node1.next:
            node1 = node1.next
            if node1.val != node2.val:
                node2.next = node1
                node2 = node2.next
        node2.next = None
        return head
