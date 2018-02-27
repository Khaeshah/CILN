# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)

        # Aqui tenim el mapa
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        # Nova posicio
        newPos = successorGameState.getPacmanPosition()
        # Mapa de las foods
        newFood = successorGameState.getFood()
        # Estats dels fantasmes
        newGhostStates = successorGameState.getGhostStates()
        # Temps restant amb powerup
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]


        "*** YOUR CODE HERE ***"
        # Agafem la posicio del fantasma enemic i calculem la distancia a ell
        posicioFantasma = currentGameState.getGhostPosition(1);
        distanciaEnemic = util.manhattanDistance(posicioFantasma, newPos);

        distanciaMenjar = [manhattanDistance(newPos,foodPos) for foodPos in newFood.asList()]

        puntuacioFinal = successorGameState.getScore()
        puntuacioFantasma = 0;
        puntuacioMenjar = 0;

        # Evitem el fantasma
        if distanciaEnemic > 2:
            if len(distanciaMenjar):
                puntuacioMenjar = 5 / min(distanciaMenjar);
            else:
                puntuacioMenjar = 100;
        else:
            puntuacioFantasma = -2000;

        puntuacioFinal += puntuacioMenjar + puntuacioFantasma;
        return puntuacioFinal;

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

    def isTerminal(self, state, depth, agent):
        return depth == self.depth or \
               state.isWin() or \
               state.isLose() or \
               state.getLegalActions(agent) == 0

    # is this agent pacman
    def isPacman(self, state, agent):
        return agent % state.getNumAgents() == 0


class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    """
        PELO
        https://github.com/georgemouse/multiagent/blob/master/multiAgents.py
        https://github.com/filR/edX-CS188.1x-Artificial-Intelligence/blob/master/Project%202%20-%20Multi-Agent%20Pacman/multiAgents.py
        https://github.com/douglaschan32167/multiagent/blob/master/multiAgents.py
    """
    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        return self.MinimaxSearch(gameState, 1, 0 )

    def MinimaxSearch(self, gameState, currentDepth, agentIndex):
        "Cas base"
        # Si intentem explorar mes del que ens han especificat o s'ha acabat la partida, parem
        if currentDepth > self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

        "MiniMax"
        # Agafem totes les accions que podem fer
        accions = gameState.getLegalActions(agentIndex);
        numeroAgents = gameState.getNumAgents();
        # Actualitzem la profunditat
        nextProfunditat = currentDepth
        # Actualitzem el seguent agent
        nextIndex = agentIndex + 1
        # Si hem mirat tots els agents, augmentem el nivell de profunditat
        if nextIndex >= numeroAgents:
            nextIndex = 0
            nextProfunditat = nextProfunditat + 1


        # Agafem una millor accio o agafem un minimax result
        resultats = [];
        for accio in accions:
            nextGameState = gameState.generateSuccessor(agentIndex, accio);
            result = self.MinimaxSearch(nextGameState, nextProfunditat, nextIndex);
            resultats.append(result);

        # Primer moviment del pacman
        if currentDepth == 1 and agentIndex == 0: # pacman first move
            millorMoviment = max(resultats)

            indexes = range(len(resultats));
            bestIndices = [];
            for index in indexes:
                if resultats[index] == millorMoviment:
                    bestIndices.append(index);

            # Com podem tenir mes de un bon index, agafem el primer com a opcio
            chosenIndex = bestIndices[0];
            #chosenIndex = random.choice(bestIndices) # Pick randomly among the best
            return accions[chosenIndex]

        # Si soc un max, agafo el max dels resultats
        if agentIndex == 0:
            millorMoviment = max(resultats)
            return millorMoviment
        # Si soc un min, agafo el min dels resultats
        else:
            millorMoviment = min(resultats)
            return millorMoviment



class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        def dispatch(state, depth, agent, A=-9999999.0, B=9999999.0):
            if agent == state.getNumAgents():  # next depth
                depth += 1
                agent = 0

            if self.isTerminal(state, depth, agent):  # dead end
                return self.evaluationFunction(state), None

            if self.isPacman(state, agent):
                return getValue(state, depth, agent, A, B, -9999999.0, max)
            else:
                return getValue(state, depth, agent, A, B, 9999999.0, min)

        def getValue(state, depth, agent, A, B, ms, mf):
            bestScore = ms
            bestAction = None

            for action in state.getLegalActions(agent):
                successor = state.generateSuccessor(agent, action)
                score,_ = dispatch(successor, depth, agent + 1, A, B)
                bestScore, bestAction = mf((bestScore, bestAction), (score, action))

                if self.isPacman(state, agent):
                    if bestScore > B:
                        return bestScore, bestAction
                    A = mf(A, bestScore)
                else:
                    if bestScore < A:
                        return bestScore, bestAction
                    B = mf(B, bestScore)

            return bestScore, bestAction

        _,action = dispatch(gameState, 0, 0)
        return action
class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
