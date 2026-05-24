class Solution:
    def trap(self, height: List[int]) -> int:
        maxr = height[len(height)-1]
        maxl = height[0]
        tot = 0
        r = len(height)-1
        l = 0
        while l<=r:
            if maxl<maxr:
                if height[l]>=maxl:
                    maxl = height[l]
                else:
                    tot = tot + maxl-height[l]
                l+=1
            else:
                if height[r]>=maxr:
                    maxr = height[r]
                else:
                    tot = tot + maxr-height[r]
                r-=1
        return tot