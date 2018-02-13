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
        # Bucle troncal

        states = self.mdp.getStates();
        for i in range(iterations):
            valores = self.values.copy();
            for state in states:
                action = self.computeActionFromValues(state);
                valor = self.computeQValueFromValues(state,action);
                valores[state] = valor;
            self.values = valores;

         #Calculamos la utilidad de cada posible estado y usamos estas para seleccionar la accion
        #MDP (MARKOV DECIVISION PROBLEM)
        """
        # https://github.com/shiro873/pacman-projects/blob/master/p3_reinforcement_learning/valueIterationAgents.py
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
        if action is None: #En caso de ninguna accion, devolvemos un valor por defecto, en este caso cero
            return 0.0
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
        actions = self.mdp.getPossibleActions(state);
        # Valor menys "infinit"
        maxValue = -9999999;
        resultat = None;
        for action in actions:
            valor = self.computeQValueFromValues(state,action);
            if valor > maxValue:
                maxValue = valor;
                resultat = action;
        return resultat;

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
