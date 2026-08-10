import matplotlib.pyplot as plt
import math

Gravity = 9.81  # m/s^2
Black_Hole_Mass = 1000  # kg
dt = 0.01  # time step in seconds (derivative of time)

Object_Position_X = 0  # initial position in meters
Object_Position_Y = 100  # initial position in meters

Object_Velocity_X = 0  # initial velocity in m/s
Object_Velocity_Y = 0  # initial velocity in m/s

Object_X_Path = []
Object_Y_Path = []

while Distance_From_Black_Hole != 0:
    Distance_From_Black_Hole = math.sqrt(Object_Position_Y**2 + Object_Position_X**2)

    Gravitational_Acceleration = (Gravity * Black_Hole_Mass) / Distance_From_Black_Hole**2

    Gravity_Force_X = Gravitational_Acceleration * (-Object_Position_X / Distance_From_Black_Hole)
    Gravity_Force_Y = Gravitational_Acceleration * (-Object_Position_Y / Distance_From_Black_Hole)


