# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def toStr(node):
            if node:
                Str = str(node.val) + toStr(node.next)
            else:
                Str = ''
            return Str

        str1 = toStr(l1)
        str2 = toStr(l2)

        str1 = str1[::-1]
        str2 = str2[::-1]

        int3 = int(str1) + int(str2)

        str3 = str(int3)
        str3 = str3[::-1]

        def toNode(Str):
            if Str.__len__() != 0:
                node = ListNode(Str[0])
                Str = Str[1:]
                node.next = toNode(Str)
            else:
                node = None
            return node

        return toNode(str3)
