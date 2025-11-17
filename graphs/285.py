from typing import Optional
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        succ = None
        cur = root
        while cur:
            if cur.val >p.val:
                succ = cur
                cur = cur.left
            else:
                cur = cur.right
        return succ
    
if __name__ == "__main__":
    solution = Solution()
    # Example usage:
    # Construct a binary search tree and test the inorderSuccessor method
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    p = root.left  # Node with value 3
    successor = solution.inorderSuccessor(root, p)
    if successor:
        print(successor.val)  # Expected output: 4
    else:
        print("No successor found")
    