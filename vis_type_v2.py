def total(xs:list) -> float:
    return sum(total)

from typing import List

def total(xs:List[float]) -> float:
    return sum(total)

x: int = 5

value = []
best_so_far = None

from typing import Optional

values: List[int] = []
best_so_far: Optional[float] = None

from typing import Dict, Iterable, Tuple

counts: Dict[str, int] = {'data':1, 'science':2}

lazy: bool = False

if lazy:
    events: Iterable[int] = (x for x in range(10) if x % 2 == 0)
else:
    events = [0,2,4,6,8]

triple: Tuple[int, float, int] = (10,2.3,5)

from typing import Callable

def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s,2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

assert twice(comma_repeater,"type sup") == "type sup, type sup"

Number = int
Numbers = List[Number]

def total(xs: Number) -> Number:
    return sum(xs)
