# dp

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        for i in range(1,len(nums)):
            self.nums[i] += self.nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > j:
            return None
        if j >= len(self.nums):
            return None
        sum = 0
        for m in range(i,j+1,1):
            sum += self.nums[m]
        return self.nums[j] - (self.nums[i-1] if i>0 else 0) 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)