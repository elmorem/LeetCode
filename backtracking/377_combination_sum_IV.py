'''
Given an array of **distinct** integers `nums` and a target integer `target`, return _the number of possible combinations that add up to_ `target`.

The test cases are generated so that the answer can fit in a **32-bit** integer.

**Example 1:**

**Input:** nums = [1,2,3], target = 4
**Output:** 7
**Explanation:**
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

**Example 2:**

**Input:** nums = [9], target = 3
**Output:** 0
'''

def combinationSum4(nums, target):
    dp = {0:1}
    for total in range(1, target+1):
        for num in nums:
            dp[total] = dp.get(total-num, 0) + dp.get(total, 0)
    return dp[target]
print(combinationSum4([1,2,3], 4)) # 7
print(combinationSum4([9], 3)) # 0