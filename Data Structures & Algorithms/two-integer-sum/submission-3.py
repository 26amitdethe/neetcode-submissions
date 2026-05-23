class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        k = {}
        for i, n in enumerate(nums):
            k[n] = i
        for i, n in enumerate(nums):
            a = target - n
            if a in k and k[a] != i:
                return [i, k[a]]
        return []