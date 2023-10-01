def subArrayLessThanK(a, n, k):
    '''

    :param a: An array
    :param n: Length of the array
    :param k: The upper bound
    :return: the product of contiguous arrays elements that are less than k
    '''
    prod = 0

    for i in range(n):
        left_counter = i
        running_prod = 0

        while running_prod < k and a[left_counter] < n:
            running_prod += a[left_counter]
            prod += 1
            left_counter += 1

    return