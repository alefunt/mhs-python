import random

import numpy as np

from matrices.Matrix import Matrix
from matrices.Mixins import MatrixOpsMixin, BetterStrMixin



def matrix_class(n, m):
    matrix1 = Matrix(n.tolist())
    matrix2 = Matrix(m.tolist())

    with open('artifacts/3.1/matrix+.txt', 'w') as f:
        f.write(str(matrix1 + matrix2))
    with open('artifacts/3.1/matrix_mult.txt', 'w') as f:
        f.write(str(matrix1 * matrix2))
    with open('artifacts/3.1/matrix@.txt', 'w') as f:
        f.write(str(matrix1 @ matrix2))


def matrix_mixin(n, m):
    class Person(BetterStrMixin, MatrixOpsMixin):
        def __init__(self, name: str = None, age: int = 0):
            super().__init__()
            self._name = name
            self._age = age

    person1 = Person("John", 12)
    person1.data = n

    person2 = Person("John", 12)
    person2.data = m

    (person1 + person2).write_to_file('artifacts/3.2/matrix+.txt')
    (person1 * person2).write_to_file('artifacts/3.2/matrix_mult.txt')
    (person1 @ person2).write_to_file('artifacts/3.2/matrix@.txt')


def main():
    random.seed(0)
    n = np.random.randint(0, 10, (10, 10))
    m = np.random.randint(0, 10, (10, 10))

    matrix_class(n, m)
    matrix_mixin(n, m)

if __name__ == "__main__":
    main()