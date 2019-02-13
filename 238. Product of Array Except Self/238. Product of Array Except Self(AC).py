# 99.69%

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        multi = 1
        result = []
        zero_nums = 0
        for num in nums:
            if num != 0:
                multi = multi * num
            else:
                zero_nums += 1
        if zero_nums == 0:
            for num in nums:
                div = multi / num
                result.append(div)
        elif zero_nums == 1:
            for num in nums:
                if num == 0:
                    result.append(multi)
                else:
                    result.append(0)
        else:
            for _ in range(len(nums)):
                result.append(0)
        return result