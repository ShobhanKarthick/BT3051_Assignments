# no libraries are allowed

""" Add your functions here """

def optimal_investment_time_series(time_series):
    """
    (list of int) -> int

    >>> optimal_investment_time_series([3,3,0,1,2,5,2,2,4,2,7,0])
        10
    """

    max_transaction = 2         # Maximum 2 transactions can be done

    # Initilaise the profit table
    profitTab = [[0 for i in range(len(time_series) + 1)] for j in range(max_transaction + 1)]

    # We want to maximise the difference between the buying and selling of stocks
    for i in range(1, max_transaction + 1):
        maxDiff = - max(time_series)
        for j in range(1, len(time_series)):

            # Maximum difference is taken from max of previous difference and new difference
            maxDiff = max(maxDiff, profitTab[i-1][j-1] - time_series[j-1])

            # Maximum profit is taken from the max of previous profit and new profit
            profitTab[i][j] = max(profitTab[i][j-1],  time_series[j] + maxDiff)

    return (profitTab[max_transaction][len(time_series)-1])



print(optimal_investment_time_series([3, 3, 5, 0, 0, 3, 1, 4]))
print(optimal_investment_time_series([3,3,0,1,2,5,2,2,4,2,7,0]))
print(optimal_investment_time_series([1, 2, 3, 4, 5]))
print(optimal_investment_time_series([5, 4, 3, 2, 1]))


        

