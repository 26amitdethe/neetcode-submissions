class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fullp = 1
        zerocount = 0
        op = []
        for i in nums:
            if i==0:
                zerocount +=1
                continue
            fullp *=i
        if zerocount>1:
            return [0]*len(nums)
        for i in nums:
            if zerocount==1 and i!=0:
                op.append(0)
            elif zerocount==1 and i==0:
                op.append(int(fullp))
            else:
                op.append(int(fullp/i))

            
        return op
        