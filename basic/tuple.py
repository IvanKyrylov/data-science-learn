my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4

for i in [my_list, my_tuple, other_tuple]:
    print(i)

my_list[1] = 3
print(my_list)

try:
    my_tuple[1] = 3
except TypeError:
    print("tuple not mut")


def sum_and_product(x, y):
    return (x + y), (x * y)


sp = sum_and_product(2, 3)
print(sp)

s, p = sum_and_product(5, 10)
print(s, p)

x, y = 1, 2
x, y = y, x

print(x, y)
