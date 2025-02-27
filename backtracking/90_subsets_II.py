'''
Given an integer array `nums` that may contain duplicates, return _all possible_ _subsets_
_(the power set)_.The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1:**

**Input:** nums = [1,2,2]
**Output:** [[],[1],[1,2],[1,2,2],[2],[2,2]]
INTUITION:  
'''
def subsetsWithDups(nums):
    n = len(nums)
    res = []
    nums.sort() # sort the array to make sure duplicates are next to each other
    # This is the key move so that we can avoid dupilicates
    def backtrack(i, subset):
        # we hit the base case when we have gone through the individes
        if i == n:
            res.append(subset[:])
            return
        # all subsets that include nums[i]
        subset.append(nums[i])
        backtrack(i+1, subset)
        subset.pop()
        # all subsets that don't include nums[i]
        # skip duplicates
        while i+1 < n and nums[i] == nums[i+1]:
            i += 1
        backtrack(i+1, subset)

    backtrack(0, [])
    return res
print(subsetsWithDups([1,2,2])) # [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(subsetsWithDups([1,2,3,4])) # [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(subsetsWithDups([1,2,3,4,5])) # [[],[1],[1,2],[1,2,2],[2],[2,2]]