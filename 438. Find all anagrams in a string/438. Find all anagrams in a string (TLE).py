# 35/36

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
        p_dict = dict()
        for c in p_list:
            if not p_dict.has_key(c):
                p_dict[c] = 1
            else:
                p_dict[c] += 1
        start = 0
        end = len(p)-1
        while(start <= len(s)-len(p) and end <= len(s)-1):
            temp_dict = dict()
            flag = True
            for j in range(start,end+1,1):
                if s_list[j] not in p_list:
                    flag = False
                    start = j+1
                    end = start+len(p)-1
                    break
                else:
                    if not temp_dict.has_key(s_list[j]):
                        temp_dict[s_list[j]] = 1
                    else:
                        temp_dict[s_list[j]] += 1
            if flag:
                if cmp(temp_dict,p_dict) == 0:
                    #print("in if")
                    result.append(start)
                start += 1
                end += 1
        return result