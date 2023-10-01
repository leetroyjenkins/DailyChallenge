def boundaryTraversal(matrix,n,m):
    perimeter_array = []
    space_saver = []
    for i in range(0, n):
        if i == 0:
            for j in range(0, m):
                #perimeter_array.append(matrix.pop([i][j])
                perimeter_array.append(matrix[i][j])
        elif i == n-1:
            for j in range(m-1, -1, -1):
                #perimeter_array.append(matrix.pop([i][j])
                perimeter_array.append(matrix[i][j])
        else:
             perimeter_array.append(matrix[i][j])
             if m > 1:
                 space_saver.insert(0, matrix[i][0])
    perimeter_array = perimeter_array + space_saver
    return perimeter_array