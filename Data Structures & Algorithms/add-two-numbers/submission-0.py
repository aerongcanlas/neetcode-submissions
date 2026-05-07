# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = cur = ListNode()
        carry = 0

        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = 1 if total > 9 else 0
            cur.next = ListNode(total % 10)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val + carry
            carry = 1 if total > 9 else 0
            cur.next = ListNode(total % 10)
            cur = cur.next
            l1 = l1.next

        while l2:
            total = l2.val + carry
            carry = 1 if total > 9 else 0
            cur.next = ListNode(total % 10)
            cur = cur.next
            l2 = l2.next

        if carry:
            cur.next = ListNode(1)
        return dummy.next
