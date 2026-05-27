class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        ds = [0]*26
        dw = [0]*26
        for idx, i in enumerate(s1):
            a = ord(i) - ord('a')
            b = ord(s2[idx]) - ord('a')
            ds[a] += 1
            dw[b] += 1
        win = len(s1)
        for i in range(len(s2)):
            if dw==ds:
                return True
            p = i+win
            if p>=len(s2):
                break
            a = ord(s2[i]) - ord('a')
            b = ord(s2[p]) - ord('a')
            dw[a] -= 1
            dw[b] += 1
            

        return False