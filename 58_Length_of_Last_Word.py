class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        div = s.split()
        if div.__len__() == 0:
            return 0
        else:
            return div[-1].__len__()

if __name__ == '__main__':
    S = Solution()
    s = "Hello \nWorld"
    print(S.lengthOfLastWord(s))