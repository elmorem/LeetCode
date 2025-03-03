'''
Given an integer array `nums` and an integer `k`, return `true` if it is possible to divide this array into `k` non-empty subsets whose sums are all equal.

**Example 1:**

**Input:** nums = [4,3,2,3,5,2,1], k = 4
**Output:** true
**Explanation:** It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

**Example 2:**

**Input:** nums = [1,2,3,4], k = 3
**Output:** false

> [!NOTE] algo summary
> Key Minor imporvements sort and divisibility check
> 1. this one is hard
> 2. recursive backtrack: pas in index, total and number of  subsets
> 	1. base case: 
> 		1. if k reaches 0 we have a solution
> 		2. if the total == 0 then we have a subset
> 	2. Msin recursion
> 		1. cycle through j from i to n
> 		2. if we add too much and it can't == taregt skip it
> 		3. Otherwise we add used nums[i] to True
> 		4. do the backtrack (i+1 add the value of nums[i])
> 		5. then when done we reset used[i to False]
> 		6. Finally if we make it to the end then we haven't found a solution

'''
from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        nums.sort(reverse=True)
        total = sum(nums)
        if total % k != 0:
            return False
        target = int(total / k)
        used = [False] * n
        
        def backtrack(index, total, k): 
            if k == 0:  # if we have made all the subsets
                return True
            if total == 0:  # when we hit a subset of the right size we then backtrack for the rest
                return backtrack(0, target, k - 1)
            for i in range(index, n):  # the main recusion
                if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                    continue
                if used[i] or total - nums[i] < 0: # we just skip if it has been used or the sum is too much
                    continue
                used[i] = True # we use the value and change condition
                if backtrack(i + 1, total - nums[i], k):
                    return True
                used[i] = False # we unset it
            return False # if we reach this we've gone through everything and it didn't work
        return backtrack(0, target, k)
s = Solution()
print(s.canPartitionKSubsets([4,3,2,3,5,2,1], 4)) # True
print(s.canPartitionKSubsets([1,2,3,4], 3)) # False
print(s.canPartitionKSubsets([1,2,3,4,5], 3)) # True
print(s.canPartitionKSubsets([1,2,3,4,5,6], 3)) # True