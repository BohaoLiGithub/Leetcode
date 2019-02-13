class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        val = nums[0]
        times = 1
        for i in range(1,len(nums)):
            if nums[i] == val:
                times +=1
                if 2*times > len(nums):
                    return val
            else:
                val = nums[i]
                times = 1
        return nums[0]