''' You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0. '''

#Solution 1 - O(n) solution.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Initialize two pointers left and right and max_profit variable.
        l, r = 0 ,1
        max_pro = 0
        # Initializing loop
        while r < len(prices):
            #If max profit < diff of price on right pointer to left pointer
            max_pro = max(max_pro, prices[r] - prices[l])
            #If right pointer price is less than left pointer price.
            if prices[r] < prices[l]:
                newr = r+1
                l = r
                r = newr
            else:
                r += 1
        #Returning the max_profits
        return max_pro
