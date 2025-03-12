'''
You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer n and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return `true` _if the edges of the given graph make up a valid tree, and_ `false` _otherwise_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/12/tree1-graph.jpg)

**Input:** n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
**Output:** true

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/12/tree2-graph.jpg)

**Input:** n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
**Output:** false
Neetcode summary
union find, if union return false, loop exists, at end size must equal n, or its not connected; dfs to get size and check for loop, since each edge is double, before dfs on neighbor of N, remove N from neighbor list of neighbor;

> [!NOTE] Algo Summary
> 1. To determine if there is a loop I am doing union find.  if union returns False we have a loop
> 2. then I'm doing a basic DFS and then we check to see if n is == len(visisted) if they are, then they are connected .  if it is less than the length then we know we didn't get all the edges

'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for nei in adj[i]:
                if nei == prev:
                    continue
                if not dfs(nei,i):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visited) #checks both conditions and returns True only if both are True
# Test cases
print(Solution().validTree(5, [[0,1],[0,2],[0,3],[1,4]])) # True    
print(Solution().validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])) # False