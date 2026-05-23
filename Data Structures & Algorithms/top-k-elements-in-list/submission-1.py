class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        a = [[] for _ in range(len(nums) + 1)]
        for i in d.keys():
            a[d[i]].append(i)
        
        op = []
        for i in range(len(nums), 0, -1):
            for num in a[i]:
                op.append(num)
                if len(op)==k:
                    return(op)


        