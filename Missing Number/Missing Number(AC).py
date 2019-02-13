class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        #print(nums)
        for i in range(len(nums)):
            if not i == nums[i]:
                return i
        return len(nums)