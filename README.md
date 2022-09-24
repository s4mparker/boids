# Boids

A simple boids simulation that is built using agent-based modelling principles.

![Demonstration Video](boids.gif)

## Usage

- To run the application, execute `python3 run.py`
- To update the parameters of the simulation, update the `parameters.json` file included in the root directory
- The purpose of each parameter is described in the *Parameters* section

## Parameters

The simulation's parameters are described below.

| *Parameters* | *Description* |
| ---------- | ----------- |
| SCREEN | Screen / display dimensions |
| ENVIRONMENT | Environment dimensions (these are scaled down to the screen dimensions at rendering) |
| XREPULSION | The width margin of the screen where the boids will begin to turn to avoid hitting a wall (e.g. 0.1 = 10% & 90%) |
| YREPULSION | The height margin of the screen where the boids will begin to turn to avoid hitting a wall (e.g. 0.1 = 10% & 90%) |
| COLOURS | A list of colours used by the simulation |
| AGENTS | A list of agents that are used by the simulation |

The agents' parameters are described below.

| *Parameters* | *Description* |
| ---------- | ----------- |
| COLOUR | The colour of the agents |
| QUANTITY | The number of agents to simulate |
| SIZE | The size of the agents |
| SPEED | The speed at which the agents move (this is represented using a normal distribution) |
| TURNING | The speed at which agents turn (this is represented using a normal distribution) |
| FORCE_WEIGHTS | The proportions with which the agents value various forces |
| INNER_RADIUS | The radius in which agents of the same type attempt to move away from each other |
| OUTER_RADIUS | The radius in which agents of the same type attempt to move towards each other and in which agents of different types attempt to move away from each other |

## Creditations

This project is heavily based on Craig Reynolds' work on Boids. More information on his research can be found [here] (<https://www.red3d.com/cwr/boids/>). I also found [this work] (<https://vanhunteradams.com/Pico/Animal_Movement/Boids-algorithm.html>) by V. Hunter Adams to be extremely helpful.

## Dependancies

- Python 3
- pygame
