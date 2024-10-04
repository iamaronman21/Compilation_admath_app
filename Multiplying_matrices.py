def multiply_matrices(matA, matB):
    rows1 = len(matA)
    cols1 = len(matA[0])
    rows2 = len(matB)
    cols2 = len(matB[0])

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(rows2):
                result[i][j] += int(matA[i][k]) * int(matB[k][j])

    return result