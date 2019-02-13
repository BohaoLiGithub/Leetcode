class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return [nums[0]]
            else:
                return nums
        dic = {}
        result = []
        for i in range(len(nums)):
            if dic.has_key(nums[i]):
                dic[nums[i]] += 1
                if dic[nums[i]] > int(len(nums)//3) and not nums[i] in result:
                    result.append(nums[i])
                    if dic[nums[i]] > int(len(nums) * 2 // 3):
                        return result
            else:
                dic[nums[i]] = 1
        return result