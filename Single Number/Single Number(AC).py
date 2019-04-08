class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_ = {}
        for num in nums:
            dict_[num] = dict_.get(num,0) + 1
        for key, val in dict_.items():
            if val == 1:
                res = key
                return res
        return -1