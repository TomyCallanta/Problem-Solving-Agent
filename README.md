## Problem Solving Agent
# The Claw
### by Tomy Callanta and Gab Barbudo

## Description
The Claw is a problem solving agent which has the aim to transfer an object to a different location. It first checks whether there is an object under the claw and if there is, it transfers the object from the left side to the right side or vice versa.

This agent may be used in factories or for any type of work that needs an automated machine that transfers objects from place to place.

## Agent and Environment Specifications
- Environment has two (2) sides: left (L) and right (R)
- Only one (1) side can contain an object
- Goal-based agent may be in L or R
- Agent can perceive if a side contains an object
- Agent can only hold or release an object, and move to the right or to the left, and upward or downward
![The Claw](/images/agent.png)

## Successor Functions
- Down (D): Crane moves downward
- Up (U): Crane moves upward
- Right (Ri): Crane moves to the right
- Left (L): Crane moves to the left
- Hold (H): Crane Claw picks up object
- Release (Re): Crane Claw lets go of object

## Instructions
1. Run the following command in the directory `/code` to start the program.
```
$ python base.py
```

2. Input the desired initial state.

The program asks for the following:

```
clawUp? craneIsLeft? clawOpen? objectIsLeft? objectHeld?
```
Sample input:
```
Input initial state:
True True True True False
```

3. Input the desired goal state.

Sample input:
```
Input goal state:
True False True False False
```

4. Input `Y` if a heuristic will be used; `N` if no.

Sample input:
```
Do you want to use a heuristic? (Y or N):
Y
```

5. If a heuristic will be used, choose from `A` or `B`.

Sample input:
```
Which heuristic do you want to use? (A or B):
A
```

6. If no heuristic will be used, choose an uninformed search strategy. Input `bfs` for Breadth-First Search or `iddfs` for Iterative Deepening Depth-First Search.

Sample input:
```
Strategy to be used (bfs or iddfs):
bfs
```

7. The output will be the series of actions and states the agent passes through to arrive at the goal state. The `PATH` section outputs the path from the initial state to the goal state in reverse order: the goal state at the top and the initial state at the bottom.