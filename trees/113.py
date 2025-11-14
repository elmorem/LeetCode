from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        temp = []
        def dfs(root):
            if not root:
                return []
            temp.append(root.val)
            
            if not root.left and not root.right and sum(temp) == targetSum:
                ans.append(temp[:])
            dfs(root.left)
            dfs(root.right)
            temp.pop()

        dfs(root)
        return ans


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

    # Test case 1: [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    # Paths: [[5,4,11,2], [5,8,4,5]]
    tree1 = create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    result1 = solution.pathSum(tree1, 22)
    print(f"Test 1: {result1}")  # Expected: [[5,4,11,2], [5,8,4,5]]

    # Test case 2: [1,2,3], targetSum = 5
    tree2 = create_tree([1, 2, 3])
    result2 = solution.pathSum(tree2, 5)
    print(f"Test 2: {result2}")  # Expected: []

    # Test case 3: [1,2], targetSum = 0
    tree3 = create_tree([1, 2])
    result3 = solution.pathSum(tree3, 0)
    print(f"Test 3: {result3}")  # Expected: []

    # Test case 4: Empty tree
    tree4 = create_tree([])
    result4 = solution.pathSum(tree4, 0)
    print(f"Test 4: {result4}")  # Expected: []

    # Test case 5: Single node [1], targetSum = 1
    tree5 = create_tree([1])
    result5 = solution.pathSum(tree5, 1)
    print(f"Test 5: {result5}")  # Expected: [[1]]