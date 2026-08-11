adme · MD
# Black Hole Orbit Simulator
 
A simple interactive 3D simulation of an object orbiting (or falling into) a black hole, built in Python with a Tkinter GUI and Matplotlib for visualization.
 
## What it does
 
This program models a small object moving under the gravitational pull of a black hole using basic Newtonian physics. You can set the black hole's mass and the object's starting velocity through a GUI, run the simulation, and see the resulting 3D orbit path plotted live — no separate windows, everything updates in place.
 
If the object gets close enough to the black hole (inside a set "event horizon" radius), the simulation stops and treats it as having fallen in.
 
## Features
 
- GUI built with Tkinter — no need to edit code to change simulation parameters
- Adjustable black hole mass and initial X/Y/Z velocity
- 3D orbit path rendered with Matplotlib, embedded directly in the app window
- Simple Newtonian gravity physics (`a = G*M / r²`)
- Event horizon detection — the simulation stops if the object falls in
- Rotatable 3D view for inspecting the orbit shape from any angle
## How it works
 
Each simulation step:
1. Calculates the object's distance from the black hole (at the origin)
2. Calculates the gravitational acceleration based on that distance
3. Splits the acceleration into X, Y, and Z components pointing toward the black hole
4. Updates the object's velocity, then its position, using that acceleration
5. Records the new position for plotting
6. Stops early if the object crosses the event horizon distance
This repeats for up to 50,000 time steps (or until the object falls in), and the full path is then plotted in 3D.
 
## Requirements
 
- Python 3
- `matplotlib`
Install the dependency with:
```
pip install matplotlib
```
(Tkinter comes built in with most Python installations.)
 
## Running it
 
```
python black_hole.py
```
 
A window will open with:
- Input fields for black hole mass and initial X/Y/Z velocity
- A "Run Simulation" button
- An embedded 3D plot area
Enter values, click **Run Simulation**, and the orbit path will be drawn. You can click and drag the plot to rotate the 3D view. Running the simulation again with new values will redraw the same plot instead of opening a new window.
 
## Suggested starting values
 
| Parameter | Suggested value |
|---|---|
| Black Hole Mass | 1000 |
| X Velocity | 2 |
| Y Velocity | 0 |
| Z Velocity | 1 |
 
- Higher sideways velocity → wider, more stable orbit (or the object escapes if too high)
- Lower sideways velocity → tighter orbit, more likely to fall in
- Higher mass → stronger pull, tighter orbits at the same velocity
## Notes / limitations
 
- This uses simplified Newtonian gravity, not general relativity — it's a visual/educational approximation, not a physically accurate model of a real black hole
- Units are arbitrary/simplified (not real-world kg, meters, or seconds) for simulation stability and visual clarity
- The "event horizon" is just a distance cutoff, not a true relativistic event horizon
## Possible next steps
 
- Add a "fell in!" / "still orbiting" status label after each run
- Add a reset/clear button
- Replace Entry boxes with sliders for real-time-feeling adjustments
- Add multiple simultaneous orbiting objects
