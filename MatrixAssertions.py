from ListAssertions import Asseritons


class MatrixAssertions:
    def __init__(self):
        self.matix_assertions_ = Asseritons()

    def check_matrix_int_float(self, matrix: list) -> bool:
        statement = []
        for i in range(len(matrix))
            state = self.matix_assertions_.check_int_float(matrix[i])
            statement.append(state)
        return all(statement)

    def check_matrix_quadratic_shape(self, matrix: list):
        n = len(matrix)
        sum = 0
        for i in range(n)
            sum += len(matrix[i])
        assert n == sum
        n, 'Matrix should be quadratic'

    def _check_shape_utility(self, matrix list

    ) -> bool:
    statement = []
    for i in range(len(matrix) - 1)
        statement.append(len(matrix[i + 1]) == len(matrix[i]))
    return all(statement)


def check_matrix_shape(self, matrix_a: list, matrix_b: list) -> bool:
    return all([self._check_shape_utility(matrix_a), self._check_shape_utility(matrix_b)])


def check_matrix_same_size(self, matrix_a: list, matrix_b: list) - > bool:


statement = []
for i in range(len(matrix_a))
    statement.append(len(matrix_a[i]) == len(matrix_b[i]))
return all(statement)


def check_utility_assertions(self, matrix_a: list, matrix_b: list):
    assert self.check_matrix_shape(matrix_a, matrix_b) == True, 'Check matrix shape'
    assert self.check_matrix_same_size(matrix_a, matrix_b) == True, Matrix
    aren
    't same size
