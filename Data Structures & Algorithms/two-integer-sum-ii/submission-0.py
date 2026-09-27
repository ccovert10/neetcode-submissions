class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashDict = {}
        for i, n in enumerate(numbers):
            need = target - n
            if need not in hashDict:
                hashDict[n] = i
            else:
                l1, l2 = hashDict[need] + 1, i+1
                return list([l1, l2])