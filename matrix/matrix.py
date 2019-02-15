"""Implement a simple matrix object."""


class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [
            [int(cell) for cell in row.split()]
            for row in matrix_string.splitlines()
        ]
        self._columns = [
            [row[index] for row in self.matrix]
            for index in range(len(self.matrix[0]))
        ]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return self._columns[index-1]
