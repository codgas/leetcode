# 問題概要

問題: 142. Linked List Cycle 2

https://hayapenguin.com/notes/LeetCode/142/LinkedListCycleTwo

言語: Python

# Step1

かかった時間：10min

思考ログ：

- set にどうやって append するの google 使う必要があった。

- set にするか dict にするか迷っていました。

```python
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes_passed_by_slow = set()
        nodes_passed_by_fast = set()
        slow = fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            nodes_passed_by_slow.add(slow)
            nodes_passed_by_fast.add(fast)
            if slow == fast:
                return next(iter(nodes_passed_by_slow & nodes_passed_by_fast))
            slow = slow.next
        return None

```

疑問点：

- submit すると 8/17 成功、時間の問題ではないので、何かのミスです。
- slow pointer と fast pointer を使用するところまで気づいたが、floyd の tortoise and hare アルゴリズムをきちんと知らなかったため、解決できませんでした。

# Step2

かかった時間：5min

思考ログ

-Tortoise and hare の algorithm を使用
ref: https://leetcode.com/problems/linked-list-cycle-ii/solutions/3274329/clean-codes-full-explanation-floyd-s-cycle-finding-algorithm-c-java-python3/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow = head
                while slow !=fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

```

# Step3

かかった時間： 4 min

上記を書き直してわかりやすくしました。
verbose になるように、変数名を工夫しました。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                starter_pointer = head
                cycle_pointer = fast
                while starter_pointer != cycle_pointer:
                    starter_pointer = starter_pointer.next
                    cycle_pointer = cycle_pointer.next
                return starter_pointer
        return None
```
