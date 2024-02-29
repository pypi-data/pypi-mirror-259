# PyRandomLoop

PyRandomLoop is a Python package designed for simulating and visualizing a random loop model on a 2d grid. Ideal for researchers and hobbyists alike, this package offers an intuitive approach to exploring complex patterns and dynamics through simple and flexible APIs.

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
