def columnNameFromAGivenColumnNumber(n):
    #https://practice.geeksforgeeks.org/problems/column-name-from-a-given-column-number4244/1
    # Count how many times is needed to divide by 26 before getting less than
    # 26.
    # eg. n = 100
    # 100 / 26 = 3.84615...
    # The first place is 3. 3 = C
    # The remainder is 22 100 %26 = 22. 22 = V
    # 100 = CV
    r = n % 26
    charlst = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    num = [i for i in range(1, 27)]
    alphadict = dict(zip(num, charlst))
    colnum = []

    while n > 26:
        r = n % 26
        if r == 0:
            for i in range(0, n):
                colnum.append('A')
        n = n / 26
        colnum.append(alphadict[r])

    if n != 0:
        colnum.append(alphadict[n])

    return colnum
