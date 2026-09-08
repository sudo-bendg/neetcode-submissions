class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = dict()
        for i, n in enumerate(nums):
            if n in res:
                return [res[n], i]
            res[target - n] = i