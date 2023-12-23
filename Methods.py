import math
import numpy as np

def createTable(matrix):
    matrix = np.array(matrix)
    colLen = matrix.shape[0]
    rowLen = matrix.shape[1]
    identityMatrix = np.eye(colLen)
    return np.hstack([matrix[:, :rowLen-1], identityMatrix, matrix[:, rowLen-1:rowLen]])

def targetCoeficient(matrix, row, column):
    if matrix[row][column] <= 0:
        return math.inf
    return matrix[row][-1] / matrix[row][column]

def performStep(matrix, target):
    pivot_value = matrix[target[0]][target[1]]
    matrix[target[0]] = [element / pivot_value for element in matrix[target[0]]]

    for row in range(len(matrix)):
        if row != target[0]:
            pivot_value = matrix[row][target[1]]
            matrix[row] = [element - pivot_value * matrix[target[0]][col] for col, element in enumerate(matrix[row])]

    return matrix

def optimize(matrix):
    row_count, column_count = len(matrix), len(matrix[0])

    while all(element >= 0 for element in matrix[-1][:-1]) == False:
        _, target_column = min((matrix[-1][col], col) for col in range(column_count - 1))
        _, target_row = min((targetCoeficient(matrix, row, target_column), row) for row in range(row_count - 1))
        target = [target_row, target_column]
        matrix = performStep(matrix, target)

    return matrix
