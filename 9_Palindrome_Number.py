class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or ((x != 0) and (x%10 == 0)):
            return False

        half = 0
        while half < x:
            half = x%10 +half*10
            x = (x/10).__int__()

        return (half == x) or ((half/10).__int__() == x)

if __name__ == '__main__':
    S = Solution()
    x = -121
    print(S.isPalindrome(x))