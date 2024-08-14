# 問題概要

問題: 2. Add Two Numbers

https://leetcode.com/problems/add-two-numbers/description/

言語: Python

# Step1

かかった時間：30min

思考ログ：

- head を返すことに気づかず、だいぶ時間かかりました。

- sum 2 number without the use of + - には似ていました。

```python
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create two pointers, one to go through the first list and another to got through the second list
        # sum gradually as we go , update the second list by that sum
        # if the sum > 10 then we take a number called temp number to the next node and added to the sum
        # the number will be sum // 10
        pointer1 = l1
        pointer2 = l2
        new_linked_list = ListNode()
        current_node = new_linked_list
        temp = 0
        while pointer1 is not None or pointer2 is not None:
            value_pointer1 = 0
            value_pointer2 = 0
            if pointer1 is not None :
                value_pointer1 = pointer1.val
            if pointer2 is not None :
                value_pointer2 = pointer2.val
            temp_sum = value_pointer1 + value_pointer2 + temp
            if temp_sum >= 10:
                temp = temp_sum // 10
                temp_sum = temp_sum % 10
            else:
                temp = 0
            current_node.next = ListNode(val = temp_sum)
            current_node = current_node.next
            if pointer1 is not None :
                pointer1 = pointer1.next
            if pointer2 is not None :
                pointer2 = pointer2.next
        if temp !=0:
            new_node = ListNode(val=temp)
            current_node.next = new_node
        return new_linked_list.next
```

疑問点：

- コードやや長くなってしまいました。無駄多かったです。

# Step2

かかった時間：5min

思考ログ

-この solution を参考にしました。
https://leetcode.com/problems/add-two-numbers/solutions/3675747/beats-100-c-java-python-beginner-friendly/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

c# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0
        while l1 is not None or l2 is not None or carry!=0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0
            temp_sum = digit1 + digit2 + carry
            digit = temp_sum % 10
            carry = temp_sum // 10

            new_node =  ListNode(digit)
            current.next = new_node
            current = current.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return dummy_head.next

```

# Step3

かかった時間： 5 min

上記を書き直してわかりやすくしました。(変数名を変えました)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_linked_list = ListNode()
        current = new_linked_list
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            temp_sum = digit1 + digit2 + carry
            digit = temp_sum % 10
            carry = temp_sum // 10
            new_node = ListNode(digit)
            current.next = new_node
            current = current.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return new_linked_list.next
```
