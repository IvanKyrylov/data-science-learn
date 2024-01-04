if 1 > 2:
    message = "1>2"
elif 1 > 3:
    message = "else if"
else:
    message = "end"

print(message)

x = 2
parity = "qut" if x % 2 == 0 else "noqut"
print(parity)

x = 0
while x < 10:
    print(x, "< 10")
    x += 1

for x in range(10):
    print(x, "<10")

for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print(x)
