# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1.__len__() == 0:
            L1 = [0]
        else:
            L1 = l1
        if l2.__len__() == 0:
            L2 = [0]
        else:
            L2 = l2

        str1 = ''
        str2 = ''

        for each in L1:
            str1 = str1 + str(each)

        for each in L2:
            str2 = str2 + str(each)

        str1 = str1[::-1]
        str2 = str2[::-1]

        num1 = int(str1)
        num2 = int(str2)

        numResult = num1 + num2

        strResult = str(numResult)

        listResult = list(strResult)

        listResult = listResult[::-1]

        result = [int(each) for each in listResult]

        return result



l1 = [2,4,3]
l2 = [5,6,4]
test = Solution()
l = test.addTwoNumbers(l1=l1,l2=l2)
print(l)