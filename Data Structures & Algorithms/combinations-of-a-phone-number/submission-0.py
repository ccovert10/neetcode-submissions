class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        nta = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        if not len(digits):
            return []
        if len(digits) == 1:
            return [c for c in nta.get(int(digits[0]), '')]
        for c in nta[int(digits[0])]:
            for s in self.letterCombinations(digits[1:]):
                res.append(c+s)
        return res