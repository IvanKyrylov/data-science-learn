empty_dict = {}
empty_dict2 = dict()
grades = {"Joel": 80, "Tim": 95}

for i in [empty_dict, empty_dict2, grades]:
    print(i)


joels_grade = grades["Joel"]
print(joels_grade)

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("key not found")

joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades

print(joel_has_grade, kate_has_grade)

joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0)
no_ones = grades.get("No exist")
print(joels_grade, kates_grade, no_ones)

grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)
print(grades.get("Tim"), grades.get("Kate"), num_students)

tweet = {
"user":"joelgrus",
"text":"data science the best",
"retweet_count":100,
"hashtags":["#data", "#science", "#datascience", "#awesome", "#yolo"]
}
print(tweet)

tweet_key = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

print(tweet_key)
print(tweet_values)
print(tweet_items)

#print("user" in tweet_keys)
print("user" in tweet)

print("joelgrus" in tweet_values)
