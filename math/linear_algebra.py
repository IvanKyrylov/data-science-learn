from typing import List

Vector = List[float]
height_weight_age = [175,
                     68,
                     40]
grades = [95,
          80,
          75,
          62]


def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)

    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def sub(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)

    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert sub([4, 5, 6], [1, 2, 3]) == [3, 3, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors

    num_element = len(vectors[0])
    assert all(len(v) == num_element for v in vectors)

    return [sum(vector[i] for vector in vectors)
            for i in range(num_element)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


