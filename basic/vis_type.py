def add(a, b):
    return a + b


assert add(10, 5) == 15
assert add([1, 2], [3]) == [1, 2, 3]
assert add("Hi ", "Hello") == "Hi Hello"

try:
    add(10, "five")
except TypeError:
    print("TypeError")


def add(a: int, b: int) -> int:
    return a + b


add(10, 5)
add("Hi ", "Hello")

from typing import Union


def secretly_ugly_func(value, operation):
    return ""


def ugly_func(value: int, operation: Union[str, int, float, bool]) -> int:
    return 0
