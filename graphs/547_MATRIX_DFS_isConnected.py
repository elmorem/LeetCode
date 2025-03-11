'''
There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return _the total number of **provinces**_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)

**Input:** isConnected = 
[[1,1,0], 1 is connected to 1, 1 is connected to 2 1 is not connected to 3
[1,1,0], 1 is connected to 2, 2 is connected to 2, 3 is not connected to 2
[0,0,1]] 3 is not connected to 1, 3 is not connecetd to 3 ,3 is connected to itself 
**Output:** 2


> [!NOTE] Algo Summary
> 1. initialized visited set and number of provinces
> 2. DFS takes in a city doesn't return anything
> 3. for each city we're going to cycke through
> 	1. continue if no connection
> 	2. continue if i in visisted
> 	3. else add it and recursively run dfs(i)
> 4. to start things off were going to all the cities
> 	1. if we've already seen it skip
> 	2. otherwise add it.
> 	3. If we made it here, this is either the first time and we increment provinces OR the dfs didn't visite it previously and so we have another province
> 	4. then run dfs on that city to find any it is connected with
> 5. Return provinces
'''
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0

        def dfs(city):
            for i in range(len(city)):
                if city[i] == 0:
                    continue
                elif i in visited:
                    continue
                else:
                    visited.add(i)
                    dfs(isConnected[i])

        
        for i in range(len(isConnected)):
            if i in visited:
                continue
            else:
                visited.add(i)
                provinces +=1
                dfs(isConnected[i])
        return provinces
# Test cases
print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])) # 2
print(Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]])) # 3
print(Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]])) # 3