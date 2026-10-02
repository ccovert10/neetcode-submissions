class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        f1 = {}
        f2 = {}
        right = 0
        for c in s1:
            f1[c] = f1.get(c, 0) + 1
        if len(s1) > len(s2):
            return False
        else:
            while right < len(s2):
                # add s2[right] to f2
                f2[s2[right]] = f2.get(s2[right], 0) + 1

                # once window reaches len(s1)
                if right - left + 1 == len(s1):

                    if f1 == f2:
                        return True

                    # remove left character
                    f2[s2[left]] -= 1

                    if f2[s2[left]] == 0:
                        del f2[s2[left]]

                    left += 1

                right += 1

            return False
