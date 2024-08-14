# 問題概要

問題: 141. Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/description/

言語: Python

# Step1

かかった時間：20min

思考ログ：

- Linked を思い出すところから始めました。どこか勉強した覚えがあったが、業務でも今までも出たことなかった。

- memorization のようなやり方でやろうと思いましたが、タイムオーバーになってしまう。

```python
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


```

疑問点：

- 問題を理解するのに、10 分ぐらいかかりました。

- 勉強用 link: https://www.geeksforgeeks.org/linked-list-data-structure/

# Step2

かかった時間：20min

思考ログ

-この solution や https://leetcode.com/problems/linked-list-cycle/solutions/5604092/video-cycle-detection-visualized-tortoise-and-hare-method/
ここの説明を見ていました。
https://hayapenguin.com/notes/LeetCode/141/LinkedListCycle

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False

```

# Step3

かかった時間： ３ min

上記を書き直してわかりやすくしました。
コメントも追加しました。(実際の interview でコメント書いた方が良さそうと思いました。)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
```
