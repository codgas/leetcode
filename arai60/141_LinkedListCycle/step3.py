from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # declare the two pointers slow and fast to the head
        slow = head
        fast = head
        # since fast is moving twice as fast as slow, if there is a cycle, they will meet at some point
        # we check fast and fast.next because fast.next.next will throw an error if fast.next is None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False
