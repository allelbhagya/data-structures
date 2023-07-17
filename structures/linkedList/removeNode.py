class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        
        current = head
        prev = None
        while current:
            if current.val == val:
                if prev:
                    prev.next = current.next
                else:
                    head = current.next
            else:
                prev = current
            current = current.next
        
        return head
