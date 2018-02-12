# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        # Set of all states
        #S = mdp.getStates();

        state = self.mdp.getStates()[2];
        states = self.mdp.getStates();
        for i in range(iterations):
            valuesForActions = self.values.copy();
            for state in self.mdp.getStates():
                finalValue = 0;

                possibleActions = self.mdp.getPossibleActions(state)
                #valuesForActions = util.Counter();
                for action in possibleActions:
                    currentValue = self.computeQValueFromValues(state,action);
                    if finalValue == None or finalValue < currentValue:
                        finalValue = currentValue
                    if finalValue == None:
                        finalValue = 0
                    valuesForActions[state] = finalValue;
            self.values = valuesForActions;



         #Calculamos la utilidad de cada posible estado y usamos estas para seleccionar la accion
        #MDP (MARKOV DECIVISION PROBLEM)
        """
        for i in range(iterations): #Calculamos para el numero de iteraciones maximas que tendremos
          valores = self.values.copy() #Sobrescribimos
          for state in self.mdp.getStates(): #Obtenemos los estados de nuestro problema MDP
            action = self.computeActionFromValues(state) #Obtenemos la accion
            actual = self.computeQValueFromValues(state,action) #Obtenemos su valor
            valores[state] = actual #Actualizamos el resultado final

          self.values = valores
        # https://github.com/shiro873/pacman-projects/blob/master/p3_reinforcement_learning/valueIterationAgents.py
        """
        #BORRAR
        state = self.mdp.getStates()[2]
        states = self.mdp.getStates()
        for i in range(iterations):
            valuesCopy = self.values.copy()
            for state in states:
                finalValue = None
                for action in self.mdp.getPossibleActions(state):
                    currentValue = self.computeQValueFromValues(state,action)
                    if finalValue == None or finalValue < currentValue:
                        finalValue = currentValue
                    if finalValue == None:
                        finalValue = 0
                    valuesCopy[state] = finalValue
            self.values = valuesCopy
        #FIN BORRAR
        """

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        #  Agafem el q-value del (state, action) pair a partir de la value function donada per self.values.
        #  returns the Q-value of the (state, action) pair given by the value function given by self.values.
        qValue = 0;
        transicions = self.mdp.getTransitionStatesAndProbs(state,action);
        # A la posicio 0 tenim el seguent estado, i a la posicio 1 la probabilitat
        for transicio in transicions:
		    qValue += transicio[1] * (self.mdp.getReward(state, action, transicio[0]) + (self.discount*self.values[transicio[0]]))
        return qValue
        util.raiseNotDefined()










    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"

        # Aqui computem la millor accio a partir de la value function donada per self.values.
        # Aqui son las flechas del gridworld
        accions = self.mdp.getPossibleActions(state);

        # Si tenim 0 accions possibles
        if len(accions) == 0:
            return None
        value = None
        result = None

        possibleActions = self.mdp.getPossibleActions(state)

        valuesForActions = util.Counter()
        for action in possibleActions:
        	transitionStatesAndProbs = self.mdp.getTransitionStatesAndProbs(state, action)
        	valueState = 0
        	for transition in transitionStatesAndProbs:
        		valueState += transition[1] * (self.mdp.getReward(state, action, transition[0]) + self.discount * self.values[transition[0]])
        	valuesForActions[action] = valueState


        """
        value = None
        result = None
        for action in possibleActions:
            temp = self.computeQValueFromValues(state, action)
            if value == None or temp > value:
                value = temp
                result = action

        return result
        """

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
