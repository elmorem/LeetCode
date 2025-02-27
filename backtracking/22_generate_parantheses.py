'''
Given `n` pairs of parentheses, write a function to _generate all combinations of well-formed parentheses_.

**Example 1:**

**Input:** n = 3
**Output:** ["((()))","(()())","(())()","()(())","()()()"]
'''

def generateParenthesis(n):
    ans, sol = [], []
    def backtrack(openn, close):
        # once we have 6
        if len(sol) == 2*n:
            ans.append("".join(sol))
            return
        if openn < n:
            sol.append("(")
            backtrack(openn+1, close)
            sol.pop()
        if close < openn:
            sol.append(")")
            backtrack(openn, close+1)
            sol.pop()
    backtrack(0, 0)
    return ans
print(generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(generateParenthesis(1)) # ["()"]
print(generateParenthesis(2)) # ["(())","()()"]