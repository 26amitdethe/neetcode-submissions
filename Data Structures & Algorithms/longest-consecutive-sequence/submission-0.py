class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            a[i] = True
        
        c = 1
        longest = 0
        for idx, i in enumerate(nums):
            p = i
            if (i-1) in a:
                continue
            while True:
                p+=1
                if p in a:
                    c+=1
                else:
                    break
            if c>longest:
                longest = c
            c=1

        return longest