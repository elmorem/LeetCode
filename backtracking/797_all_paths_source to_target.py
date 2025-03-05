'''
Given a directed acyclic graph (**DAG**) of `n` nodes labeled from `0` to `n - 1`, find all possible paths from node `0` to node `n - 1` and return them in **any order**.

The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node `i` (i.e., there is a directed edge from node `i` to node `graph[i][j]`).

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg)

**Input:** graph = [[1,2],[3],[3],[]]
**Output:** [[0,1,3],[0,2,3]]
**Explanation:** There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg)

**Input:** graph = [[4,3,1],[3,2,4],[3],[4],[]]
**Output:** [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(list)
        ans = []
        for i, vals in enumerate(graph):
            adj_list[i] = vals
        n = len(graph)
        def backtrack(cur_path, cur_node):
            n = len(graph)
            if cur_node ==  n-1:
                ans.append(cur_path[:])
                return
            for connection in adj_list[cur_node]:
                cur_path.append(connection)
                backtrack(cur_path, connection)
                cur_path.pop()
        backtrack([0], 0)
        return ans
