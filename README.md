# Boids

A simple boids simulation built using agent-based modelling principles.

Each boid ('bird-oid object') follows a simple ruleset in order to navigate themselves around the simulated environment. The simulation allows for multiple types of boids within a single environment, each with its own parameters. This enables each type of boid to exhibit its own unique behaviour and collectively produces complex emergent behaviour among the population.

![Demonstration Video](boids.gif)

## Usage

- To run the application, execute `python3 run.py`
- To update the parameters of the simulation, update the `parameters.json` file included in the project's root directory

## Parameters

The simulation's parameters can be broken down into two types: environment and agents.

- The environment parameters are related to the simulated environment. For example, the environment's size or the environment's margins in which agents attempt to avoid hitting a wall.
- The agent parameters are related to the various agents that inhabit the simulated environment. For example, the quantity of a certain type of agent or a specific agent's colour.

### Environment Parameters

The environment's parameters are detailed in the table below.

| **Parameters** | **Description** |
| ---------- | ----------- |
| `SCREEN` | The dimensions of the displayed window |
| `ENVIRONMENT` | The dimensions of the simulated environment |
| `XREPULSION` | The point at which agents will attempt to steer away from hitting either the left / right 'walls' (boundaries of the environment) |
| `YREPULSION` | The point at which agents will attempt to steer away from hitting either the top / bottom 'walls' (boundaries of the environment) |
| `COLOURS` | A list of RGB colours that are used in the simulation |
| `AGENTS` | A list of agent specifications that inhabit the simulated environment |

### Agent Parameters

The agents' parameters are detailed in the table below. Each specification represents a single type of agent; therefore if you wish to simulate two types of agents, you will need to include two specifications within the `AGENTS` environment parameter.

In the table below, the term 'agents' refer to a single, specific type of agent.

| **Parameters** | **Description** |
| ---------- | ----------- |
| `COLOUR` | The colour of the agents |
| `QUANTITY` | The number of agents to simulate |
| `SIZE` | The size of the agents |
| `SPEED` | The speed at which the agents move (normal distribution) |
| `TURNING` | The speed at which the agents turn (normal distribution) |
| `FORCE_WEIGHTS` | The proportions with which the agents value the various forces |
| `INNER_RADIUS` | The radius in which agents of the same type attempt to move away from each other |
| `OUTER_RADIUS` | The radius in which agents of the same type attempt to move towards each other and in which agents of different types attempt to move away from each other |

There are 4 types of forces that may be imposed on an agent.

| **Force** | **Description** |
| --------- | --------------- |
| `REPULSE LIKE` | Repulsion from agents of the same type that are within the agent's `INNER_RADIUS` area |
| `REPULSE UNLIKE` | Repulsion from agents of a different type that are within the agent's `OUTER_RADIUS` area |
| `ALIGN` | Desire to point the agent in the same direction as other agents of the same type that are within the agent's `OUTER_RADIUS` area |
| `COHESION` | Attraction towards agents of the same type that are within the agent's `OUTER_RADIUS` area |

These forces are weighted relatively using an agent's `FORCE_WEIGHTS` parameters.

## Creditations

This project is heavily based on Craig Reynolds' work on boids, of which more information can be found [here](<https://www.red3d.com/cwr/boids/>). I also found the work by V. Hunter Adams, found [here](<https://vanhunteradams.com/Pico/Animal_Movement/Boids-algorithm.html>), to be extremely helpful.

## Dependancies

- Python 3
- pygame
