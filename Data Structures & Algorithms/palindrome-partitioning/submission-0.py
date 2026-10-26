class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, pal = [], []
        def bt(start):
            if start == len(s):                         #*
                res.append(pal.copy())
                return
            for end in range(start, len(s)):
                substring = s[start:end+1]              #*    
                if substring != substring[::-1]:
                    continue
                pal.append(substring)
                bt(end+1)
                pal.pop()
        bt(0)
        return res
