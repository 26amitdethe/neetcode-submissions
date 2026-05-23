class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op = {}
        for i in strs:
            a = self.makefreqmap(i)
            if not op.get(a):
                op[a] = [i]
            else:
                op[a].append(i)

        return list(op.values())

    def makefreqmap(self, word):
        wt = [0]*26
        for i in word:
            a = ord(i) - ord('a')
            wt[a] += 1
        return tuple(wt)

    #     op = []
    #     temp = []
    #     visited = set()
    #     for i,s1 in enumerate(strs):
    #         if i in visited:
    #             continue
    #         temp = []
    #         temp.append(s1)
    #         for j,s2 in enumerate(strs[i+1::]):
    #             if len(s1)==len(s2) and self.makefreqmap(s1)==self.makefreqmap(s2):
    #                 temp.append(s2)
    #                 visited.add(j+i+1)
    #         op.append(temp)

    #     # print(op)
    #     return op

    # def makefreqmap(self, word):
    #     d = {}
    #     for i in word:
    #         d[i] = d.get(i, 0) + 1
    #     return d