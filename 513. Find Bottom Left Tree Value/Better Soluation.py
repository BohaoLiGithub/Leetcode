# BST from right to left
# using filter to filter None

def findLeftMostNode(self, root)
    queue = [root]
    for node in queue
        queue += filter(None, (node.right, node.left))
    return node.val