class Solution(object):
    def buildTree(self, inorder, postorder):
        index_map = {val: i for i, val in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)

            mid = index_map[root_val]

            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)