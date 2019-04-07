class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic_ = {}
        res = []
        for idx1, val in enumerate(nums):
            dic_[val] = dic_.get(val,[]) + [idx1]
        
        for key,list_ in dic_.items():
            key2 = target - key
            if key2 in dic_.keys():
                if key == key2 and len(list_) > 1:
                    res += [list_[0],list_[1]]
                else:
                    res += [list_[0],dic_.get(key2)[0]]
                return res
                break
        return []