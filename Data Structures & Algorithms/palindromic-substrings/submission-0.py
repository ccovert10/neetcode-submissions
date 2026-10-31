class Solution:
    def countSubstrings(self, s: str) -> int:
        if not len(s):
            return 0
        if len(s) == 1:
            return 1
        l = []
        strLen = 0
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > strLen:
                    l.append(s[left:right+1])
                left -= 1
                right += 1
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > strLen:
                    l.append(s[left:right+1])
                left -= 1
                right += 1
        return len(l)