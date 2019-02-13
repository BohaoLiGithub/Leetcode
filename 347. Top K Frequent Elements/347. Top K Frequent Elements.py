
# collections.Counter(list).most_common(k)
# return a dic

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = collections.Counter(nums).most_common(k)
        result = []
        for i,j in dic:
            result.append(i)
        return result