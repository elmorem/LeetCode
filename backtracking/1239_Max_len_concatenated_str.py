'''
You are given an array of strings `arr`. A string `s` is formed by the **concatenation** of a **subsequence** of `arr` that has **unique characters**.

Return _the **maximum** possible length_ of `s`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

**Example 1:**

**Input:** arr = ["un","iq","ue"]
**Output:** 4
**Explanation:** All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

**Example 2:**

**Input:** arr = ["cha","r","act","ers"]
**Output:** 6
**Explanation:** Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

> [!NOTE] Algo Summary
> KEY: use a helper function to do the overlap checking Use counter to check for duplicates
> 1. recursive function -- we are returning the max of including and not including
> 	1. basecase: once we've gone through the array
> 	2. if there is no overlap then we do our backtracking checking where we choose arr[i] and not choosing it
'''
from typing import List
from collections import Counter

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = []
        included = set()
        n = len(arr)
        def overlap(included, s):
            c = Counter(included) + Counter(s)
            return max(c.values()) > 1  # if it is in the counter object more than once

        def backtrack(i):
            if i == n:
                return len(included)
            res = 0
            if not overlap(included, arr[i]): # include it
                for c in arr[i]:
                    included.add(c)
                res = backtrack(i+1) # res = with it included
                for c in arr[i]:
                    included.remove(c)
            return max(res, backtrack(i+1)) # this is basically the max of 
								            # including and not including
        return backtrack(0)
