# PyRandomLoop

PyRandomLoop is a Python package designed for simulating and visualizing a random loop model on a 2d grid. 
The core of the simulation is the class `stateSpace`. Features include performance optimizations, execution logging, and statistics calculation, alongside visualization tools for detailed analysis. Ideal for researchers and students in physics and related fields.

## Features

- **Multiple Initialization Patterns:** Choose from random, snake, or donut patterns to start your simulations.
- **Flexible Simulation Algorithms:** Supports both Metropolis and Glauber algorithms to drive the simulation process.
- **Visualization:** Easily plot the current state of the grid with support for highlighting color loops.
- **State Management:** Save and load simulation states, allowing for pause-resume functionality.

## Quick Start

```python
from PyRandomLoop import stateSpace

# Initialize and run the simulation
simulation = stateSpace(num_colors=3, grid_size=50, beta=0.5)
simulation.step(num_steps=1000)

# Visualization
simulation.plot_grid()

# Save/load the simulation state
simulation.save_data("simulation_state.json")
simulation.load_data("simulation_state.json")
