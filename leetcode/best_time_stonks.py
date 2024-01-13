# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a 
# different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve
# any profit, return 0.

# I added "What if you were asked to tell which buy/sell day?"
def max_profit(prices):
    if prices == sorted(prices, reverse=True):
        return 0, None, None
    if not prices or len(prices) < 2:
        return 0
    sell_day = 0
    buy_day = 0
    min_price = prices[0]
    max_profit = 0
    previous_max_profit = 0

    for idx, price in enumerate(prices[1:]):
        max_profit = max(max_profit, price - min_price)
        if max_profit != previous_max_profit: 
            sell_day = idx
        min_price = min(min_price, price)
        buy_day = prices.index(min_price)
        previous_max_proft = max_profit
    
    return max_profit, buy_day, sell_day

prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
max_profit_num, buy_day, sell_day = max_profit(prices)

print(f"You should buy on day {buy_day}")
print(f"You should sell on day {sell_day}")
print(f"Your max profit will be {max_profit_num}")