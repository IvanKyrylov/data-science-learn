def generate_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in generate_range(10):
    print(f"i: {i}")

def natural_number():
    n = 1
    while True:
        yield n
        n += 1

#for i in natural_number(20):
#    print(i)

#t = natural_number
#for i in t(10):
    print("t", i)

#for i in t(20):
#    print("t2", i)

event_below_20 = (i for i in generate_range(20) if i % 2 == 0)

for i in event_below_20:
    print("t3", i)

data = natural_number()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)
count=0
for i in even_squares_ending_in_six:
    if count == 10:
        break 
    print(i)
    count+=1


names = ["Alice", "Bob", "Charlie", "Debbie"]

for i in range(len(names)):
    print(f"name {i} is {names[i]}")

i=0
for name in names:
    print(f"name {i} is {names[i]}")
    i+=1

for i, name in enumerate(names):
    print(f"name {i} is {name}")

