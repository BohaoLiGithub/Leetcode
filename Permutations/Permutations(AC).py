#backtracking

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result = []
        templist = []

        def backtracking():
            if len(templist) == len(nums):
                list1 = list(templist)
                result.append(list1)
            else:
                for i in range(len(nums)):
                    if nums[i] in templist:
                        continue
                    templist.append(nums[i])
                    backtracking()
                    templist.pop()
        backtracking()
        return result