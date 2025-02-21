'''
You are given an integer array `nums` and an integer `target`.

You want to build an **expression** out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.

- For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `"+2-1"`.

Return the number of different **expressions** that you can build, which evaluates to `target`.

**Example 1:**

**Input:** nums = [1,1,1,1,1], target = 3
**Output:** 5
**Explanation:** There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
'''
def findTargetSumWays(nums, target):
    dp = {} # (index, total) --> num ways
    # return num ways to reach target
    def backtrack(i, total):
        if i == len(nums):
            return 1 if total == target else 0
        if (i, total) in dp:
            return dp[(i, total)]
        # recursive relationship where we are trying both the pos and the negative for each i+1
        dp[(i,total)] = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])
        return dp[(i,total)]
    return backtrack(0, 0)
print(findTargetSumWays([1,1,1,1,1], 3)) # 5
print(findTargetSumWays([1], 1)) # 1
print(findTargetSumWays([1], 0)) # 0
print(findTargetSumWays([1,2,3], 3)) # 0