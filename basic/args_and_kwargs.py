def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x):
        return 2 * f(x)

    # And return that new function.
    return g


def f1(x):
    return x + 1


g = doubler(f1)
assert g(3) == 8, "(3 + 1) * 2 should equal 8"
assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"


def f2(x, y):
    return x + y


g = doubler(f2)
try:
    g(1, 2)
except TypeError:
    print("as defined, g only takes one argument")


def magic(*args, **kwargs):
    print("anonim arg", args)
    print("named arg", kwargs)


magic(1, 2, key="word", key2="word2")


def other_way_magic(x, y, z):
    return x + y + z


x_y_list = [1, 2]
z_dict = {"z": 3}
assert other_way_magic(*x_y_list, **z_dict) == 6


def doubler_correct(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)

    return g


g = doubler_correct(f2)

print(g(1, 2))
