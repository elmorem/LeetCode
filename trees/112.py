# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_sum(root, cur_sum):
            if not root:
                return False
            cur_sum += root.val
            # now check to see if it is a leaf node
            if not root.left and not root.right:
                return cur_sum == targetSum
            return has_sum(root.left, cur_sum) or has_sum(root.right, cur_sum)
            # the or here ensures that we are checking everywhere
        return has_sum(root, cur_sum=0)


# Helper functions for testing
def create_tree(values: list) -> Optional[TreeNode]:
    """Create a binary tree from a list (level-order traversal, None for missing nodes)"""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    # Path: 5->4->11->2 = 22
    tree1 = create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    result1 = solution.hasPathSum(tree1, 22)
    print(f"Test 1: {result1}")  # Expected: True

    # Test case 2: [1,2,3], targetSum = 5
    tree2 = create_tree([1, 2, 3])
    result2 = solution.hasPathSum(tree2, 5)
    print(f"Test 2: {result2}")  # Expected: False

    # Test case 3: Empty tree
    tree3 = create_tree([])
    result3 = solution.hasPathSum(tree3, 0)
    print(f"Test 3: {result3}")  # Expected: False

    # Test case 4: Single node [1], targetSum = 1
    tree4 = create_tree([1])
    result4 = solution.hasPathSum(tree4, 1)
    print(f"Test 4: {result4}")  # Expected: True

    # Test case 5: Single node [1], targetSum = 0
    tree5 = create_tree([1])
    result5 = solution.hasPathSum(tree5, 0)
    print(f"Test 5: {result5}")  # Expected: False
