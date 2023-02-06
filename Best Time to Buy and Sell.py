class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            
            profit = max(profit, price - lowest)

        return profit




# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maximum = 0
        
#         while(len(prices)>1):
#             min_value = min(prices)
#             min_index = prices.index(min_value)
            
#             arr = prices[min_index:len(prices)]
#             max_value = max(arr)
            
#             prices = prices[0:min_index]

#             if maximum < max_value-min_value:
#                 maximum = max_value-min_value
            
#         return maximum
