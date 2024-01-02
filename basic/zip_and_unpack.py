list1 = ['a','b','c']
list2 = [1,2,3]

pairs =[pair for pair in zip(list1,list2)]
print(pairs)

letter, number = zip(*pairs)

print(*pairs)
print(zip(*pairs))

def add(a,b):return a+b

print(add(1,2))

try:
    add([1,2])
except:
    print("not value type")

print(add(*[1,2]))
