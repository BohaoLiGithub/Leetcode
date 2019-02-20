class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        longest = 0
        dict_ = {}
        for i in range(len(nums)):
            if nums[i] not in dict_:
                dict_[nums[i]] = 1
            else:
                continue
            begin = nums[i]
            end = nums[i]
            if (nums[i] - 1) in dict_ :
                begin -= dict_[nums[i]-1]
            if (nums[i] + 1) in dict_ :
                end += dict_[nums[i]+1]
            longest = max(longest,end - begin +1)
            dict_[end] = end-begin + 1
            dict_[begin] = end-begin + 1
        return longest