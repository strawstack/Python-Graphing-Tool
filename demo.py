from geeraph import geeraph
import math

#
# BUILD a LIST
# of x and y coordinates
#
x = list(range(1000))
x = list(map(lambda x: x/100, x))
G = lambda x: math.sin(x) + 3 * math.cos(x - math.pi)**3
y = [G(p) for p in x]

#
# DISPLAY GRAPH
# in default browser
# with one easy command
#
geeraph.show(x, y)
# Alternatively, pass a list of coords. ex. geeraph.show( [(x1, y1), (x2, y2), ..., (xk, yk)] )
