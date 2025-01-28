import math
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import io
import base64

def calculate_points(velocity: float, angle: float, gravity: float, time: float) -> tuple:
    """
    Calculate the x and y points of the projectile
    """
    
    #Convert to radians
    angle = math.radians(angle)

    # We can define initial velocity in X and Y axis
    velocity_x = velocity * math.cos(angle)
    velocity_y = velocity * math.sin(angle)

    # Each second of flight is divided into 100 parts
    parts = 100

    # Calculate the time step
    time_step = time / parts

    # Initialize the lists
    x_points = []
    y_points = []

    # Calculate the points
    for i in range(parts + 1):
        t = time_step * i
        x = velocity_x * t
        y = velocity_y * t - 0.5 * gravity * t**2
        x_points.append(x)
        y_points.append(y)

    return x_points, y_points

def plot_points(x_points: list, y_points: list):
    """
    Plot the x and y points
    """
    
    plt.figure(figsize=(8, 8), facecolor="#f3fbfd")
    plt.plot(x_points, y_points, color="#19becf", linewidth=2.5)

    plt.xlabel("Horizontal Distance (m)", fontsize=14, color="#2c3e50")
    plt.ylabel("Vertical Distance (m)", fontsize=14, color="#2c3e50")

    plt.grid(True, linestyle="--", alpha=0.5, color="#c5f4f7")

    # Set limits
    plt.xlim(0, max(x_points))
    plt.ylim(0, max(y_points) * 1.1)

    # Maintatin equal aspect ratio
    plt.gca().set_aspect('equal', adjustable='datalim')

    plt.axhline(0, color="#34495e", linewidth=1.2)
    plt.tight_layout()
    plt.box(False)  # Remove the outer frame for a cleaner look



    # Save the plot to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=100)
    buffer.seek(0)
    plt.close()

    # Encode the buffer to base64
    image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    return image