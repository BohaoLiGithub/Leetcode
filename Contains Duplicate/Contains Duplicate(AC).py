class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        dic = {}
        for i in range(len(nums)):
            if dic.has_key(nums[i]):
                return True
            else:
                dic[nums[i]] = 1
        return False