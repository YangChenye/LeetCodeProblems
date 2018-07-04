class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        '''Brute Force'''
        l = len(nums)

        for i in range(l):
            for j in range(i+1, l):
                if nums[i]+nums[j] == target:
                    return [i, j]

        '''Two-pass Hash Table'''
        # l = len(nums)
        # table = {}
        # for i in range(l):
        #     table[i] = '%d' %nums[i]
        #
        # for i in range(l):
        #     complement = target - nums[i]
        #     if table.get('%d' %complement) != None and table.get('%d' %complement) != i:
        #         return [i, table.get('%d' %complement)]

nums = [2, 7, 11, 15]
target = 9
print(Solution.twoSum(Solution, nums=nums, target=target))