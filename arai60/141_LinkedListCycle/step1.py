from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# It took me about 20 min to come up with this solution.
# it gets the first few test cases right, but it times out during the submission.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        seen_dic = {head.val: head.next}
        current_node = head.next
        while current_node is not None:
            next_node = current_node.next
            if (current_node.val in seen_dic) and (
                seen_dic[current_node.val] == next_node
            ):
                return True
            seen_dic[current_node.val] = next_node
            current_node = next_node
        return False
