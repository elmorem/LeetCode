'''
Given a string `s`, return _the number of **palindromic substrings** in it_.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

**Example 1:**

**Input:** s = "abc"
**Output:** 3
**Explanation:** Three palindromic strings: "a", "b", "c".

**Example 2:**

**Input:** s = "aaa"
**Output:** 6
**Explanation:** Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''
### Intutiion here to get the time complexity down to
# n2 is to check from the center of the palidrome
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            l, r = i, i
            while l >=0 and r < n and s[r] == s[l]:
                count +=1
                l -=1
                r+=1
            l = i
            r = i+1
            while l >=0 and r < n and s[r] == s[l]:
                count +=1
                l -=1
                r+=1
        return count
'''
#############
#my first take
# works bu too slow
# time omplexity of this one is n3
class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalidrome(sub):
            i = 0
            j = len(sub)-1
            while i <j:
                if sub[i] != sub[j]:
                    return False
                elif sub[i] == sub[j]:
                    i +=1
                    j -= 1
            return True
        count = 0
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                sub = s[i:j+1]
                if isPalidrome(sub):
                    count +=1
                else:
                    continue
        return count

        '''
# print(countSubstrings(0, "abc")) # 3
# print(countSubstrings(0, "aaa")) # 6
# print(countSubstrings(0, "aaaa")) # 10