import geeraph
import math

# buld lst of z and y coordinates
x = list(range(1000))
x = list(map(lambda x: x/100, x))
G = lambda x: math.sin(x) + 3 * math.cos(x - math.pi)**3
y = [G(p) for p in x]

#
# display graph in default browser
# with one easy command 
#
geeraph.show(x, y)
