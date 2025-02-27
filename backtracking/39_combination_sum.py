'''
Given an array of **distinct**integers`candidates` and a target integer `target`, return _a list of all **unique combinations** of_ `candidates` _where the chosen numbers sum to_ `target`_._ You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.
- as we iterate through these we are going to want to consider all the possible combinations that include the number at that index and then we can consider all the combinations of each of the other values at a given index
- and then within these we are going to have to consider all the combinations where there are 2 values at a given index, then three etc.  until the sum of those is either equal to the target or it breaks
- then also at each step (say when there are 2 2s or 3 2s, we have to add one or multiple of the other numbers )
'''

def sol (candidates, target):
    ans, sol = [], []
    n = len(candidates)

    def backtrack(i, sum):
        if sum == target:
            ans.append(sol[:])
            return
        if sum  > target or i == n:
            return
        # we can pick the number at index i
        # the two moves below can be swapped
        # we can start by picking the number at index i OR
        # not picking the number at index i
        sol.append(candidates[i])
        backtrack(i, sum + candidates[i])
        # we can skip the number at index i
        sol.pop()
        backtrack(i+1, sum)
    backtrack(0, 0)
    return ans

print(sol([2,3,6,7], 7)) # [[2,2,3],[7]]
print(sol([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
print(sol([2], 1)) # []
print(sol([1], 1)) # [[1]]