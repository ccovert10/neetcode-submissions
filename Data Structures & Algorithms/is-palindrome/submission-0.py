class Solution:
    def isPalindrome(self, s: str) -> bool:
        validstr = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        revstr = validstr[::-1]
        return revstr == validstr