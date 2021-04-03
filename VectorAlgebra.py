class VectorAlgebra:

    def __init__(self):
        self.assert_ = Asseritons()

    def vector_sum(self, vector_a: list, vector_b: list) -> list:
        """
        vector_a -> list
        vector_b -> list
        return vector_a + vector_b
        """

        self.assert_.check_assertion(vector_a, vector_b)

        vector_c = []
        for elem_a, elem_b in zip(vector_a, vector_b):
            vector_c.append(elem_a + elem_b)

        return vector_c

    def vector_difference(self, vector_a: list, vector_b: list) -> list:
        """
        vector_a -> list
        vector_b -> list
        return vector_a - vector_b
        """

        self.assert_.check_assertion(vector_a, vector_b)

        vector_c = []
        for elem_a, elem_b in zip(vector_a, vector_b):
            vector_c.append(elem_a - elem_b)

        return vector_c

    def is_vectors_equal(self, vector_a: list, vector_b: list) -> bool:
        """
        vector_a -> list
        vector_b -> list
        for each elemnts in both list check are they equal
        """
        self.assert_.check_assertion(vector_a, vector_b)

        k = 0

        for a, b in zip(vector_a, vector_b):
            if a == b:
                k += 1
            else:
                return False

        return True

    def calculate_vector_module(self, vector_a: list) -> float:
        """
        vector_a -> list
        calculate module of vector
        return float value
        """
        d = 0
        for i in vector_a:
            d += i ** 2
        return d ** 0.5

    def calculate_mul_two_vectors(self, vector_a: list, vector_b: list) -> bool:
        self.assert_.check_assertion(vector_a, vector_b)

        mul = 0
        for a, b in zip(vector_a, vector_b):
            mul += a * b
            return mul

    def calculate_cos_between_two_vectors(self, vector_a: list, vector_b: list) -> float:
        self.assert_.check_assertion(vector_a, vector_b)
        return self.calculate_mul_two_vectors(vector_a, vector_b) / self.calculate_vector_module(
            vector_a) * self.calculate_vector_module(vector_b)
