'''
You are given an `n x n` binary matrix `grid` where `1` represents land and `0` represents water.

An **island** is a 4-directionally connected group of `1`'s not connected to any other `1`'s. There are **exactly two islands** in `grid`.

You may change `0`'s to `1`'s to connect the two islands to form **one island**.

Return _the smallest number of_ `0`_'s you must flip to connect the two islands_.
O n2

> [!NOTE] Algo Summary
> 1.  Probably the best way to do this is to use bfs.  where we find any starting island and then add all their neighbors and that is one
> 2. but to find any starting island we are going to run a basic dfs
> 3. then we are going to run bfs on the neighbors of the starting island
> 4. then we are going to keep track of the visited nodes and the distance from the starting node


'''
from collections import deque
from typing import List
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[0,1],[0,-1],[-1,0], [1,0]]
        # a little checker to see if we are out of bounds
        visit =set()
        def invalid(r,c):
            return r < 0 or c < 0 or r == N or c == N
        
        def dfs(r,c):
            if (invalid(r,c) or not grid[r][c] or (r,c) in visit):
                return
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        def bfs():
            res = 0
            q = deque(visit)
            
            while q:
                for i in range(len(q)): # how we're going to go through each cycle and count
                    r,c, = q.popleft()
                    for dr, dc in directions:
                        curR, curC = r + dr, c+dc
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]:
                            return res
                        q.append([curR,curC])
                        visit.add((curR, curC))
                res +=1
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r,c) # we only need to run this once since this is what starts our bfs
                    return bfs()  # we can call this without anything here because we will be using the visit set
                            # as our queue
