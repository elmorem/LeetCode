class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        cuts = [0]* (n+1)
        for i in range(n+1):
            cuts[i] = i-1
        def expand(l,r):
            while l >=0 and r <n and s[l] == s[r]:
                cuts[r+1] = min(cuts[r+1], cuts[l] + 1)
                l -=1
                r+=1
        for center in range(n):
            expand(center, center)
            expand(center, center+1)
        return cuts[n]
if __name__ == "__main__":
    sol = Solution()
    s1 = "aab"
    print(sol.minCut(s1))  # Expected output: 1
    s2 = "a"
    print(sol.minCut(s2))  # Expected output: 0
    s3 = "ab"
    print(sol.minCut(s3))  # Expected output: 1
    s4 = "racecar"
    print(sol.minCut(s4))  # Expected output: 0
    s5 = "noonabbad"
    print(sol.minCut(s5))  # Expected output: 2