class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums)-1
        cursor = start
        while cursor < len(nums) and cursor <= end :
            if nums[cursor] == 0:
                nums[cursor] = nums[start]
                nums[start] = 0
                start += 1
                cursor += 1
            elif nums[cursor] == 1:
                cursor += 1
                
            else:
                nums[cursor] = nums[end]
                nums[end] = 2
                end -= 1