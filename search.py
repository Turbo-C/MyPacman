# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        # type: (object) -> object
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        :rtype: object
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    visited_node = []
    stack_node = util.Stack()
    result = []
    sub_result = []
    if problem.isGoalState(problem.getStartState()):
        return []
    stack_node.push((problem.getStartState(), []))
    while not stack_node.isEmpty():
        node = stack_node.pop()
        result = node[1]
        sub_result = list(result)
        if problem.isGoalState(node[0]):
            return result
        if node[0] not in visited_node:
            visited_node.append(node[0])
        Succerssors=problem.getSuccessors(node[0])
        succ=[k for k in Succerssors if k[0] not in visited_node]
        if (len(succ) != 0):
                    stack_node.push(node)
                    sub_result.append(succ[0][1])
                    stack_node.push((succ[0][0],sub_result))

    "*** YOUR CODE HERE ***"

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    visited_node = []
    stack_node = util.Queue()
    result = []
    sub_result = []
    final_result=[]
    if problem.isGoalState(problem.getStartState()):
        return []
    stack_node.push((problem.getStartState(), []))
    visited_node.append(problem.getStartState())
    while not stack_node.isEmpty():
        node = stack_node.pop()
        result = node[1]
        if problem.isGoalState(node[0]):
            visited_node.append(node[0])
            return result
        for record in problem.getSuccessors(node[0]):
            leaf = record[0]
            action = record[1]
            sub_result = list(result)
            if not leaf in visited_node:
                visited_node.append(leaf)
                sub_result.append(action)
                stack_node.push((leaf,sub_result))
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    path = []
    explored = []
    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(), []), 0)
    visited={}
    while frontier.isEmpty() != 1:
        node = frontier.pop()
        explored.append(node[0])
        if problem.isGoalState(node[0]):
            return node[1][0]
        for successor, nextAction, cost in problem.getSuccessors(node):
            if successor not in explored:
                g_score = problem.getCostOfActions(path) + cost
                addPath = path + [nextAction]
                frontier.push((successor, addPath), g_score)
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    path = []
    explored = []
    frontier = util.PriorityQueue()
    h_score = heuristic(problem.getStartState(), problem)
    frontier.push((problem.getStartState(), []), h_score)
    while frontier.isEmpty() != 1:
        node, path = frontier.pop()
        if problem.isGoalState(node):
            return path
        explored.append(node)
        for successor, nextAction, cost in problem.getSuccessors(node):
            if successor not in explored:
                addPath = path + [nextAction]
                f_score = problem.getCostOfActions(addPath) + heuristic(node, problem)
                frontier.push((successor, addPath), f_score)
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
