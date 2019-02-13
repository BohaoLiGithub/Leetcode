from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def func(a,b):
            return cmp(a+b,b+a)
        nums = map(str,nums)
        nums.sort(key = cmp_to_key(func),reverse = True)
        return '0' if nums[0] == '0' else ''.join(nums) 