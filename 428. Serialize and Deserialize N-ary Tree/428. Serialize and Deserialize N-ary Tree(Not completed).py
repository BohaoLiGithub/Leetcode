# deserialize not completed    
def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        res = self.preOrder(root)
        return res
    def preOrder(self,root):
        if not root:
            return
        res = str(root.val)
        if len(root.children) == 0:
            return res
        res += '['
        for node in root.children:
            res += self.preOrder(node)+' '
        res = res[:len(res)-1]
        res += ']'
        return res