def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    result = [[0 * n for i in range(n)] for j in range(len(matrix[0]))]

    for i in range(len(result)):
        for j in range(n):
            result[i][j] = matrix[j][i]
    return result