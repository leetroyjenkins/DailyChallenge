def max_index_diff(n, arr):
    """
    Name: Maximum Index
    URL: https://practice.geeksforgeeks.org/problems/maximum-index3307/1
    gfg Daily for 7/3/2013

    """
    '''max_val = 0
    x = n
    while x > max_val:
        for ind_i, i in enumerate(arr):
            x -= ind_i
            for ind_j, j in reversed(list(enumerate(arr))):
                if i <= j and (ind_j - ind_i) >= max_val:
                    max_val = ind_j - ind_i
        return max_val'''

    max_val = 0
    x = n
    while x > max_val:
        for ind_i, i in enumerate(arr):
            x -= ind_i
            for ind_j, j in reversed(list(enumerate(arr))):
                if i <= j and (ind_j - ind_i) >= max_val:
                    max_val = ind_j - ind_i
        return max_val
