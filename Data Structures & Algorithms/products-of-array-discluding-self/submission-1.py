class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # fullp = 1
        # zerocount = 0
        # op = []
        # for i in nums:
        #     if i==0:
        #         zerocount +=1
        #         continue
        #     fullp *=i
        # if zerocount>1:
        #     return [0]*len(nums)
        # for i in nums:
        #     if zerocount==1 and i!=0:
        #         op.append(0)
        #     elif zerocount==1 and i==0:
        #         op.append(int(fullp))
        #     else:
        #         op.append(int(fullp/i))

            
        # return op

        lp = 1
        rp = 1
        r = []
        l = []
        op = []

        for i in nums:
            l.append(lp)
            lp = lp*i
        for i in nums[::-1]:
            r.insert(0, rp)
            rp = rp*i
        for i in range(len(nums)):
            op.append(r[i]*l[i])

        
        # print(op)
        return op
        