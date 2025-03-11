'''
You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return _the maximum **area** of an island in_ `grid`. If there is no island, return `0`.

> [!NOTE] Algo Summary
> 1.Initialize max area, and grid parameters
> 1. we're doing a DFS on (i,j)
> 	1. Our recursive function is returning a value, which is the area of a particular isan
> 2. base case
> 	1. if we go out of bounds or we hit water 
> 	2. Then we return 0 so that when we are adding thing up in the end it makes sense
> 3. Else:
> 	1. set the position to 0
> 	2. and return 1 + dfs (on all the surrounding positions)
> 4. Outide the dfs we're going to cycle through through all positions
> 	1. If that position contains an island we take the existing max of the existing max_area and whateer dfs(i,j) return 

'''
from typing import List
def maxAreaOfIsland(grid: List[List[int]]) -> int:
    max_area = 0
    m, n = len(grid), len(grid[0])
    def dfs(i, j):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return 0
        else:
            grid[i][j] = 0
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i,j))
    return max_area
# Test cases
print(maxAreaOfIsland([[0,0,0,0,0,0,0,0]])) # 0
print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])) # 2
#6
