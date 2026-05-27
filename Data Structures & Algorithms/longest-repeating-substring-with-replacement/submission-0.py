class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        op = 0
        l = 0
        r = 1
        max_f = 0
        counts = [0]*26 
        for r in range(len(s)):
            counts[ord(s[r])-ord('A')] += 1
            if max_f<counts[ord(s[r])-ord('A')]:
                max_f = counts[ord(s[r])-ord('A')]
            if (r-l+1) - max_f >k:
                counts[ord(s[l])-ord('A')] -= 1
                l+=1
            win = (r-l+1)
            if win>op:
                op = win
        return op

