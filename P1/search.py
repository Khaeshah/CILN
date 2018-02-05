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
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
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

    "*** YOUR CODE HERE ***"

    struct = util.Stack();
    setCaminos = [];
    visited = set();

    startState = problem.getStartState(); #posicion inicial
    #nodo,accion,cost
    struct.push((startState,[],[]));
    setCaminos.append([]);
    # Mientras haya algo en la pila
    # Contador de debug
    i = 0;

    while not struct.isEmpty():

        # Cojo un nodo temporal de la pila
        actualNode = struct.pop();
        nodePos = actualNode[0]; # POSICION
        actions = actualNode[1]; # ACCION
        cost = actualNode[2]; # COSTE

        # Ultimo set de setCaminos en lista setCaminos
        actualAction = setCaminos.pop();
        """
        print "Actual Actions: ";
        print actualAction;
        print "Posicion del nodo: ";
        print nodePos;
        print "Accion que hemos hecho: ";
        print actions;
        """
            # Si tenim goal
        if problem.isGoalState(nodePos):
            print "TROBAT! Accions per arribar al objectiu: ";
            #print actualAction;
            return actualAction;
        # contador per fer debug
        j = 0;
        # Si nuevo nodo
        if nodePos not in visited:
            # Anyadimos a visitados
            visited.add(nodePos)
            # Para los nodos adyacentes
            for nodePos,actions,cost in problem.getSuccessors(nodePos):
                # Los anyadimos a la pila
                struct.push((nodePos,actions,cost));
                #Aniadimos set de setCaminos actual, movs +  accions
                setCaminos.append(actualAction + [actions]);
                #print "Cas: "+ str(i)+ " Succ: " + str(j) + " " + str(actions);

                j = j+1;
        i = i + 1;
        #print "\n"
    util.raiseNotDefined()
    """
    print "acciones anteriores: "
    print actualAction
    print "\n"
    print "acciones nuevas: "
    print [actions]
    print "\n"
    """

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    struct = util.Queue();
    setCaminos = util.Queue();
    visited = [];

    startState = problem.getStartState(); #posicion inicial
    #nodo,accion,cost
    struct.push((startState,"Stop",0));
    setCaminos.push([]);
    # Mientras haya algo en la pila
    i = 0;

    while not struct.isEmpty():

    # Cojo un nodo temporal de la pila
        actualNode = struct.pop();
        nodePos = actualNode[0]; # POSICION
        actions = actualNode[1]; # ACCION
        cost = actualNode[2]; # COSTE


        # Ultimo set de setCaminos en lista setCaminos
        actualAction = setCaminos.pop();
        """
        print "Actual Actions: ";
        print actualAction;
        print "Posicion del nodo: ";
        print nodePos;
        print "Accion que hemos hecho: ";
        print actions;
        """
            # Si tenim goal
        if problem.isGoalState(nodePos):
            print "TROBAT! Accions per arribar al objectiu: ";
            #print actualAction;
            return actualAction;

        j = 0;
        # Si nuevo nodo
        if nodePos not in visited:
            # Anyadimos a visitados
            visited.append(nodePos)
            # Para los nodos adyacentes
            for nodePos,actions,cost in problem.getSuccessors(nodePos):
                # Los anyadimos a la pila
                struct.push((nodePos,actions,cost));
                #Aniadimos set de setCaminos actual, movs +  accions
                setCaminos.push(actualAction + [actions]);
                #print "Cas: "+ str(i)+ " Succ: " + str(j) + " " + str(actions);
                j = j+1;
        i = i + 1;
        #print "\n"
    util.raiseNotDefined()
    util.raiseNotDefined()

# UCS utilitza una cua de prioritat. La prioritat es el cost cumulatiu cap a un node.
# UCS dona al minim cost acumulat la maxima prioritat.
# UCS retorna el primer cami trobat, no tots.
# UCS retorna un cami optim en termes de cost.
# UCS es el millor algoritmo actual que no utilitza heuristicas.
def uniformCostSearch(problem):
    "*** YOUR CODE HERE ***"
    struct = util.PriorityQueue();
    setCaminos = util.PriorityQueue();
    visited = set();

    startState=problem.getStartState(); #posicion inicial
    #           [pos,accion,cost], coste acumulado
    struct.push([(startState,[],[]),0],0); # Node i coste, con el acumulativo
    setCaminos.push([],0);

    while not struct.isEmpty():
        # Cojo un nodo
        actualNode = struct.pop();
        nodePos = actualNode[0][0]; # POSICION
        actions = actualNode[0][1]; # ACCION
        cost = actualNode[0][2]; # COSTE

        actualAction = setCaminos.pop();

        # Si es goalstate:
        if problem.isGoalState(nodePos):
            print "TROBAT! Accions per arribar al objectiu: ";
            #print actualAction;
            return actualAction;

        # Si nuevo nodo
        if nodePos not in visited:
            # Anyadimos a visitados
            visited.add(nodePos)
            # Para los nodos adyacentes
            for nodePos,actions,cost in problem.getSuccessors(nodePos):
                # Actualnode contiene el coste acumulado
                # cost es el coste que vemos para ir a otro nodo
                cumulativeCost = actualNode[1] + cost;

		        #  (        [nodo]         ,  coste      , coste acumulao)
                struct.push([(nodePos,actions,cost), cumulativeCost ], cumulativeCost);
                #	       (   set de acciones      ,  coste acumulado  )
                setCaminos.push(actualAction + [actions], cumulativeCost    );
        #print "\n"

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    struct = util.PriorityQueue();
    setCaminos = util.PriorityQueue();
    visited = [];

    startState=problem.getStartState(); #posicion inicial
    #[nodo,accion,cost], coste acumulado
    struct.push([(startState,[],[]),0],0); # Node i coste, con el acumulativo
    setCaminos.push([],0);

    while not struct.isEmpty():
        # Cojo un nodo
        actualNode = struct.pop();
        nodePos = actualNode[0][0]; # POSICION
        actions = actualNode[0][1]; # ACCION
        cost = actualNode[0][2]; # COSTE

        actualAction = setCaminos.pop();

        # Si es goalstate:
        if problem.isGoalState(nodePos):
            print "TROBAT! Accions per arribar al objectiu: ";
            #print actualAction;
            return actualAction;

        # Si nuevo nodo
        if nodePos not in visited:
            # Anyadimos a visitados
            visited.append(nodePos)
            # Para los nodos adyacentes
            for nodePos,actions,cost in problem.getSuccessors(nodePos):
                # Actualnode contiene el coste acumulado
                # cost es el coste que vemos para ir a otro nodo
                cumulativeCost = actualNode[1] + cost + heuristic(nodePos,problem);
                # 	   (        [nodo]         ,  coste      , coste acumula + heuristik)
                struct.push([(nodePos,actions,cost), actualNode[1] + cost], cumulativeCost);
                #	       (   set de acciones      ,  coste acumulado  )
                setCaminos.push(actualAction + [actions], cumulativeCost    );
                #print "\n"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
