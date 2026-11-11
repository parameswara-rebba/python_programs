"""Matrix transpose, addition and multiplication using nested lists."""

Matrix = list[list[float]]


def transpose(m: Matrix) -> Matrix:
    return [list(row) for row in zip(*m)]


def add(a: Matrix, b: Matrix) -> Matrix:
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise ValueError("matrices must have the same shape")
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("columns of the first must equal rows of the second")
    columns = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in columns] for row in a]


if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    print("transpose:", transpose(a))
    print("add:      ", add(a, b))
    print("multiply: ", multiply(a, b))
