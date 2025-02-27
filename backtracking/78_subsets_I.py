'''
Given an integer array `nums` of **unique** elements, return _all possible_ 

_subsets_ _(the power set)_.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1:**
**Input:** nums = [1,2,3]
**Output:** [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''

def subsets(nums):
    n = len(nums)
    res, sol = [], []
    def backtrack(i):
        # we hit the base case when we have gone through the individes
        if i == n:
            res.append(sol[:])
            return
        # don't pick nums[i]
        backtrack(i+1)
        # pick nums[i]
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()

    backtrack(0)
    return res
print(subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(subsets([1,2,3,4])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3],[4],[1,4],[2,4],[1,2,4],[3,4],[1,3,4],[2,3,4],[1,2,3,4]]