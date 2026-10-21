class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, ss = [], []
        nums.sort()
        def sub(i):
            res.append(ss.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                ss.append(nums[j])
                sub(j+1)
                ss.pop()
        sub(0)
        return res