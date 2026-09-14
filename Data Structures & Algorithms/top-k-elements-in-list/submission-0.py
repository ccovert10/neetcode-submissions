class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashDict = {}
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] not in hashDict:
                hashDict[nums[i]] = 1
            else:
                hashDict[nums[i]] += 1       
        hashDict = dict(sorted(hashDict.items(), key=lambda x: x[1], reverse=True))
        return list(hashDict.keys())[:k]