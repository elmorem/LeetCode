'''
## LC 329 hard
Given an `m x n` integers `matrix`, return _the length of the longest increasing path in_ `matrix`.

From each cell, you can either move in four directions: left, right, up, or down. You **may not** move **diagonally** or move **outside the boundary** (i.e., wrap-around is not allowed).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg)

**Input:** matrix = [[9,9,4],[6,6,8],[2,1,1]]
**Output:** 4
**Explanation:** The longest increasing path is `[1, 2, 6, 9]`.

'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = defaultdict(int) #indicies:count
        
        def dfs(r,c, prevVal):
            if r <0 or r == m or c <0 or c ==n or matrix[r][c]<= prevVal:  
                #Do the out of bound check first
                #NOTE also add the condition if the value here is not an increasing value
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            val = matrix[r][c]
            count = 1
            count = max(count, 1+dfs(r+1, c, val))
            count = max(count, 1+dfs(r-1, c, val))
            count = max(count, 1+dfs(r, c+1, val))
            count = max(count, 1+dfs(r, c-1, val))
            dp[(r,c)] = count
            return count
        for r in range(m):
            for c in range(n):
                dfs(r,c,-1)
        print(f"{dp = }")
        return max(dp.values())
