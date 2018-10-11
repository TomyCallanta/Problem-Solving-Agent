"""
Just the functions
Returns a path from start to goal

Notes from Gab:
	- I'll be on immersion from Friday to Sunday :((
	- How will you implement BFS?
	- Do you want to use 'The Claw' or nah?
"""

def dls(path, goal, depth):
	"""
    Return the depth limited search path from a subpath to the goal.
    
    path: the current path of Nodes being taken
    goal: the label of the goal node
    depth: the depth in the graph to search
    """
    curr = path[-1]
	if path == goal:
		return path
	if depth <= 0:
		return None
	for i in path:
		result = dls(i, goal, depth-1)
		if result is not None:
			return result


def iddfs(start, goal, max_depth):
	"""
	Return the IDDFS path from the start node to the node with the goal label.

	start: the node to start at
    goal: the label of the goal node
    max_depth: the maximum depth to search
	"""
	for depth in range(0, max_depth):
		result = dls([start], goal, depth)
		if result is None:
			continue
	return result