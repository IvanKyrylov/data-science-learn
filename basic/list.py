integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.2, True]
list_of_lists = [integer_list, heterogeneous_list, []]

for i in [integer_list, heterogeneous_list, list_of_lists]:
    print(i)
    print("len " + str(len(i)))
    # print("sum " + str(sum(i)))

print(sum(integer_list))

x = list(range(10))
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]

print(x)
print(zero)
print(one)
print(nine)
print(eight)

x[0] = -1
print(x)

first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]

copy_of_x = x[:]

for i in [first_three, three_to_end, one_to_four, last_three, without_first_and_last, copy_of_x]:
    print(i)

every_third = x[::3]
five_to_thtrr = x[5:2:-1]

print(1 in [1, 2, 3])
print(0 in [1, 2, 3])

x = [1, 2, 3]
x.extend([4, 5, 6])
print(x)

y = x + [4, 5, 6]
print(y)

x.append(0)
y = x[-1]
z = len(x)

print(x)
print(y)
print(z)

x, y = [1, 2]
print(x, y)

_, y = [3, 4]
print(y)
