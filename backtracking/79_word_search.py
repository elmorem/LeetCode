'''
Given an `m x n` grid of characters `board` and a string `word`, return `true` _if_ `word` _exists in the grid_.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

**Input:** board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
**Output:** true
'''

def exist(board, word):
    m = len(board)
    n = len(board[0])
    w = len(word)

    if m == 1 and n == 1:
        return board[0][0] == word
    
    def backtrack(pos, index):
        i, j = pos
        if index == w:
            return True
        if board[i][j] != word[index]:
            return False
        # mark as visited
        temp = board[i][j]
        board[i][j] = "#"
        # check all 4 directions
        for i_off, j_off in [(0,1), (1,0), (0,-1), (-1,0)]:
            r,c = i+i_off, j+j_off
            if 0 <= r < m and 0 <= c < n and board[r][c] != "#":
                if backtrack((r,c), index+1):
                    return True
        # unmark
        board[i][j] = temp
        return False
    
    for i in range(m):
        for j in range(n):
            if backtrack((i,j), 0):
                return True
    return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(exist([["a"]], "a"))