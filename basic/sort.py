x = [4, 1, 2, 3]
y = sorted(x)
x.sort()

print(x)
print(y)

x = sorted([-4, 1, -2, 3], reverse=True)
print(x)

wc = sorted([("test", 2), ("test2", 1)], key=lambda word_and_count: word_and_count[1], reverse=True)
print(wc)

x = sorted(["AA", "AAA", "A"])
print(x)
