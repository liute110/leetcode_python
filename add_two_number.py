#coding=utf-8

class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution():
    def add_two_nums(self,l1,l2):
        tmp = 0
        result = ListNode(0)
        point = result
        while l1 and l2:
            data = l1.val + l2.val + tmp
            tmp = 0
            if data >= 10:
                data = data - 10
                tmp = 1
            point.next = ListNode(data)
            point = point.next
            l1,l2 = l1.next,l2.next
        while l1:
            data = tmp + l1.val
            tmp = 0
            if data >= 10:
                data = data - 10
                tmp = 1
            point.next = ListNode(data)
            point = point.next
            l1 = l1.next
        while l2:
            data = tmp + l2.val
            tmp = 0
            if data >= 10:
                data = data - 10
                tmp = 1
            point.next = ListNode(data)
            point = point.next
            l2 = l2.next
        if tmp > 0:
            point.next = ListNode(tmp)
            tmp = 0
        return result.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
re = Solution().add_two_nums(l1,l2)
while re:
    print re.val
    re = re.next
            
