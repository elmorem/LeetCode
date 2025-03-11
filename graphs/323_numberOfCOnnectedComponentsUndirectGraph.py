'''
You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between `ai` and `bi` in the graph.

Return _the number of connected components in the graph_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/conn1-graph.jpg)

**Input:** n = 5, edges = [[0,1],[1,2],[3,4]]
**Output:** 2

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/conn2-graph.jpg)

**Input:** n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
**Output:** 1

'''
## Classic DFS solution
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i) # we need both becauseit is undirected
        def dfs(node, visited):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei, visited)

        count = 0
        visited = set()
        for i in range(n):
            if i not in visited: # we don't add to visited here b/c we do it in dfs
                dfs(i, visited)
                count +=1 # increment count anytime we come to a new node we haven't see
                        #always the first and if they're all connected never again
        return count
# Time complexity is O(m+n) where m is the number of edges and n is the number of nodes
# Space complexity is O(n) where n is the number of nodes
# This is because we are storing the adjacency list and the visited set

# union find solution
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [x for x in range(n)]
        rank = [1 for x in range(n)]
        def find(n1):
            res = n1
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else: 
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1,n2)
        return res 
# The time complexity is O(n) because we are iterating through the edges
# The space complexity is O(n) because we are storing the parent and the rank
# of each node