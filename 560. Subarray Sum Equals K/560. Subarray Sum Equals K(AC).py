# time complexity O(N)

class Solution(object):
    def subarraySum(self, nums, target):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0:1}
        res = pre_sum = 0
        for num in nums:
            #print('nums:'+str(num))
            pre_sum += num
            #print('pre_sum: '+str(pre_sum))
            res += dic.get(pre_sum - target, 0)
            #print('res:'+str(res))
            dic[pre_sum] = dic.get(pre_sum, 0) + 1
            #for key,val in dic.items():
                #print('key: '+str(key)),
                #print('val: '+str(val))
        return res