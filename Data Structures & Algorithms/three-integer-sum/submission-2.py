class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        b = 0
        c = 0
        op = []
        nums.sort()
        for idx, i in enumerate(nums):
            if idx>0 and i==nums[idx-1]:
                continue
            b = idx+1
            c = len(nums)-1
            while b<c:
                s = nums[b] + nums[c]
                if s>-i:
                    c-=1
                elif s<-i:
                    b+=1
                else:
                    op.append([nums[idx], nums[b], nums[c]])
                    c-=1
                    b+=1
                    while nums[b]==nums[b-1] and b<c:
                        b+=1


        return op