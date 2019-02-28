# sum(bool) True means 1, False means 0

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > 0:
            return len(set(nums) & set(num+k for num in nums))
        elif k == 0:
            #list_ = [v>1 for v in collections.Counter(nums).values()]
            return sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0