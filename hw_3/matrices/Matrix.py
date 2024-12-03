class Matrix:
    def __init__(self, data: list[list[int]]):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must be of the same length")
        self.rows = len(data)
        self.cols = len(data[0])
        self.data = [row[:] for row in data]


    @classmethod
    def zeros(cls, rows: int, cols: int) -> 'Matrix':
        return cls([[0]*cols]*rows)

    def __getitem__(self, item: int) -> list[int]:
        return self.data[item]

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must be of same size")
        result = Matrix.zeros(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self[i][j] + other[i][j]
        return result

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must be of same size")
        result = Matrix.zeros(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self[i][j] * other[i][j]
        return result

    def __matmul__(self, other:'Matrix') -> 'Matrix':
        if self.cols != other.rows:
            raise ValueError("First matrix should have same numbers of columns as second matrix has rows")
        result = Matrix.zeros(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self[i][k] * other[k][j]
        return result

    def __str__(self):
        return "\n".join([str("\t".join([str(x) for x in row])) for row in self.data])