class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevValue = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in prevValue:
                return [prevValue[difference], i]
            prevValue[n] = i