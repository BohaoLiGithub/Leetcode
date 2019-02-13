class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        closest = float("inf")
        sumA = int()
        if len(nums) < 3:
            return res
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l = i + 1
            r = len(nums) -1
            while l < r:
                temp = nums[i] + nums[l] + nums[r] - target
                if temp == 0:
                    sumA = nums[i] + nums[l] + nums[r]
                    return sumA
                else:
                    if abs(temp) < closest:
                        closest = abs(temp)
                        sumA = nums[i] + nums[l] + nums[r]
                    if temp < 0:
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    else:
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
        return sumA