class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float('inf')
        p=0
        for price in prices:
            if price<buy_price:
                buy_price=price
            else:
                p = max(price-buy_price,p)
        return p
            
