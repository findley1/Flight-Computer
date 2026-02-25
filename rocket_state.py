class RocketState: 
    def __init__(self):
        # Positon
        self.pos = [0.0, 0.0, 0.0]
        # Velocity
        self.vel = [0.0, 0.0, 0.0]
        # Acceleration
        self.accel = [0.0, 0.0, 0.0]
        # Body Quaternion
        self.q = [1.0, 0.0, 0.0, 0.0]
        # Magnetometer
        self.mag = [0.0, 0.0, 0.0]
        # Altimeter
        self.alt = 0.0