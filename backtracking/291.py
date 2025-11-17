class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        mapping = {}
        used = set()
        def dfs(pi, si):
            if pi == len(pattern) and si == len(s):
                return True
            if pi == len(pattern) or si == len(s):
                return False
            ch = pattern[pi]
            if ch in mapping:
                word = mapping[ch]
                if not s.startswith(word, si):
                    return False
                return dfs(pi +1, si +len(word))
            remaining = len(pattern) - pi
            max_end = len(s) - (remaining-1)
            for end in range(si+1, max_end+1):
                cand = s[si:end]
                if cand in used:
                    continue
                mapping[ch] = cand
                used.add(cand)
                if dfs(pi+1, end):
                    return True
                del mapping[ch]
                used.remove(cand)
            return False
        return dfs(0,0)
if __name__ == "__main__":
    solution = Solution()
    print(solution.wordPatternMatch("abab", "redblueredblue"))  # Expected output: True
    print(solution.wordPatternMatch("aaaa", "asdasdasdasd"))    # Expected output: True
    print(solution.wordPatternMatch("aabb", "xyzabcxzyabc"))    # Expected output: False
    print(37%3)