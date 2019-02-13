class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not n:
            return []
        temp = []
        result = []
        resultHeight = []
        for i in range(len(edges)):
            m = list(edges[i])
            m.reverse()
            temp.append(m)
        edges.extend(temp)
        #print (edges)
        for i in range(n):
            #print(i)
            visited = set()
            queue = []
            queue.insert(0,i)
            tempHeight = 0
            visited.add(i)
            while len(queue):
                tempHeight += 1
                level = len(queue)
                for _ in range(level):
                    value = queue.pop(-1)
                    #print("pop out "+str(value))
                    for j in range(len(edges)):
                        if edges[j][0] == value and (not edges[j][1] in visited):
                            visited.add(edges[j][1])
                            queue.insert(0,edges[j][1])
            resultHeight.append(tempHeight)
        #print (resultHeight)
        
        
        minHeight = min(resultHeight)
        for i in range(len(resultHeight)):
            if resultHeight[i] == minHeight:
                result.append(int(i))
        return result