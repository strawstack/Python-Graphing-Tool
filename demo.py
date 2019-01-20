import geeraph
import random

x = range(100)
y = [random.randint(1, 75) for x in range(100)]

geeraph.show(x, y)
