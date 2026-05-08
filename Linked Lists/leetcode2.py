# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        current = head
        carry = 0

        while l1 is not None or l2 is not None:
            sum = 0

            if l1 is not None:
                sum += l1.val
                l1 = l1.next

            if l2 is not None:
                sum += l2.val
                l2 = l2.next

            sum += carry
            val = sum % 10
            carry = sum // 10

            if current is None:
                head = ListNode(val)
                current = head
            else:
                current.next = ListNode(val)
                current = current.next

        if carry > 0:
            current.next = ListNode(carry)

        return head
