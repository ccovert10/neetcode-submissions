class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 
        nums = sorted(nums)
        return nums[0]