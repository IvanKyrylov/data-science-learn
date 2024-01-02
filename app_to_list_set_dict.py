event_number=[x for x in range(5) if x%2 == 0]
squares = [x * x for x in range(5)]
event_squares = [x * x for x in event_number]

for x in [event_number, squares, event_squares]:
    print(x)

squares_dict={x:x*x for x in range(5)}
square_set = {x*x for x in [1,-1]}

print(squares_dict)
print(square_set)

zeros = [0 for _ in event_number]
print(zeros)

pairs = [ (x,y)
for x in range(10)
for y in range(10)
]
print(pairs)

increasing_pairs = [(x,y)
for x in range(10)
for y in range(x+1,10)]
print(increasing_pairs)
