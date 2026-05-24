class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights)-1
        vol = 0
        while s<e:
            start = heights[s]
            end = heights[e]
            cap = min(start, end)*(e-s)
            if cap>vol:
                vol = cap
            if start<end:
                s+=1
            elif end<=start:
                e-=1

        return vol