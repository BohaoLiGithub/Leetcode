"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return "";
        res = str(root.val)
        if len(root.children) != 0:
            children_res = []
            for child in root.children:
                children_res.append(self.serialize(child))
            res = res + "[" + " ".join(children_res) + "]"
        #print(res)
        return res
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if len(data) == 0:
            return None
        start = data.find('[')
        end = data.rfind(']')
        node = None
        if start == -1:
            #print('data:'+str(data))
            node = Node(int(data),[])
            return node
        else:
            node = Node(int(data[:start]),[])
        middle = data[start+1:end]
        level = 0
        start = 0
        for i in range(len(middle)):
            if middle[i] == '[':
                level += 1
            elif middle[i] == ']':
                level -= 1
            elif middle[i] == ' ' and level == 0:
                node.children.append(self.deserialize(middle[start:i]))
                start = i + 1
        node.children.append(self.deserialize(middle[start:])) #last node
        return node
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))