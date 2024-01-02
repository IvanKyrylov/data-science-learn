def double(x):
    """
    
    multicolm comment
    
    """
    return x * 2
print(double(2))

#print(double_v2(3))
def double_v2(x):
    return x / 2
print(double_v2(3))


def apply_to_one(f):
    return f(1)

my_double = double
x = apply_to_one(my_double)
print(x)

y = apply_to_one(lambda x: x + 4)
print(y)

#another_double = lambda x: 2 * x
def another_double(x):
    return 2 * x

def my_print(message="my message"):
    print(message)

my_print("hello")
my_print()
my_print("")


def full_name(first = "first name", last = "last name"):
    return first + " " + last

my_print(full_name("Ivan", "Kyrylov"))
my_print(full_name("Ivan"))
my_print(full_name(last="Kyrylov"))
my_print(full_name(first="Ivan"))
