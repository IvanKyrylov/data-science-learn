from matplotlib import pyplot as plt

movies = ["M1", "M2", "M3", "M4", "M5"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), num_oscars)

plt.title("Best film")
plt.ylabel("count")

plt.xticks(range(len(movies)), movies)

plt.show()

from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],
        histogram.values(),
        10,
        edgecolor=(0, 0, 0))

plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])

plt.xlabel("Del")
plt.ylabel("students count")
plt.title("Test 1")

plt.show()

mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("data science say count")

plt.ticklabel_format(useOffset=False)

plt.axis([2016.5, 2018.5, 499, 506])
plt.title("A big increase")

plt.show()

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("data science say count")

plt.axis([2015, 2020, 0, 600])
plt.title("Not huge increase")

plt.show()
