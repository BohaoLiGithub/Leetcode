class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        res = ''
        for val,counter in counter.most_common():
            res += val * counter
        return res