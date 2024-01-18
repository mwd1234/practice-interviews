# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def max_profit(prices):
    if prices == sorted(prices, reverse=False): 
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit

prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
max_profit_num = max_profit(prices)

print(f"Your max profit will be {max_profit_num}")