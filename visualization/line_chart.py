from matplotlib import pyplot as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]

total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label='dispersion')
plt.plot(xs, bias_squared, 'r-.', label='shift^2')
plt.plot(xs, total_error, 'b:', label='error count')

plt.legend(loc=9)
plt.xlabel("Model complexity")
plt.title("Compromise")

plt.show()
