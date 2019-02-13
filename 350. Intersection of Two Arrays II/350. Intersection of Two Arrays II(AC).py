class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        res = []
        if len(nums1) >= len(nums2):
            dic = collections.Counter(nums1)
            for val in nums2:
                if val in dic and dic[val] > 0:
                    dic[val] -= 1
                    res.append(val)
        else:
            dic = collections.Counter(nums2)
            for val in nums1:
                if val in dic and dic[val] > 0:
                    dic[val] -= 1
                    res.append(val)
        return res