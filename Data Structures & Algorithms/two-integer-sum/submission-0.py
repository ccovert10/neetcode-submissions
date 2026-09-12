class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevEle = {}
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in prevEle:
                return [prevEle[diff], i]
            prevEle[n] = i
        return