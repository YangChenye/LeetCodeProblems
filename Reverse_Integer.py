class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= 0:
            xStr = str(x)
            xList = list(xStr)
            xList.reverse()
            result = ''
            for each in xList:
                result = result + each
            final = int(result)
        else:
            xStr = str(-x)
            xList = list(xStr)
            xList.reverse()
            result = ''
            for each in xList:
                result = result + each
            final = -int(result)

        return final

S = Solution()
X = 12
print(S.reverse(X))