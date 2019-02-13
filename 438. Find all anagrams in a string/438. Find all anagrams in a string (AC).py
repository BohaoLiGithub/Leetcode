#Slide window

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_list = list(p)
        s_list = list(s)
        result = []
        p_dict = collections.defaultdict(int)
        for c in p_list:
            p_dict[c] += 1
        start = 0
        end = 0
        count = len(p_dict)
        while(end < len(s)):
            if p_dict.has_key(s[end]):
                p_dict[s[end]] -= 1
                if p_dict[s[end]] == 0 :
                    count -= 1
            end += 1
            while count == 0:
                char_start = s[start]
                if p_dict.has_key(char_start):
                    p_dict[char_start] +=1
                    if p_dict[char_start] > 0 :
                        count += 1
                        print ("count: "+ str(count))
                        print ("char: "+ str(char_start))
                        print ("start: " + str(start))
                if end - start == len(p):
                    result.append(start)
                start += 1
                
        return result