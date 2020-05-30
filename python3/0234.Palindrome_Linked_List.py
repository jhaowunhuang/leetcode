# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        fast = slow = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, rev, slow = rev, slow, slow.next
        if fast:
            slow = slow.next
        while slow:
            if rev.val != slow.val:
                return False
            slow, rev = slow.next, rev.next
        return True
