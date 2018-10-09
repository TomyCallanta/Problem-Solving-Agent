from collections import deque

class Problem:
    #must input initial state, a successor function, and a goal
    def __init__(self, init_state, successor_fn, step_cost, goal):
        """
        Problem contains methods and values to describe a problem that can be solve a general problem

        init_stat = node describes initial state where search for the solution starts
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
        elif search == "dfs":
            return fringe.pop()

    def get_path(self, node):
        path = [node]
        while node.parent is not None:
            path.append(node.parent)

        return path

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
        elif search == "dfs":
            fringe = [] #fringe is a regular list but can be used as a stack

        fringe.append(self.init_state)

        while True:
            if not fringe: #checks if fringe is empty
                return None #return null if no solution
            
            node = self.remove_front(fringe, search)

            if self.goal_test(node):
                return self.get_path(node)

            new_nodes = self.expand(node)

            for n in new_nodes:
                fringe.append(n)

class ProblemState:
    def __new__(cls, state, prev_node = None, action=None, step_cost=0):
        """
        Only inistantiates node if previous node and action are either both null or both not null

        prev_node = previous / parent node of node about to be intialized. Can be null if initial state, but action must also be null.
        action = action done to reach node about to be initialized from previous node
        state = ordered list of values that describe the state of the node
        """
        if (action is not None and prev_node is not None) or (action is None and prev_node is None):
            return super().__init__(prev_node, action, state, step_cost)
        else: #don't initialize
            return None

    def __init__(self, state, prev_node=None, action=None, step_cost=0):
        self.parent = prev_node
        self.state = state

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
