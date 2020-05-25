# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        ans = ListNode(0)
        node = ans
        while head:
            if head.val != val:
                node.next = head
                node = node.next
            head = head.next
        node.next = head
        return ans.next
