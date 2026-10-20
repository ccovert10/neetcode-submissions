class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        def bt(i, target):
            if target == 0:
                res.append(path.copy())
                return
            if target < 0:
                return
            for j in range(i, len(nums)):
                path.append(nums[j])    
                bt(j, target - nums[j])
                path.pop()
        bt(0, target)
        return res