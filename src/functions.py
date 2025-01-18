
def calculate(angle: float, velocity: float, gravity: float) -> dict:

    distance = (velocity**2 * (2 * gravity) * (angle**2)) / (2 * gravity)
    max_height = (velocity**2 * (angle**2) * (gravity)) / (2 * gravity)
    time = (2 * velocity * angle) / gravity

    return {
        'angle': angle,
        'velocity': velocity,
        'gravity': gravity,
        'distance': distance,
        'max_height': max_height,
        'time': time
    }