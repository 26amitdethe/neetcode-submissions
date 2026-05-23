class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        fs = {}
        ft = {}
        for i in range(len(s)):
            if s[i] in fs:
                fs[s[i]] += 1
            else:
                fs[s[i]] = 1
            if t[i] in ft:
                ft[t[i]] += 1
            else:
                ft[t[i]] = 1
        for i in s:
            if i not in ft:
                return False
            if fs[i] != ft[i]:
                return False
        return True


            