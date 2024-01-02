import random

random.seed(10)

four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)

random.seed(10)
print(random.random())

random.seed(10)
print(random.random())

print(random.randrange(10))
print(random.randrange(3,6))

up_to_ten = list(range(10))
random.shuffle(up_to_ten)
print(up_to_ten)

print(random.choice(["Alice","Bob","Charlie"]))

lottery_numbers = range(60)
winning_numbers =random.sample(lottery_numbers, 6)
print(winning_numbers)

four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)

