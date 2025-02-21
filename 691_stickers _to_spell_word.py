'''
SEE ALSO WORD Break 139
We are given `n` different types of `stickers`. Each sticker has a lowercase English word on it.

You would like to spell out the given string `target` by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

Return _the minimum number of stickers that you need to spell out_ `target`. If the task is impossible, return `-1`.

**Note:** In all test cases, all words were chosen randomly from the `1000` most common US English words, and `target` was chosen as a concatenation of two random words.

**Example 1:**

**Input:** stickers = ["with","example","science"], target = "thehat"
**Output:** 3
**Explanation:**
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
'''

def minStickers(stickers, target):
    stickCount = []
    for i, s in enumerate(stickers):
        stickCount.append({})
        for c in s:
            stickCount[i][c] = stickCount[i].get(c, 0) + 1
    dp = {} # key substring target, value min stickers
    # return min stickers to form target
    def backtrack(t, stick):
        if t in dp:
            return dp[t]
        res = 1 if stick else 0
        remain_letters = ""
        for c in t:
            if c in stick and stick[c] > 0:
                stick[c] -= 1
            else:
                remain_letters += c
        if remain_letters:
            used = float("inf")
            for s in stickCount:
                if remain_letters[0] not in s:
                    continue
                used = min(used, backtrack(remain_letters, s.copy()))
            dp[remain_letters] = used    
            res += used
        return res
    ans = backtrack(target, {})
    return ans if ans < float("inf") else -1
print(minStickers(["with","example","science"], "thehat")) # 3
print(minStickers(["notice", "possible"], "basicbasic")) # -1
print(minStickers(["h", "e", "l", "l", "o"], "hello")) # 5
print(minStickers(["a", "b", "c"], "abc")) # 3
print(minStickers(["a", "b", "c"], "abcd")) # -1