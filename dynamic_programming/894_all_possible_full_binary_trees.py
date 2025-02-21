'''
Given an integer `n`, return _a list of all possible **full binary trees** with_ `n` _nodes_. Each node of each tree in the answer must have `Node.val == 0`.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in **any order**.

A **full binary tree** is a binary tree where each node has exactly `0` or `2` children.

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png)

**Input:** n = 7
**Output:** [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0:[], 1: [TreeNode]} # map int n to list of binary trees
        # return full list of fbt with n nodes
        def backtrack(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode(val=0)]
            ans = []
            if n in dp:
                return dp[n] 
            else:
            # this is the key
            # this is the key move
                for l in range(n):
                    r = n-1-l
                    print(f"{l = }")
                    print(f"{r = }")
                    leftTrees, rightTrees = backtrack(l), backtrack(r)
                    for t1 in leftTrees:
                        for t2 in rightTrees:
                            ans.append(TreeNode(0, t1, t2))
                dp[n] = ans
                return ans
        return backtrack(n)
print(Solution().allPossibleFBT(7))
# print(Solution().allPossibleFBT(5))
# print(Solution().allPossibleFBT(3))