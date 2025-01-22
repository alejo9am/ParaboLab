import math

def calculate(angle: float, velocity: float, gravity: float) -> dict:
    """
    In the X axis the projectile follows this equations
    x = v0 * cos(angle) * t
    Vx = v0 * cos(angle) -----> it has constant velocity

    In the Y axis the projectile follows this equations
    y = v0 * sin(angle) * t - (g * t^2)/2
    Vy = v0 * sin(angle) - g * t
    """

    # We can define initial velocity in X and Y axis
    velocity_x = velocity * math.cos(math.radians(angle))
    velocity_y = velocity * math.sin(math.radians(angle))

    # First we calculate the time when it reaches max height
    time_max_height = calculate_max_height_time(velocity_y, gravity)

    # Now we can calculate the max height using the formula:
    # y = v0 * sin(angle) * t - (g * t^2)/2
    max_height = calculate_max_height(velocity_y, time_max_height, gravity)

    # We can calculate the total time using "time of max height" value
    time = 2 * time_max_height  # -----> time to reach max height and return to the ground

    # Now we can calculate the final distance using the formula:
    # x = v0 * cos(angle) * t
    distance = velocity_x * time

    return {
        'angle': angle,
        'velocity': velocity,
        'gravity': gravity,
        'distance': round(distance, 2),
        'max_height': round(max_height, 2),
        'time': round(time, 2)
    }

def calculate_max_height_time(velocity_y: float, gravity: float) -> float:
    """
    Calculate the time when the projectile reaches the max height
    Vy = v0 * sin(angle) - g * t
    0 = v0 * sin(angle) - g * t
    g * t = v0 * sin(angle)
    t = v0 * sin(angle) / g
    """

    return velocity_y / gravity

def calculate_max_height(velocity_y: float, time_max_height: float, gravity: float) -> float:
    """
    Calculate the max height of the projectile
    y = v0 * sin(angle) * t - (g * t^2)/2
    We substitute the time value
    h = velocity_y * time_max_height - (gravity * time_max_height^2) / 2
    """

    return velocity_y * time_max_height - (gravity * time_max_height**2) / 2