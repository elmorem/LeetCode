'''
Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


![](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

'''
def letterCombinations(digits):
    if not digits:
        return []
    num_to_let = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    ans, sol = [], []
    n = len(digits)
    def backtrack(i):
        if i == n:
            ans.append("".join(sol))
            return
        for char in num_to_let[digits[i]]:
            sol.append(char)
            backtrack(i + 1)
            sol.pop()
    backtrack(0)
    return ans

print(letterCombinations("23")) # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print("================================")
print(letterCombinations("2")) # ['a', 'b', 'c']
print("================================")
print(letterCombinations("")) # []
print("================================")
print(letterCombinations("2345")) # ['adgj', 'adgk', 'adgl', 'adhj', 'adhk', 'adhl', 'adij', 'adik', 'adil', 'aegj', 'aegk', 'aegl', 'aehj', 'aehk', 'aehl', 'aeij', 'aeik', 'aeil', 'afgj', 'afgk', 'afgl', 'afhj', 'afhk', 'afhl', 'afij', 'afik', 'afil', 'bdgj', 'bdgk', 'bdgl', 'bdhj', 'bdhk', 'bdhl', 'bdij', 'bdik', 'bdil', 'begj', 'begk', 'begl', 'behj', 'behk', 'behl', 'beij', 'beik', 'beil', 'bfgj', 'bfgk', 'bfgl', 'bfhj', 'bfhk', 'bfhl', 'bfij', 'bfik', 'bfil', 'cdgj', 'cdgk', 'cdgl', 'cdhj', 'cdhk', 'cdhl', 'cdij', 'cdik', 'cdil', 'cegj', 'cegk', 'cegl', 'cehj', 'cehk', 'cehl', 'ceij', 'ceik', 'ceil', 'cfgj', 'cfgk', 'cfgl', 'cfhj', 'cfhk', 'cfhl', 'cfij', 'cfik', 'cfil']