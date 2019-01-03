# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        SumNode = ListNode(0)
        ImGroot = SumNode
        count = 0
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        while(True):
            count = 0
            SumNode.val += l1.val + l2.val
            if SumNode.val >= 10 :
                SumNode.val %= 10
                count += 1
                SumNode.next = ListNode(count)

            if l1.next == None and l2.next == None:
                break
            else:
                SumNode.next = ListNode(count)
                if l1.next == None:
                    l1.next = ListNode(0)
                    l1 = l1.next
                    l2 = l2.next
                elif l2.next == None:
                    l2.next = ListNode(0)
                    l2 = l2.next
                    l1 = l1.next
                else:
                    l1 = l1.next
                    l2 = l2.next

            SumNode = SumNode.next


        return ImGroot
