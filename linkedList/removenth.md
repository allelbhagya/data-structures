# remove nth node from end of list

## approach

- make a dummy node
- count length of list, subtract with n
- iterate over list again, when at right place, skip that node with

```python
curr.next = curr.next.next
```

## time complexity - O(n)

```py
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        l = 0
        curr = head
        while curr:
            l+=1
            curr = curr.next
        val = l-n
        curr = dummy
        for i in range(val):
            curr=curr.next
        curr.next = curr.next.next
        return dummy.next
```
