def stockBuyAndSell(prices, n):
    '''

    :param self:
    :param n:
    :param prices:
    :return:
    '''
    #
    profit = 0
    i = 0
    while i <= n-2:
        if (prices[i+1] - prices[i]) > 0:
            profit += prices[i+1] - prices[i]
        i += 1
    return profit