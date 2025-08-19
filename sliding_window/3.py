class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        window = set()
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            w = (r-l) +1
            longest = max(w,longest)
            window.add(s[r])
        return longest