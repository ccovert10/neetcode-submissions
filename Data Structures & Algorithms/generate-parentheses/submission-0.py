class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bt(s, op, cl):
            if len(s) == 2*n:
                res.append(s)
                return
            if op < n:
                bt(s + '(', op + 1, cl)
            if cl < op:
                bt(s + ')', op, cl + 1)
        bt('', 0, 0)
        return res