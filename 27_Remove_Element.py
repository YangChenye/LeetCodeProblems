class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for each in nums:
            if each == val:
                count += 1

        for i in range(count):
            nums.remove(val)

        return nums.__len__()

if __name__ == '__main__':
    S = Solution()
    nums = [1,2,3,2,5]
    val = 5
    print(S.removeElement(nums,val))