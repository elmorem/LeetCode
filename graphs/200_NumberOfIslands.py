'''
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return _the number of islands_.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

**Input:** grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
**Output:** 1

> [!NOTE] Algo Summary
> Approach: We're going to do dfs through the grid
> 1. Our dfs we're passing in (i,j)
> 	1. Base case: 1. if we go out of bounds OR OR if we hit a square that isn;t a one
> 	2. Essentailly we are going to run dfs each time we hit a "1".  and then we're going to traverse all the adjacent positions that are 1 and set them to 0
> 2. we're goging to traverse the matrix and 
> 	1. if we find a "1" we set it to "0" 
> 	2. we increment islands 
> 	3. run dfs on the adjacent positions until ther are no more "1"s or we run out
> 3. return islands

'''
from typing import List
def numIslands(grid: List[List[str]]) -> int:
    def dfs(i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                islands += 1
                dfs(i,j)
    return islands