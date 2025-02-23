'''
Given an integer array `nums`, return _the number of longest increasing subsequences._

**Notice** that the sequence has to be **strictly** increasing.

**Example 1:**

**Input:** nums = [1,3,5,4,7]
**Output:** 2
**Explanation:** The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

**Example 2:**

**Input:** nums = [2,2,2,2,2]
**Output:** 5
**Explanation:** The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.

'''

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(int) # index == key, value == {len of lis, count}
        lenLIS, res = 0,0 
        for i in range(n-1, -1,-1):
            maxLen, maxCnt = 1,1  #len and count of LIS start from i
            for j in range(i+1, n):
                if nums[j] > nums[i]: # make sure increasing order
                    length, count = dp[j] # length, count of LIS start from j
                    if length +1 > maxLen:  # increment this here if we need to extend the maxLen
                        maxLen, maxCnt = length + 1, count # update length and counts
                    elif length + 1 == maxLen:
                        maxCnt += count # here we only need to update count
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif lenLIS == maxLen:
                res += maxCnt
            dp[i] = (maxLen, maxCnt)
        print(f"{ dp = }")
        return res
print(Solution().findNumberOfLIS([1,3,5,4,7])) # 2
print(Solution().findNumberOfLIS([2,2,2,2,2])) # 5
print(Solution().findNumberOfLIS([1,2,3,4,5])) # 1