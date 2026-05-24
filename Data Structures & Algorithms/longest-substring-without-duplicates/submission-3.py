class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        r = 0
        maxlen = 0
        l=0
        for r in range(len(s)):
            curr = s[r]
            if curr in d and d[curr]>=l:
                l = d[curr] + 1
            d[curr] = r
            if maxlen<(r-l+1):
                maxlen = r-l+1

        
        return maxlen