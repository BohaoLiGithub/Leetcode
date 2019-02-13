#Topological Sorting

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        graph = {i : set() for i in range(numCourses)}
        inDegree = {i : 0 for i in range(numCourses)}
        visited = [0] * numCourses
        for prep in prerequisites:
            graph[prep[0]].add(prep[1])
            inDegree[prep[1]] += 1
        
        queue = []
        k = 0
        for key,value in inDegree.items():
            if inDegree[key] == 0:
                queue.insert(0,key)
                k += 1
                visited[key] = 1
        while len(queue):
            index = queue.pop(-1)
            for endpoint in graph[index]:
                inDegree[endpoint] -= 1
                if inDegree[endpoint] == 0:
                    queue.insert(0,endpoint)
                    k += 1
                    visited[key] = 1     
        return k == numCourses