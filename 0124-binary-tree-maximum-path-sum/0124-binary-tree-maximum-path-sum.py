# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maxSum = float('-inf')
    def solve(self, root):
        if root is None:
            return 0
        leftSum = self.solve(root.left)
        rightSum = self.solve(root.right)

        left_root_right_sum = leftSum + rightSum + root.val
        single_side_max = max(leftSum, rightSum) + root.val
        only_node = root.val
        val_arr = [left_root_right_sum, single_side_max, only_node, self.maxSum]
        self.maxSum = max(val_arr)
        return max([single_side_max, only_node])

    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.solve(root)
        return self.maxSum
        