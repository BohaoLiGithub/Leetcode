class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target > nums[i] :
                if i == len(nums)-1:
                    return len(nums)
                else:
                    continue
            elif target == nums[i]:
                return i
            else:
                return i