import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random
import math

def func(a, b, c, x):
    return a * x**2 + b * x + c

loc = random.randint(1, 100)
loch = random.randint(1, 1000)
print(f"A rocket has to clear a wall that is {loch} meters high, {loc} meters away")

a = -1
b = float(input("Initial velocity (m/s) = "))
c = 0

# Change vx and vy to represent the vertex
vx = -b / (2 * a)
vy = a * vx**2 + b * vx + c

# Also change the following dimensions to display the vertex
xmin = -1
xmax = 150
ymin = -1
ymax = max(loch, int(vy)) + 10

points = 2 * (xmax - xmin)
x = np.linspace(xmin, xmax, points)
y = func(a, b, c, x)

fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax])  # window size

line, = plt.plot([], [], 'b-')
vertex, = plt.plot([], [], 'ro')
wall, = plt.plot([loc, loc], [0, loch], "r")  # wall

def init():
    line.set_data([], [])
    vertex.set_data([], [])
    return line, vertex

def update(frame):
    x_vals = np.linspace(xmin, xmax, points)
    y_vals = func(a, b, c, x_vals - frame)

    line.set_data(x_vals, y_vals)
    vertex.set_data([vx - frame], [func(a, b, c, vx - frame)])

    return line, vertex

animation = FuncAnimation(fig, update, frames=xmax, init_func=init, interval=50, repeat=False)

root_sq = round((-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a), 2)

if func(a, b, c, loc) >= loch and root_sq >= loc:  # must fly past wall
    print("Success")
else:
    print("Missed")

print(" ")
plt.show()
