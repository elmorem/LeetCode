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
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # Expected output: 3
    print(solution.lengthOfLongestSubstring("bbbbb"))     # Expected output: 1
    print(solution.lengthOfLongestSubstring("pwwkew"))    # Expected output: 3
    print(solution.lengthOfLongestSubstring(""))           # Expected output: 0
    print(solution.lengthOfLongestSubstring(" "))          # Expected output: 1
