'''
Given an array of strings `nums` containing `n` **unique** binary strings each of length `n`, return _a binary string of length_ `n` _that **does not appear** in_ `nums`_. If there are multiple answers, you may return **any** of them_.

**Example 1:**

**Input:** nums = ["01","10"]
**Output:** "11"
**Explanation:** "11" does not appear in nums. "00" would also be correct.

**Example 2:**

**Input:** nums = ["00","01"]
**Output:** "11"
**Explanation:** "11" does not appear in nums. "10" would also be correct.
'''
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        strSet = {s for s in nums}

        def backtrack(i, cur):
            if i == n:
                res = "".join(cur)
                return None if res in strSet else res
            res = backtrack(i+1, cur)
            if res:
                return res
            cur[i] = "1"
            res = backtrack(i+1, cur)
            if res:
                return res
            
        return backtrack(0, ["0" for x in nums])
s = Solution()
print(s.findDifferentBinaryString(["01","10"])) # "11"
print(s.findDifferentBinaryString(["00","01"])) # "11"
print(s.findDifferentBinaryString(["00","10"])) # "01"
print(s.findDifferentBinaryString(["01","11"])) # "00"

