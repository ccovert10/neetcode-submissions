class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, pt = [], []
        def pnc():
            if len(pt) == len(nums):
                res.append(pt.copy())
                return
            for n in nums:
                if n not in pt:
                    pt.append(n)
                    pnc()
                    pt.pop()
        pnc()
        return res