class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        mx = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                p = prices[right] - prices[left]
                if p > mx:
                    mx = p
            right += 1
        return mx