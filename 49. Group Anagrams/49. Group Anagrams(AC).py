class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = collections.defaultdict(list)
        for word in strs:
            dic[''.join(sorted(word))] += [word]
        return [value for key, value in dic.items()]