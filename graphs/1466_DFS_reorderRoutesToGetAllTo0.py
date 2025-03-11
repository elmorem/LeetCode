'''
There are `n` cities numbered from `0` to `n - 1` and `n - 1` roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by `connections` where `connections[i] = [ai, bi]` represents a road from city `ai` to city `bi`.

This year, there will be a big event in the capital (city `0`), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city `0`. Return the **minimum** number of edges changed.

It's **guaranteed** that each city can reach city `0` after reorder.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/05/13/sample_1_1819.png)

**Input:** n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
**Output:** 3
**Explanation:** Change the direction of edges show in red such that each node can reach the node 0 (capital).
- IDEASL. no loops in the graph.  no loops


> [!NOTE] Algo Sumary
> We're going to do DFS
> 1. Initialize: 
> 	1. edges set
> 	2. visited set
> 	3. changes variable
> 	4. neighbors. These are all the cities connected to one another no matter the direction.  Set this usp with an adj list
> 2. dfs:
> 	1. nonlocal edges, neighbnors, visited, changes
> 	2. cycle through all neighbor in neighbors[city
> 		1. continue if we already visisted
> 		2. if (neighbor, city) not in edges that means we need to switch the direction
> 		3. add that neighbor to visisted
> 		4. run dfs recursively
> 3. to start things off we add 0 to visited and run dfs on 0
> 4. return changes

'''
from collections import defaultdict
from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a,b in connections}
        visited = set()
        changes = 0
        neighbors = defaultdict(list)
        for i,j in connections:
            neighbors[i].append(j)
            neighbors[j].append(i)
        def dfs(city):
            nonlocal changes, neighbors, edges, visited
            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                if (neighbor, city) not in edges:
                    changes +=1
                visited.add(neighbor)
                dfs(neighbor)
        visited.add(0)
        dfs(0)
        return changes
# Test cases
sol = Solution()
print(sol.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])) # 3
print(sol.minReorder(5, [[1,0],[1,2],[2,3],[4,0],[4,3]])) # 2
print(sol.minReorder(3, [[1,0],[2,0]])) # 0
print(sol.minReorder(4, [[1,0],[2,0],[3,1],[3,2]])) # 1
