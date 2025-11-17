from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0 
        def dfs(node):
            if not node:
                return True, None
            left_uni, left_val = dfs(node.left)
            right_uni, right_val = dfs(node.right)
            is_uni = left_uni and right_uni
            if left_val is not None and right_val != node.val:
                is_uni = False
            nonlocal count
            if is_uni:
                count +=1
            return is_uni, node.val
        dfs(root)
        return count
if __name__ == "__main__":
    solution = Solution()
    # Example usage:
    # Construct a binary tree and test the countUnivalSubtrees method
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(5)
    print(solution.countUnivalSubtrees(root))  # Expected output: 4