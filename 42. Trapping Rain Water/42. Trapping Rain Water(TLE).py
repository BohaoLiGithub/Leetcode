class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <2:
            return 0
        max_ = max(height)
        
        res = 0
        for i in range(1,max_+1):
            temp = [0] * len(height)
            for j in range(len(height)):
                if height[j] > 0:
                    temp[j] = 1
                    height[j] -= 1
                    
            start,end = 0,len(temp)-1
            flag = False
            while start <= end:
                if temp[start] == 1 and temp[end] == 1:
                    flag = True
                    break
                elif temp[start]==1:
                    end -= 1
                elif temp[end] == 1:
                    start += 1
                else:
                    start +=1 
                    end -= 1
            if flag:
                num = 0
                for p in range(start,end+1):
                    if temp[p] == 0:
                        num +=1
                res += num
                
        return res