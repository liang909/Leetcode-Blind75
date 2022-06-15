  #O(N2) over time...
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(1,len(prices)):
            num1 = prices[i]
            for j in range(len(prices)):
                num2 = prices[j]
                if i>j: 
                    tempmax = num1-num2
                    if(tempmax > 0 and tempmax>max):
                        max = tempmax
        return max    
"""
#O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
