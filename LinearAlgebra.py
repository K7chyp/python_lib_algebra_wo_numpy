from copy import deepcopy
from MatrixAssertions import MatrixAssertions


class LinearAlgebra:

    def __init__(self):
        self.matrix_asserions = MatrixAssertions()

    @private
    def _get_minor(self, matrix, row_, column):
        return [row[:column] + row[column + 1:] for row in (matrix[:row_] + matrix[row_ + 1:])]

    def get_zero_matrix(self, rows: int, cols: int) -> list:
        """
        rows: int
        cols: int
        return [[0.0, 0.0 ....
                [0.0, 0.0 ....
                ....
                ....0.0, 0.0]
                ]
        """
        assert (isinstance(rows) == int and isinstance(cols) == int), 'Rows and cols should be INT'
        return [[0.0] * cols for i in range(rows)]

    @private
    def _calculate_utility_det(self, matrix_2_2: list) -> float:
        """
        It shouldn't use out of class
        get list 2X2 and return determinant
        """
        return matrix_2_2[0][0] * matrix_2_2[1][1] - matrix_2_2[1][0] * matrix_2_2[0][1]

    def find_determinant(self, matrix: list) -> float:
        """
        Get matrix NXN
        return determinant
        """
        self.matrix_asserions.check_matrix_quadratic_shape(matrix)
        assert self.matrix_asserions.check_matrix_int_float(
            matrix) is False, 'Matrix should consist int or float values'

        determinant = 0

        idx = list(range(len(matrix)))

        if len(matrix) == 2 and len(matrix[0]) == 2:
            return self._calculate_utility_det(matrix)

        for j in idx:
            sub_matrix = deepcopy(matrix)
            sub_matrix = sub_matrix[1:]
            height = len(sub_matrix)

            for i in range(height):
                sub_matrix[i] = sub_matrix[i][0:j] + sub_matrix[i][j + 1:]

            sign = (-1) ** (j % 2)
            sub_det = self.find_determinant(sub_matrix)
            determinant += sign * matrix[0][j] * sub_det

        return determinant

    def matrix_sum(self, matrix_a: list, matrix_b: list) -> list:
        """
        get two matrix
        return matrix_a + matrix_b
        """
        self.matrix_asserions.check_utility_assertions(matrix_a, matrix_b)
        sub_matrix = [
            [matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))]
            for i in range(len(matrix_a))
        ]
        return sub_matrix

    def matrix_diff(self, matrix_a: list, matrix_b: list) -> list:
        """
        get two matrix
        return matrix_a - matrix_b
        """
        self.matrix_asserions.check_utility_assertions(matrix_a, matrix_b)
        sub_matrix = [
            [matrix_a[i][j] - matrix_b[i][j] for j in range(len(matrix_a[0]))]
            for i in range(len(matrix_a))
        ]
        return sub_matrix

    def matrix_transpose(self, matrix: list) -> list:
        """
        get matrix
        return transpose matrix
        """
        return list(map(list, zip(*matrix)))

    def multiply_two_matrix(self, matrix_a: list, matrix_b: list) -> list:
        """
        get two matrix
        return multiplied matrix
        """
        assert len(matrix_a) == len(matrix_b[0]), "Shapes aren't valid"
        self.matrix_asserions.check_utility_assertions(matrix_a, matrix_b)

        sub_matrix = self.get_zero_matrix(len(matrix_a), len(matrix_b[0]))
        for i in enumerate(matrix_a):
            for j in enumerate(matrix_b[0]):
                for k in enumerate(matrix_b):
                    sub_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

        return sub_matrix

    def get_inverse_matrix(self, matrix: list) -> list:
        """
        get matrix
        return inverse matrix
        """

        assert len(matrix) >= 2, 'Matrix should be at least 2X2'
        determinant = self.find_determinant(matrix)

        if len(matrix) == 2:
            return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                    [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant]]

        cofactors = []
        for row in range(len(matrix)):
            cofactor_row = []
            for column in range(len(matrix)):
                minor = self._get_minor(matrix, row, column)
                cofactor_row.append(((-1) ** (row + column)) * self.find_determinant(minor))
            cofactors.append(cofactor_row)
        cofactors = self.matrix_transpose(cofactors)
        for row in enumerate(cofactors):
            for column in enumerate(cofactors):
                cofactors[row][column] = cofactors[row][column] / determinant
        return cofactors

    def matrix_division(self, matrix_a: list, matrix_b: list) -> list:
        """
        Actully, it's my loving func
        get matrix_a, matrix_b
        return matrix_a / matrix_b
        """
        self.matrix_asserions.check_utility_assertions(matrix_a, matrix_b)
        return self.multiply_two_matrix(matrix_a, self.get_inverse_matrix(matrix_b))
