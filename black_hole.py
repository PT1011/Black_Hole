import matplotlib.pyplot as plt
import math

Gravity = 9.81  # m/s^2
Black_Hole_Mass = 1000  # kg
dt = 0.01  # time step in seconds (derivative of time)

Object_Position_X = 0  # initial position in meters
Object_Position_Y = 100  # initial position in meters

Object_Velocity_X = 10  # initial velocity in m/s
Object_Velocity_Y = 0  # initial velocity in m/s

Object_X_Path = []
Object_Y_Path = []

Distance_From_Black_Hole = math.sqrt(Object_Position_Y**2 + Object_Position_X**2)

while Distance_From_Black_Hole > 0.9:
    Distance_From_Black_Hole = math.sqrt(Object_Position_Y**2 + Object_Position_X**2)

    Gravitational_Acceleration = (Gravity * Black_Hole_Mass) / Distance_From_Black_Hole**2

    Gravity_Force_X = Gravitational_Acceleration * (-Object_Position_X / Distance_From_Black_Hole)
    Gravity_Force_Y = Gravitational_Acceleration * (-Object_Position_Y / Distance_From_Black_Hole)

    Object_Velocity_X += Gravity_Force_X * dt
    Object_Velocity_Y += Gravity_Force_Y * dt

    Object_Position_X += Object_Velocity_X * dt
    Object_Position_Y += Object_Velocity_Y * dt

    Object_X_Path.append(Object_Position_X)
    Object_Y_Path.append(Object_Position_Y)

    plt.plot(Object_X_Path, Object_Y_Path, color='blue') # Plotting the path of the object
    plt.plot(0, 0, marker='o', markersize=10, color='black')  # Black hole at the origin
