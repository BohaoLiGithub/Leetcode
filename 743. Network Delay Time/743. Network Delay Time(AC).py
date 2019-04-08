from Queue import PriorityQueue
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        dist = [float('inf') for _ in range(N)]
        dist[K-1] = 0
        for idx in range(1,N+1):
            for x,y,time in times:
                if dist[x-1] + time < dist[y-1]:
                    dist[y-1] = dist[x-1] + time
        return -1 if max(dist) == float('inf') else max(dist)