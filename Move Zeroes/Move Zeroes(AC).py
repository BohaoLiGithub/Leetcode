class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        firstzero = -1
        for i in range(len(nums)):
            if not nums[i] == 0:
                firstzero += 1
                temp = nums[i]
                nums[i] = nums[firstzero]
                nums[firstzero] = temp