import gfg.stockBuyAndSell
from gfg import countsubarraylessthank

def print_start(func):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Starting solution check: {func}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    debug_class = 'gfg.stockBuyAndSell.stockBuyAndSell'
    print_start(debug_class)
    test_array = [1, 2, 3, 4]
    n = 4
    k = 10
    answer = gfg.countSubarrayLessThanK.subArrayLessThanK(test_array, n, k)
    print(answer)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
