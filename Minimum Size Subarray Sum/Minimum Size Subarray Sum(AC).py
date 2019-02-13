class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        left = 0
        result = len(nums) + 1
        for right in range(len(nums)):
            total += nums[right]
            while total >= s:
                result = min(result,right - left + 1)
                total -= nums[left]
                left += 1
                
        if result <= len(nums):
            return result
        else:
            return 0