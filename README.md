# Maze-Solver-Visualizer

This project implements simple maze solver that simulates an agent navigating a grid maze to reach a goal. It includes a visualization of the agent's movement using Matplotlib.

## Features 
 - Simulates an agent taking random actions to solve a maze.
 - Visualizes the path taken by the agent to reach the goal.
 - Handles unsolvable mazes by exiting after a timeout.


## Prerequisites 
 - Python 
 - matplotlib, numpy

## How to run 
 1. Clone this repository 
  ``git clone https://github.com/AstroWalker24/Maze-Solver-Visualizer.git``
  ``cd Maze-Solver-Visualizer``

 2. Run the program 
   ``python src.py``


## Explanation 
 1. Simulation 
   The agent starts at a given position and randomly chooses actions (up, down, left, right) to navigate the grid. The goal is to reach a predefined goal state.

 2. Visualization
   The agent's movement is visualized using Matplotlib. A red dot represents the agent, and a green dot marks the goal. The animation shows the agent's progress step-by-step.

## Future enhancements 
 * Add Support for Customizable grid sizes \
 * Implement Algorithms like A* or Djikstra 

## Contributions 
 Feel free to submit pull requests or raise issues for enhancements. 