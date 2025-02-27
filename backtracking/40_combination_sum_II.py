'''
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.
**Example 1:**
**Input:** candidates = [10,1,2,7,6,1,5], target = 8
**Output:** 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
'''
def combinationSum2(candidates, target):
    ans, cur = [],[]
    candidates.sort()
    n = len(candidates)
    def backtrack(cur, i, sum):
        if sum == target:
            ans.append(cur[:])
            return 
        if sum > target or i == n:
            return
        prev = -1  # to skip duplicates we initialize a variable to -1
        for i in range(i, n):
            # skip duplicates
            if candidates[i] == prev:
                continue
            cur.append(candidates[i])
            backtrack(cur, i+1, sum + candidates[i])
            cur.pop()
            prev = candidates[i]  # update prev to the current number so that we can check on the next iteration
    backtrack(cur, 0, 0)
    return ans

print(combinationSum2([10,1,2,7,6,1,5], 8)) ## [[1, 2, 5], [1, 7], [2, 6]]v
print(combinationSum2([1,1,1,1,1], 2)) # [[1,1]]
print(combinationSum2([1,2,3,4,5], 5)) # [[1,4],[2,3],[5]]