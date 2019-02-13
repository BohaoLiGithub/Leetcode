class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {i : set() for i in range(numCourses)}
        inDegree = {i: 0 for i in range(numCourses)}
        visited = []
        queue = []
        
        for prep in prerequisites :
            graph[prep[0]].add(prep[1])
            inDegree[prep[1]] += 1
        for key in inDegree :
            if inDegree[key] == 0:
                queue.insert(0,key)
        while len(queue):
            index = queue.pop(-1)
            visited.insert(0,index)
            for endpoint in graph[index]:
                inDegree[endpoint] -= 1
                if inDegree[endpoint] == 0:
                    queue.insert(0,endpoint)
        if len(visited) == numCourses:
            return visited
        else:
            return []