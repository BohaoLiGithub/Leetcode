class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two, three = float('-inf'),float('-inf'),float('-inf')
        for num in nums:
            if num > one: # one is the maximum
                one,two,three = num,one,two
            elif num > two and num < one:
                two, three = num,two
            elif num > three and num < two:
                three = num
        return three if three != float('-inf') else one