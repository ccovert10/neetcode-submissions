class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        candidates.sort()
        def bt(i, target):
            if target == 0:
                res.append(path.copy())
                return
            if target < 0:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])
                bt(j+1, target - candidates[j])
                path.pop()
        bt(0, target)
        return res