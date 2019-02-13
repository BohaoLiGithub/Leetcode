# https://www.cnblogs.com/grandyang/p/5336668.html

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0:-1}
        sumA = 0
        maxLen = 0
        for i in range(len(nums)):
            sumA += nums[i]
            if sumA - k in dic and i - dic[sumA-k] > maxLen:
                maxLen = i - dic[sumA-k]
            if sumA not in dic:
                dic[sumA] = i
        return maxLen