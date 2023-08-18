# merge sorted lists

## time complexity - O(n)

```py
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        start = ListNode()
        curr = start

        while list1 and list2:
            v1 = list1.val
            v2 = list2.val

            if v1<=v2:
                curr.next = ListNode(v1)
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = ListNode(v2)
                curr = curr.next
                list2 = list2.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return start.next
```
