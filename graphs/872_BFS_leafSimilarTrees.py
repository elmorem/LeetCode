'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a **leaf value sequence**_._
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a **leaf value sequence**_._
**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg)

**Input:** root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
**Output:** true

For example, in the given tree above, the leaf value sequence is `(6, 7, 4, 9, 8)`.

Two binary trees are considered _leaf-similar_ if their leaf value sequence is the same.

Return `true` if and only if the two given trees with head nodes `root1` and `root2` are leaf-similar.
> [!NOTE] Algo Summary
> KEY: excellent for getting the essence of BFS
> Key:  Pretty straight forward.  we're going to have a function that does a basic BFS and returns a list of all the leavesfrom left to right
> 1. function.
> 	1. uses a deque to append the vals
> 	2. while q
> 		1. we pop off each node append both if left and right, only 1 if only 1
> 		2. then if there are no node.left OR node.right we append the nodes to the leaves list
> 2. finaly we check if both leave lists are the sam


'''
from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root):
            if root is None:
                return []
            leaves = []
            queue = deque()
            queue.append(root)
            while queue:
                print(queue)
                n = len(queue)
                for i in range(n):
                    node = queue.pop()
                    if node.left and node.right:
                        queue.append(node.left)
                        queue.append(node.right)
                    elif node.left and not node.right:
                        queue.append(node.left)
                    elif node.right and not node.left:
                        queue.append(node.right)
                    elif not node.left and not node.right:
                        leaves.append(node.val)
            return leaves
        return get_leaves(root1) == get_leaves(root2)
# Test cases
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)          
root1.right.left = TreeNode(7)
root1.right.right = TreeNode(4)
root1.left.right.left = TreeNode(9)
root1.left.right.right = TreeNode(8)
root2 = TreeNode(3)     
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)          
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.left.right.left = TreeNode(9)
root2.left.right.right = TreeNode(8)
sol = Solution()    
print(sol.leafSimilar(root1, root2)) # False