import matplotlib.pyplot as plt
import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
import math

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)

label = tk.Label(root, text="Black Hole Simulation Parameters")
label.pack()

tk.Label(root, text="Black Hole Mass (kg)").grid(row=0, column=0)

tk.Label(root, text="Object X Initial Velocity (m/s)").grid(row=2, column=0)
tk.Label(root, text="Object Y Initial Velocity (m/s)").grid(row=3, column=0)
tk.Label(root, text="Object Z Initial Velocity (m/s)").grid(row=4, column=0)

Black_Hole_Mass_Entry = tk.Entry(root)
Object_Velocity_X_Entry = tk.Entry(root)
Object_Velocity_Y_Entry = tk.Entry(root)
Object_Velocity_Z_Entry = tk.Entry(root)

Black_Hole_Mass_Entry.grid(row=0, column=1)
Object_Velocity_X_Entry.grid(row=2, column=1)
Object_Velocity_Y_Entry.grid(row=3, column=1)
Object_Velocity_Z_Entry.grid(row=4, column=1)

root.mainloop()

Gravity = 9.81  # m/s^2
Black_Hole_Mass = float(Black_Hole_Mass_Entry.get())  # kg
dt = 0.01  # time step in seconds (derivative of time)

# initial position in meters
Object_Position_X = 0  
Object_Position_Y = 100  
Object_Position_Z = 0  

# initial velocity in m/s
Object_Velocity_X = float(Object_Velocity_X_Entry.get())
Object_Velocity_Y = float(Object_Velocity_Y_Entry.get())
Object_Velocity_Z = float(Object_Velocity_Z_Entry.get())

# Lists to store the path of the object
Object_X_Path = []
Object_Y_Path = []
Object_Z_Path = []

# Calculate the initial distance from the black hole
Distance_From_Black_Hole = math.sqrt(Object_Position_Y**2 + Object_Position_X**2 + Object_Position_Z**2)

# Simulate the motion of the object under the influence of the black hole's gravity
for step in range(50000):  # simulate for 10000 time steps

    # Calculate the distance from the black hole
    Distance_From_Black_Hole = math.sqrt(Object_Position_Y**2 + Object_Position_X**2 + Object_Position_Z**2)

    # Calculate the gravitational acceleration towards the black hole
    Gravitational_Acceleration = (Gravity * Black_Hole_Mass) / Distance_From_Black_Hole**2

    # Calculate the gravitational force components
    Gravity_Force_X = Gravitational_Acceleration * (-Object_Position_X / Distance_From_Black_Hole)
    Gravity_Force_Y = Gravitational_Acceleration * (-Object_Position_Y / Distance_From_Black_Hole)
    Gravity_Force_Z = Gravitational_Acceleration * (-Object_Position_Z / Distance_From_Black_Hole)

    # Update the object's velocity and position using the gravitational force
    Object_Velocity_X += Gravity_Force_X * dt
    Object_Velocity_Y += Gravity_Force_Y * dt
    Object_Velocity_Z += Gravity_Force_Z * dt

    # Update the object's position based on its velocity
    Object_Position_X += Object_Velocity_X * dt
    Object_Position_Y += Object_Velocity_Y * dt
    Object_Position_Z += Object_Velocity_Z * dt

    Object_X_Path.append(Object_Position_X)
    Object_Y_Path.append(Object_Position_Y)
    Object_Z_Path.append(Object_Position_Z)

    # Check if the object has crossed the event horizon (distance < 2 meters)
    if Distance_From_Black_Hole < 2:
        break

# Plot the path of the object in 3D space
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(Object_X_Path, Object_Y_Path, Object_Z_Path, color='blue')
ax.plot([0], [0], [0], marker='o', markersize=10, color='black')
plt.show()