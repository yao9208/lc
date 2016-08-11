# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []
        if not root:
            return data
        queue = deque()
        queue.append(root)
        data.append(root.val)
        while len(queue)!=0:
            flag = False
            size = len(queue)
            for i in range(size):
              node = queue.popleft()
              if node.left:
                queue.append(node.left)
                data.append(node.left.val)
                flag = True
              else:
                data.append('#')
              if node.right:
                queue.append(node.right)
                data.append(node.right.val)
                flag = True
              else:
                data.append('#')
            if not flag:
              break
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None
        root = TreeNode(data[0])
        queue = deque()
        queue.append(root)
        i = 1
        while len(queue)!=0:
            size = len(queue)
            for j in range(size):
              node = queue.popleft()
              if data[i]!='#':
                node.left = TreeNode(data[i])
                queue.append(node.left)
              i+=1
              if data[i]!='#':
                  node.right = TreeNode(data[i])
                  queue.append(node.right)
              i+=1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
