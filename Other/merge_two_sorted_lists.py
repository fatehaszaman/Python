# Merge Two Sorted Linked Lists — return a new sorted merged list
# Time: O(m + n)  — traverse both lists exactly once
# Space: O(1)     — re-links existing nodes, only one dummy node allocated


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(m + n) | Space: O(1)
def merge_two_lists(l1, l2):
    result = ListNode()   # dummy head
    tail = result
    while l1 and l2:
        if l1.val < l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2   # attach remainder
    return result.next
