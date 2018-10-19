from collections import deque

def do_successor(node):
	current_state = node.state
	successors =[]
	if current_state[0] == True:
		successors.append(('D', [False] + current_state[1:]))
		OBJECT_LEFT = current_state[3]
		
		if current_state[1] == True:
			if current_state[4] == True:
				OBJECT_LEFT = False
			successors.append(('Ri', current_state[0:1] + [False] + current_state[2:3] + [OBJECT_LEFT] + current_state[4:]))
		else:
			if current_state[4] == True:
				OBJECT_LEFT = True
			successors.append(('L', current_state[0:1] + [True] + current_state[2:3] + [OBJECT_LEFT] + current_state[4:]))
	else:
		successors.append(('U', [True] + current_state[1:]))

	if current_state[2] == True:
		if current_state[0] == False and current_state[1] == current_state[3]:
			successors.append(('H', current_state[0:2] + [False] + current_state[3:4] + [True]))
		else:
			successors.append(('H', current_state[0:2] + [False] + current_state[3:]))
	else:
		if current_state[4] == True:
			successors.append(('Re', current_state[0:2] + [True] + current_state[3:4] + [False]))
		else:
			successors.append(('Re', current_state[0:2] + [True] + current_state[3:]))

	return successors

def step_cost_fn(state, action, result):
	return 1

class Problem:
    #must input initial state, a successor function, and a goal
    def __init__(self, init_state, successor_fn, step_cost, goal):
        """
        Problem contains methods and values to describe a problem that can solve a general problem

        init_state = node describes initial state where search for the solution starts
        successor_fn = function to create new node states based on the specifications of the problem
        step_cost = function to compute for doing an action to move from one node to another 
        goal = node that describes the end goal where search stops
        """
        self.init_state = init_state
        self.successor_fn = successor_fn
        self.step_cost = step_cost
        self.goal = goal

    def goal_test(self, node):
        return self.goal == node
    
    def remove_front(self, fringe, search):
        if search == "bfs":
            return fringe.popleft()
        elif search == "iddfs":
            return fringe.pop()

    def get_path(self, node):
        path = [node]
        curr = node.parent
        print("---------------PATH---------------")
        print(node.action)
        print(node.state)
        while curr is not None:
            path.append(curr)
            print(curr.action)
            print(curr.state)
            curr = curr.parent

        return path

    def init_state(state):
    	label_crane = "Crane: "
    	label_object = "Object: "
    	if state == 0:
    		CLAW_DOWN = False
    		CRANE_RIGHT = False
    		CLAW_CLOSED = False
    		OBJECT_RIGHT = False

    def expand(self, node):
        """
        returns a list of children nodes of node parameter
        """
        successors = []

        for action, result in self.successor_fn(node):
            stp_cost = self.step_cost(node.state, action, result)
            s = ProblemState(result, node, action, stp_cost)
            successors.append(s)

        return successors

    def tree_solve(self, search="bfs"):
        if search == "bfs":
            fringe = deque([]) #fringe is a queue
        elif search == "iddfs":
            fringe = [] #fringe is a regular list but can be used as a stack

        fringe.append(self.init_state)

        counter = 0
        while True:
        	counter = counter + 1
        	if search == "iddfs":
        		while True:
        			print('Depth: ' + str(counter))
        			if not fringe:
        				break

        			node = self.remove_front(fringe, search)
        			depth = node.path_cost
        			print(node.action)
        			print(node.state)

        			if self.goal_test(node):
        				return self.get_path(node)

        			if node.path_cost + 1 <= counter:
        				new_nodes = self.expand(node)
        				for n in new_nodes:
        					fringe.append(n)

        		fringe = []
        		fringe.append(self.init_state)

        	elif search == "bfs":
        		if not fringe: #checks if fringe is empty
        			return None #return null if no solution

        		node = self.remove_front(fringe, search)
        		depth = node.path_cost
        		print('Depth: ' + str(depth))
        		print(node.action)
        		print(node.state)

        		if self.goal_test(node):
        			return self.get_path(node)

        		new_nodes = self.expand(node)

        		for n in new_nodes:
        			fringe.append(n)

class ProblemState:
    # def __new__(cls, state, prev_node = None, action=None, step_cost=0):
    #     """
    #     Only inistantiates node if previous node and action are either both null or both not null

    #     prev_node = previous / parent node of node about to be intialized. Can be null if initial state, but action must also be null.
    #     action = action done to reach node about to be initialized from previous node
    #     state = ordered list of values that describe the state of the node
    #     """
    #     print(state)
    #     if (action is not None and prev_node is not None) or (action is None and prev_node is None):
    #         return super().__init__(prev_node, action, state, step_cost)
    #         print('hi')
    #     else: #don't initialize
    #         return None

    def __init__(self, state, prev_node=None, action=None, step_cost=0):
        self.parent = prev_node
        self.state = state
        self.action = action

        if prev_node is not None:
            self.depth = prev_node.depth + 1
            
            self.path_cost = prev_node.path_cost + step_cost
        else:
            self.depth = 0
            self.path_cost = 0

    def __eq__(self, other):
        if isinstance(other, ProblemState):
            return self.state == other.state
        else:
            return False

# 
print('The Claw')
print('Input initial state: ')
init_state = input()
init_array = []
for i in init_state.split(' '):
	init_array.append(i == 'True')

init_state = ProblemState(init_array)

print('Input goal state: ')
goal_state = input()
goal_array = []
for i in goal_state.split(' '):
	goal_array.append(i == 'True')
goal_state = ProblemState(goal_array)

print('Strategy to be used (bfs or iddfs): ')
strategy = input()

problem = Problem(init_state, do_successor, step_cost_fn, goal_state)
problem.tree_solve(strategy)
