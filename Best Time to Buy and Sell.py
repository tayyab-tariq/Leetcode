class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = prices[0]
        profit = 0

        for num in prices:
            profit = max(profit, num - min_price)
            min_price = min(min_price, num)
        
        return profit
        
        # profit = 0
        
        # lowest = prices[0]
        # for price in prices:
        #     if price < lowest:
        #         lowest = price
            
        #     profit = max(profit, price - lowest)

        # return profit
