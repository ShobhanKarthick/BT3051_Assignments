# no libraries are allowed

def totalProfit(stocksNum, price_2011, price_2021):
    """
    Calculates the total profit given an array of 
    number of stocks bought in 2011
    """

    profit = 0
    n = len(stocksNum)

    for i in range(n):
        profit += stocksNum[i]*(price_2021[i] - price_2011[i])

    return profit

def optimal_investment_stocks_selection(price_2011, price_2021, investment_amount, n):
    """
    (list of int), (list of int), (int), (int) -> (list of int)

    >>> optimal_investment_stocks_selection([1000,1000,1800,100,1200], [3900, 1300, 4700, 120, 4500], 3000, 5)
        [3, 0, 0, 0, 0]
    """
    if len(price_2011) != n or len(price_2021) != n:
        raise("Incorrect Input!")

    # Initialisation of the Stock selection table
    stockSelTab = [[0 for i in range(n)] for j in range(investment_amount + 1)]

    # The table gets a value of 1 when the stock is present in the input
    for i in range(n):
        stocks = [0 for i in range(n)]
        stocks[i] = 1

        if(totalProfit(stockSelTab[price_2011[i]], price_2011, price_2021) < totalProfit(stocks, price_2011, price_2021)):
            stockSelTab[price_2011[i]] = stocks

    # We update the StockSelTab only if the i-value is greater than 2011 price else we use the previous row
    for i in range(investment_amount + 1):
        for j in range(n):
            yearProfit = price_2021[j]-price_2011[j]
            if (i > price_2011[j] and totalProfit(stockSelTab[i], price_2011, price_2021) < totalProfit(stockSelTab[i - price_2011[j]], price_2011, price_2021) + yearProfit):
                    stocks = stockSelTab[i-price_2011[j]].copy()
                    stocks[j] += 1
                    stockSelTab[i] = stocks

    return (stockSelTab[investment_amount])

print(optimal_investment_stocks_selection([1000,1000,1800,100,1200], [3900, 1300, 4700, 120, 4500], 3000, 5))
