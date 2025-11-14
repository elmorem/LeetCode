# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        x = None
        y = None
        curr = root
        while curr:
            if curr.left is None:
                if prev and prev.val > curr.val:
                    if x is None:
                        x =prev
                    y = curr
                prev=curr
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    if prev and prev.val > curr.val:
                        if x is None:
                            x = prev
                        y = curr
                    prev = curr
                    curr = curr.right
        if x and y:
            x.val, y.val = y.val, x.val
if __name__ == "__main__":
    solution = Solution()
    # Example usage:
    # Construct a binary tree with swapped nodes and call recoverTree
    # Note: You would need to implement tree construction and printing functions for full testing