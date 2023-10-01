from gfg import boundarytraversalofmatrix
def print_start(func):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Starting solution check: {func}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    debug_class = 'gfg.boundarytraversalofmatrix'
    print_start(debug_class)
    test_array = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15,16]]
    n = 4
    m = 4
    answer = boundarytraversalofmatrix.boundaryTraversal(test_array, n , m)
    print(answer)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
