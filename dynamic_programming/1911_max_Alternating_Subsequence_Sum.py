'''
The **alternating sum** of a **0-indexed** array is defined as the **sum** of the elements at **even** indices **minus** the **sum** of the elements at **odd** inPartition Equal Subset sumdices.

- For example, the alternating sum of `[4,2,5,3]` is `(4 + 5) - (2 + 3) = 4`.

Given an array `nums`, return _the **maximum alternating sum** of any subsequence of_ `nums` _(after **reindexing** the elements of the subsequence)_.

A **subsequence** of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, `[2,7,4]` is a subsequence of `[4,2,3,7,2,1,4]` (the underlined elements), while `[2,4,2]` is not.

**Example 1:**

**Input:** nums = [4,2,5,3]
**Output:** 7
**Explanation:** It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.
'''
def maxAlternatingSum(nums):
    dp = {} # key = index,  even boolean val = max sum
    def backtrack(i, even):
        if i == len(nums):
            return 0 # i'm not certain why this is 0
        if (i,even) in dp:
            return dp[(i,even)]
        total = nums[i] if even else (-1*nums[i])
        # recursive relationship
        dp[i,even] = max(total + backtrack(i+1, not even), backtrack(i+1, even))
        return dp[i,even]
    return backtrack(0, True)

print(maxAlternatingSum([4,2,5,3])) # 7
print(maxAlternatingSum([1,2,3,4])) # 4
print(maxAlternatingSum([5,6,7,8])) # 8
print(maxAlternatingSum([6,2,1,2,4,5])) # 10
print(maxAlternatingSum([1,3,2,4])) # 5