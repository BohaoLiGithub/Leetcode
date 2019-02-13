class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for c in range(m,len(nums1)):
            nums1.pop(-1)
        cursor1, cursor2 = 0,0
        while cursor1 < len(nums1) and cursor2 < n:
            if nums2[cursor2] <= nums1[cursor1]:
                nums1.insert(cursor1,nums2[cursor2])
                cursor2 += 1
            else:
                cursor1 += 1
        if not cursor2 > n:
            nums1 += nums2[cursor2:]