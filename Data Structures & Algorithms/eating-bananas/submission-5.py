class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            tot = 0
            for p in piles:
                tot += (p + mid - 1) // mid
            if tot <= h:
                right = mid
            else:
                left = mid + 1
        return left