# Black Hole Orbit Simulator

A simple interactive 3D simulation of an object orbiting (or falling into) a black hole, built in Python with a Tkinter GUI and Matplotlib for visualization.

## What it does

This program models a small object moving under the gravitational pull of a black hole using basic Newtonian physics. You can set the black hole's mass and the object's starting velocity through a GUI, run the simulation, and see the resulting 3D orbit path plotted live.

If the object gets close enough to the black hole (inside a set "event horizon" radius), the simulation stops and treats it as having fallen in.

## Features

- GUI built with Tkinter, using sliders for input
- Adjustable black hole mass and initial X/Y/Z velocity
- 3D orbit path rendered with Matplotlib, embedded directly in the app window
- Labeled X, Y, and Z axes
- Simple Newtonian gravity physics (`a = G*M / r²`)
- Event horizon detection
- Rotatable 3D view for inspecting the orbit shape from any angle
- "Run Animation" button to watch the object trace its path over time, instead of seeing it drawn instantly

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
- Sliders for black hole mass and initial X/Y/Z velocity
- A "Run Simulation" button
- A "Run Animation" button
- An embedded, labeled 3D plot area

Set the sliders, click **Run Simulation** once to draw the initial orbit instantly. After that first click, moving any slider automatically reruns the simulation and updates the plot in place — no need to click the button again. You can also click and drag the plot itself to rotate the 3D view at any time.

Click **Run Animation** at any point after the first run to watch the object trace its most recent path step-by-step instead of seeing it appear all at once.

## Suggested starting values

| Parameter | Suggested value |
|---|---|
| Black Hole Mass | 1000 |
| X Velocity | 2 |
| Y Velocity | 0 |
| Z Velocity | 3 |

- **Higher X velocity** → wider, more stable orbit (or the object escapes entirely if too high)
- **Lower X velocity** → tighter orbit, more likely to fall in
- **X velocity of 0** → no sideways motion at all, object falls straight in

- **Higher Z velocity** → tilts the orbit further out of the flat plane, making it more clearly 3D when rotated; too much combined with X velocity can push the object into an escape trajectory
- **Z velocity of 0** → orbit stays flat (2D), even though it's being plotted in a 3D view

- **Higher mass** → stronger pull, tighter/faster orbits at the same velocity, more likely to capture the object
- **Lower mass** → weaker pull, wider orbits, more likely the object escapes at the same velocity

- **Y velocity** behaves differently from X and Z: the object starts *on* the Y-axis (`Object_Position_Y = 100`, with X and Z at 0), so Y velocity at the start points directly toward or away from the black hole rather than sideways. A positive Y velocity here means moving further away initially; it doesn't create the sideways motion needed for an orbit the way X or Z velocity does

In general, it's the **total sideways speed** (X and Z combined) relative to the black hole's mass that determines whether you get a falling-in trajectory, a stable orbit, or an escape — small adjustments to any one value can shift which of the three you get, so this is very much a "tweak and rerun" kind of simulation

## Notes / limitations

- This uses simplified Newtonian gravity, not general relativity, meaning it's a visual/educational approximation, not a physically accurate model of a real black hole
- Units are arbitrary/simplified (not real-world kg, meters, or seconds) for simulation stability and visual clarity
- The "event horizon" is just a distance cutoff, not a true relativistic event horizon

## Possible next steps

- Add a reset/clear button
- Add labels showing the live slider values and/or a "fell in!" vs "still orbiting" status message
- Add a speed control for the animation
- Add multiple simultaneous orbiting objects
