class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        mf = 0
        res = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            mf = max(mf, count[s[right]])
            while (right - left) + 1 - mf > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res