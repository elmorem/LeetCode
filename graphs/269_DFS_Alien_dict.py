'''
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary. Now it is claimed that the strings in `words` are **sorted lexicographically** by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in `words` cannot correspond to any order of letters, return `"".`

Otherwise, return _a string of the unique letters in the new alien language sorted in **lexicographically increasing order** by the new language's rules__._ If there are multiple solutions, return _**any of them**_.

**Example 1:**

**Input:** words = ["wrt","wrf","er","ett","rftt"]
**Output:** "wertf"


> [!NOTE] Algo Summary
> KEY: We need to use topological sort
> POST ORDER DFS
> - If we ever see a situation where all the letters of a string match except one of them has one more character, but it comes second in the order, then. we retyren ""
> - The other way to see this when we represent things as a graph is that if there is a cycle it is invalid
> - For each pair of words, lets iterate through the letter as soon as we have a differeing letter, we know that whichever came from i instead of i+1, that one is first
> 

'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w }
        for i in range(len(words) - 1):  
            # we do this -1 here because we are going to be checking pairs
            # it's a better way to do it that checking that i+1 is there
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {} # False = visited, True = visited and in current path
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
