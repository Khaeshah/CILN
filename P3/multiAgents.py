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
        maxAccio = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == maxAccio]
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
        "*** YOUR CODE HERE ***"

        """ Number of ghosts in game """
        numFantasmes = gameState.getNumAgents() - 1
        alpha = -9999999
        beta = 9999999

        def maxAgent(gameState, depth, alpha, beta):

            """ If game is finished """
            if depth > self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)

            # Initialize best action and score
            # v = -INF in max
            bestAccio = None
            maxValor = -9999999

            accions = gameState.getLegalActions(self.index) # 0 is the index for pacman

            """ For each action we have to obtain max score of min movements """
            for action in accions:
                successorGameState = gameState.generateSuccessor(self.index, action)
                valor = minAgent(successorGameState, depth, 1, alpha, beta)
                # Update best max score
                if(valor > maxValor):
                    maxValor = valor
                    bestAccio = action

                if(maxValor > beta):
                    valorFinal = maxValor;
                    return valorFinal;
                alpha = max(alpha, maxValor)

            # Recursive calls have finished -> depth = initial depth -> return best action
            if depth == 0:
                return bestAccio
            # We are in different depth, we need to return a score
            else:
                return maxValor

        def minAgent(gameState, depth, ghost, alpha, beta):

            if depth > self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)

            maxValor = 9999999
            # Legal actions for selected ghost
            accions = gameState.getLegalActions(ghost)

            for action in accions:
                successorGameState = gameState.generateSuccessor(ghost, action)
                if(ghost < numFantasmes):
                    # There are still ghosts to move
                    # Using ghost + 1 to select the next ghost
                    valor = minAgent(successorGameState, depth, ghost + 1, alpha, beta) # returns a score
                else:
                    # Last ghost -> next turn is for pacman
                    if(depth == self.depth - 1): # IF IT IS A TERMINAL
                        valor = self.evaluationFunction(successorGameState)
                    else:
                        # If it is not a terminal
                        valor = maxAgent(successorGameState, depth + 1, alpha, beta) # returns a score
                # Update best min score
                maxValor = min(valor, maxValor)

                if(maxValor < alpha):
                    return maxValor
                beta = min(beta, maxValor)
            return maxValor


        # RETURN AN ACTION
        return maxAgent(gameState, 0, alpha, beta) # depth = 0

        util.raiseNotDefined()
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
