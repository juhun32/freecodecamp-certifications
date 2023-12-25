import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
g = 9.8  # acceleration due to gravity (m/s^2)

# Function to calculate projectile motion
def projectile_motion(t, v0, theta):
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    return x, y

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 25)
ax.set_ylim(0, 10)

# Initialize the plot with an empty line
line, = ax.plot([], [], 'o-', lw=2)

# Animation function to update the plot
def update(frame):
    t = np.linspace(0, frame / 10, 100)
    v0 = 10  # initial velocity (m/s)
    theta = np.radians(45)  # launch angle

    x, y = projectile_motion(t, v0, theta)

    line.set_data(x, y)
    return line

# Create an animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 30), interval=200)

# Display the plot
plt.title('Projectile Motion Animation')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.grid(True)
plt.show()
