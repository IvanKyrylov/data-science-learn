from collections import Counter

c = Counter([0, 2, 1, 0])
print(c)

c_str = Counter(["zero", "one", "two", "zero"])
print(c_str)

word_counts = Counter(["zero", "test", "test"])
for word, count in word_counts.most_common(1):
    print(word, count)
