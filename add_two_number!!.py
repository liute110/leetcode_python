#coding=utf-8
class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1,stack2 = [],[]
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        head = ListNode(0)
        val = carry = 0
        while stack1 or stack2  or carry:
            val = carry
            if stack1:
                val += stack1.pop()
            if stack2:
                val += stack2.pop()
            #carry, val = divmod(val, 10)
            if val >= 10:
                val -= 10
                carry = 1
            pre = ListNode(val)
            pre.next = head.next
            head.next = pre
        return head.next
