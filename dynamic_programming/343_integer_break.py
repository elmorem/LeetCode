'''
Given an integer `n`, break it into the sum of `k` **positive integers**, where `k >= 2`, and maximize the product of those integers.

Return _the maximum product you can get_.

**Example 1:**

**Input:** n = 2
**Output:** 1
**Explanation:** 2 = 1 + 1, 1 × 1 = 1.

**Example 2:**

**Input:** n = 10
**Output:** 36
**Explanation:** 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

'''


```
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        def dfs(num):
            if num in dp:
                return dp[num]
            dp[num] = 0 if num == n else num
            for i in range(1,num):
                val = dfs(i)*dfs(num-i)
                dp[num] = max(val, dp[num])
            return dp[num]
        return dfs(n)
        
        
        '''
        my solution here works but the time complexity is too high
        sol = []
        ans = [0]
        candidates = [x for x in range(1,n+1)]
        n = len(candidates)
        def backtrack(i, sum):
            if sum == n and len(sol) >=2:
                prod = math.prod(sol)
                ans[0] = max(prod, ans[0])
                return
            if sum > n or i ==n:
                return
            backtrack(i+1, sum)
            sol.append(candidates[i])
            backtrack(i, sum + candidates[i])
            sol.pop()
        backtrack(0,0)
        # print(f"{ans = }")

        return ans[0]
        '''