'''
Given two integers `n` and `k`, return _all possible combinations of_ `k` _numbers chosen from the range_ `[1, n]`.

You may return the answer in **any order**.
'''
from typing import List

def combine( n: int, k: int) -> List[List[int]]:
    ans = []
    sol = []
    def backtrack(x):
        if len(sol) == k:
            ans.append(sol[:])
            return
        left = x
        still_need = k - len(sol)
        print(f"{left = }" )
        print(f"{still_need = }")
        if left > k - len(sol):
            backtrack(x-1)
        sol.append(x)
        backtrack(x-1)
        sol.pop()
    backtrack(n)
    return ans

print(combine(4,2)) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print("-------------")
print(combine(4,3)) # [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
print("-------------")
print(combine(4,4)) # [[1,2,3,4]]