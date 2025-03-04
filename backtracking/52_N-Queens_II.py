'''
The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return _the number of distinct solutions to the **n-queens puzzle**_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

**Input:** n = 4
**Output:** 2
**Explanation:** There are two distinct solutions to the 4-queens puzzle as shown.

**Example 2:**

**Input:** n = 1
**Output:** 1

'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        res,col,pos,neg=0,set(),set(),set()
        def backtracking(r):
            if n==r:
                nonlocal res
                res+=1
            for c in range(n):
                if c in col or (c+r) in pos or (r-c) in neg:
                    continue
                col.add(c)
                pos.add(c+r)
                neg.add(r-c)
                backtracking(r+1)
                col.remove(c)
                pos.remove(c+r)
                neg.remove(r-c)
                
        backtracking(0)

        return res

print(Solution().totalNQueens(4)) # 2
print(Solution().totalNQueens(1)) # 1
print(Solution().totalNQueens(5)) # 10
print(Solution().totalNQueens(6)) # 4
