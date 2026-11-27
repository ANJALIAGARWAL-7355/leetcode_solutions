class Solution:
    def maxPathSum(self, root):
        maxi = [float('-inf')]

        def maxGain(node):
            if not node:
                return 0

            left = max(0, maxGain(node.left))
            right = max(0, maxGain(node.right))

            maxi[0] = max(maxi[0], node.val + left + right)

            return node.val + max(left, right)

        maxGain(root)
        return maxi[0]