## Problem Solving Agent
# The Claw
### by Tomy Callanta and Gab Barbudo

## Agent and Environment Specifications
- Environment has two (2) sides: left (L) and right (R)
- Only one (1) side can contain an object
- Goal-based agent may be in L or R
- Agent can perceive if a side contains an object
- Agent can only hold or release an object, and move to the right or to the left, and upward or downward

## Successor Functions
- Down (D): Crane moves downward
- Up (U): Crane moves upward
- Right (Ri): Crane moves to the right
- Left (L): Crane moves to the left
- Hold (H): Crane Claw picks up object
- Release (Re): Crane Claw lets go of object

## How to start the program
1. Input the desired initial state.
2. Input the desired goal state.
3. Choose the search strategy to be used. Input 'bfs' for Breadth-First Search or 'iddfs' for Iterative Deepening Depth-First Search.
4. The output will be the series of actions and states the agent passes through to arrive at the goal state.