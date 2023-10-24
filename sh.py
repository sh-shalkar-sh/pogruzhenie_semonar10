class MatrixTransposer:
    def __init__(self, matrix):
        self.matrix = matrix

    def transpose_matrix(self):
        rows, cols = len(self.matrix), len(self.matrix[0])
        transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transposed_matrix[j][i] = self.matrix[i][j]

        return transposed_matrix

# Пример использования класса
my_matrix = [['a', 'b', 'c'],
             [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

matrix_transposer = MatrixTransposer(my_matrix)
result = matrix_transposer.transpose_matrix()

for row in result:
    print(row)
