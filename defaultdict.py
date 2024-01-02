word_counts = {}
document = "test", "test", "test2"
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word]=1

print(word_counts)

word_counts = {}
for word in document:
    try:
        word_counts[word]+=1
    except KeyError:
        word_counts[word]=1

print(word_counts)

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

print(word_counts)


from collections import defaultdict

word_count = defaultdict(int)
for word in document:
    word_count[word] += 1

print(word_count)

dd_list = defaultdict(list)
dd_list[2].append(1)
print(dd_list)

dd_dict = defaultdict(dict)
dd_dict["Ivan"]["city"] = "Vishneve"
print(dd_dict)

dd_pair = defaultdict(lambda: [0,0])
dd_pair[2][1] = 1
print(dd_pair)

def test_int():
    return 666

dd_def = defaultdict(test_int)
dd_def["test"]+=1
print(dd_def)
