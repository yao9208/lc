class Node(object):
        def __init__(self, val, count):
            self.val = val
            self.count = count
            self.dup = 1
            self.left = None
            self.right = None

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        root = None
        for i in range(n-1, -1, -1):
            root = self.insert(root, nums[i], result, i)
        return result

    def insert(self, root, x, result, i):
        if not root:
            result[i] = 0
            return Node(x, 0)
        node = prev = root
        count = 0
        while node:
            prev = node
            if x>node.val:
                count+=node.dup+node.count
                node = node.right
            elif x<node.val:
                node.count += 1
                node = node.left
            else:
                node.dup += 1
                result[i] = count+node.count
                return root
        if x>prev.val:
            prev.right = Node(x, 0)
        else:
            prev.left = Node(x, 0)
        result[i] = count
        return root
