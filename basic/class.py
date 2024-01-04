class CountingClicker:
    """
    CountTingClicker
    """

    def __init__(self, count=0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self, num_times=1):
        """add >=1 clicks"""
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0


clicker1 = CountingClicker()
clicker2 = CountingClicker(100)
clicker3 = CountingClicker(count=100)

print(clicker1)
print(clicker2)
print(clicker3)

clicker = CountingClicker()
assert clicker.read() == 0
clicker.click()
clicker.click()
assert clicker.read() == 2
clicker.reset()
assert clicker.read() == 0


class NoResetClicker(CountingClicker):
    def reset(self):
        pass


clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1
