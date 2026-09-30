class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            # Diameter passing through this node
            self.diameter = max(self.diameter, left + right)

            # Height of this node
            return 1 + max(left, right)

        height(root)
        return self.diameter