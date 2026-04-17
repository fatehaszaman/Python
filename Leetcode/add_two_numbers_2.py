# LeetCode #2 — Add Two Numbers
# Time: O(max(m, n))  — traverse both lists to their full length
# Space: O(max(m, n)) — result list has at most max(m,n)+1 nodes


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time: O(max(m, n)) | Space: O(max(m, n))
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10

        return dummy.next
