'''
You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. Each `Ai` or `Bi` is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [Cj, Dj]` represents the `jth` query where you must find the answer for `Cj / Dj = ?`.

Return _the answers to all queries_. If a single answer cannot be determined, return `-1.0`.

**Note:** The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

**Note:** The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

**Example 1:**

**Input:** equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
**Output:** [6.00000,0.50000,-1.00000,1.00000,-1.00000]
**Explanation:** 
Given: _a / b = 2.0_, _b / c = 3.0_
queries are: _a / c = ?_, _b / a = ?_, _a / e = ?_, _a / a = ?_, _x / x = ?_ 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

'''
from typing import List
import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list) # map {a: [[b, 2], [c, 1]]}
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])

        def dfs(start, target, accW, visited):
            if start not in adj or target not in adj or start in visited:
                return -1
            if start == target:
                return accW
            visited.add(start)
            for n, w in adj[start]:
                res = dfs(n, target, accW*w, visited)
                if res != -1:
                    return res
            return res

        return [dfs(q[0], q[1], 1, set()) for q in queries]
# Test cases
sol = Solution()
print(sol.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])) # [6.00000,0.50000,-1.00000,1.00000,-1.00000]
print(sol.calcEquation([["a","b"],["b","c"],["c","d"]], [2.0,3.0,4.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])) # [6.00000,0.50000,-1.00000,1.00000,-1.00000]
print(sol.calcEquation([["a","b"],["b","c"],["c","d"]], [2.0,3.0,4.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])) # [6.00000,0.50000,-1.00000,1.00000,-1.00000]