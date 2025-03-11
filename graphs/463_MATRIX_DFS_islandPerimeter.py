'''

You are given `row x col` `grid` representing a map where `grid[i][j] = 1` represents land and `grid[i][j] = 0` represents water.

Grid cells are connected **horizontally/vertically** (not diagonally). The `grid` is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/12/island.png)

**Input:** grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
**Output:** 16
**Explanation:** The perimeter is the 16 yellow stripes in the image above.


> [!NOTE] Algo Summary
> KEY: The key to this one is realizing that we can get the perimeter of a given cell by adding up the number of sides that are either out of bounds or are facing water.
> Key: the other key we need to keep track of which ones we've seen so we don't count them twice
> recursive function 
> 	1 .is going to return 0 if we've already visited
> 	1. return 1 for each boundary or 1
> 1. Then we basically only need to call it on the first position with a 1.
'''
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        matrix = grid[::]
        print(matrix)
        visited = set()
        def dfs(i,j):
            if i <0 or j < 0 or i >=m or j >=n or grid[i][j] == 0:
                return 1
            elif (i,j) in visited:
                return 0
            visited.add((i,j))
            perimeter = 0
            perimeter += (dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1))
            return perimeter 
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i,j)

# Test cases
print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])) # 16
print(Solution().islandPerimeter([[1]])) # 4
print(Solution().islandPerimeter([[1,0]])) # 4