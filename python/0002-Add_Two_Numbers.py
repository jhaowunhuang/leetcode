# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.val = None

    def addTwoNumbers(l1, l2):
        ans = node = ListNode(0)
        a = 0
        while l1 or l2 or a:
            if l1:
                a += l1.val
                l1 = l1.next
            if l2:
                a += l2.val
                l2 = l2.next
            a, b = divmod(a, 10)
            node.next = ListNode(b)
            node = node.next
        return ans.next
