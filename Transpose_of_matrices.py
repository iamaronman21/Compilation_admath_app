def transpose_matrices(matrix1, matrix2):

    transposed_matrix1 = [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1[0]))]

    transposed_matrix2 = [[matrix2[j][i] for j in range(len(matrix2))] for i in range(len(matrix2[0]))]

    return transposed_matrix1, transposed_matrix2