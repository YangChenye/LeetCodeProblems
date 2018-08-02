class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x > pow(2,31)-1 or x < -pow(2,31):
            return 0

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

        if final > pow(2,31)-1 or final < -pow(2,31):
            return 0

        return final

S = Solution()
X = 12
print(S.reverse(X))