'''Напишите функцию для транспонирования матрицы'''
def transform_matrix(matrix):
    r = len(matrix)
    c = len(matrix[0])
    transposed = [[0 for _ in range(r)] for _ in range(c)]

    for i in range(r):
        for j in range(c):
            transposed[j][i] = matrix[i][j]

    return transposed


matrix = [[15, 12, 34], [74, 7, 13], [10, 64, 37]]
print(transform_matrix(matrix))