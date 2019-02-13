# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        this problem seemed very hard but actually once you draw a picture on a paper or in your brain, it becomes pretty clear.
        - for the left  node, you set its index as index - 1
        - for the right node, you set its index as index + 1
        - use queue to loop through all the nodes in a tree
        - set index as a key to the hashmap() and value as a list of vals
        - add node.data into hashmap() with index as a key
        - keep track of min and max index and store into solution list and return it
        """
        if not root: return []
        queue = [(root,0)]
        dic = collections.defaultdict(list)
        Min, Max = 0, 0
        while queue:
            node,index = queue.pop(0)
            dic[index] += [node.val]
            if node.left:
                Min = min(Min,index-1)
                queue.append((node.left,index-1))
            if node.right:
                Max = max(Max,index+1)
                queue.append((node.right,index+1))
        result = []
        for i in range(Min,Max+1):
            result.append(dic[i])
        return result