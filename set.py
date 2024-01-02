s = set()
s.add(1)
s.add(2)
s.add(2)
x=len(s)
y = 2 in s
z = 3 in s

for i in [s, x, y, z]:
    print(i)


hundreds_of_other_words = ["test","test", "test2", "test3"]
stopwords_list = ["a","an", "at"] + hundreds_of_other_words + ["yet", "you"]
print(stopwords_list)

print("zip" in stopwords_list)

stopword_set = set(stopwords_list)
print(stopword_set)

print("zip" in stopword_set)

item_list = [1,2,3,1,2,3]
num_items = len(item_list)
item_set = set(item_list)
num_distinct_items=len(item_set)
distinct_item_list = list(item_set)

print(num_items)
print(item_set)
print(num_distinct_items)
print(distinct_item_list)
