'''
Given a string `s`, you can transform every letter individually to be lowercase or uppercase to create another string.

Return _a list of all possible strings we could create_. Return the output in **any order**.

**Example 1:**

**Input:** s = "a1b2"
**Output:** ["a1b2","a1B2","A1b2","A1B2"]

**Example 2:**

**Input:** s = "3z4"
**Output:** ["3z4","3Z4"]

> [!NOTE] Algo Summary
> KEY:  note how we are using the for loop a in ans to construct the strings. we first save it to temp, then move it to ans, then use each of these to add the new character

'''
from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]
        for c in s:
            tmp = [] # we are going to build up temp 
            if c.isalpha():
                for a in ans:   # not sure I understand how this is working
                                # this is how we are mimicing recursion
                    print(f"a in ans alpha {ans = } ")
                    tmp.append(a+c.lower())
                    tmp.append(a+c.upper()) # whenever we have a character we append 2 different chars
            else:
                for a in ans:
                    print(f"a in ans number {ans = } ")
                    tmp.append(a+c) 
            print(f"{tmp =}")
            ans = tmp
        print(f"{ans = }")    
        return ans            