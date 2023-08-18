# add two numbers

## approach

- increment until both the lists are finished
- keep carry value to add with two values from list
- carry = value // 10 for next node in list
- value = value % 10, to add only 1 digit

## time complexity - O(max(l1,l2))

```py
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = ListNode()
        curr = start
        carry = 0

        # iterating until either nodes are present
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            value = v1 + v2 + carry
            carry = value // 10
            value = value % 10
            curr.next = ListNode(value)

            # updating the values
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            curr.next = ListNode(carry)
        return start.next
```
