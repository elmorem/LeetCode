'''
Given a string `s`, partition `s` such that every 
substring of the partition is a **palindrome**. Return _all possible palindrome partitioning of_ `s`.

**Example 1:**
**Input:** s = "aab"
**Output:** [["a","a","b"],["aa","b"]]
INTUITION:   
1. recursive backtracking
2. insuide backtrack basecase is going to be a palindrome check
3. run basic backtracking on subsets to get all the substrings
'''
class Solution:
    def check_pal(self, s, i, j):
        while i <=j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def partition(self, s):
        ans, sol = [], []
        n = len(s)
        def backtrack(i):
            if i == len(s):
                ans.append(sol[:])
                return
            for i in range(i, n):
                if self.check_pal(s, i, j):
                    sol.append(s[i:j+1])
                    backtrack(j+1)
                    sol.pop()
        backtrack(0)
        return ans
    
s = Solution()
print(s.partition("aab")) # [["a","a","b"],["aa","b"]]
print(s.partition("a")) # [["a"]]
print(s.partition("ab")) # [["a","b"]]