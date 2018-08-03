class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = nums
        T = target
        if ((T in N) == False):
            N.append(T)
            N.sort()

        return N.index(T)

S = Solution()
nums = [1,3,5,6]
target = 0
print(S.searchInsert(nums, target))