assert 1+1 == 2
assert 1+1 == 2, "not true"

def small_item(xs):
    assert xs, "xs None"
    return min(xs)

assert small_item([10,20,5,40])==5
assert small_item([1,0,-1,2])==-1


