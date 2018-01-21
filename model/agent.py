# agent.py

""" agent.py

Class: Agent.

    Attributes:
        amp (double): Maximum arousal for agent.
        hab_rate (double): Rate of habituation for a stimulus.
        hab_scalar (double): Magnitude of habituation.
        act_thr (double): Activation threshold for agent to express.
        rec_thr (double): Recharge threshold fora gent to recharge arousal.
        decay_rate (double): Rate of arousal decay for agent.

"""

import numpy as np
import math

class Agent():

    def __init__(self, id, n_steps):

        # Agent identifier
        self._id = id

        # Specs
        self.amp = 10.0
        self.hab_rate = 0.7
        self.hab_scalar = 0.0
        self.act_thr = 7.0
        self.rec_thr = 3.0
        self.dec_rate = 1.0

        # Agent memory characteristics
        self.recent_stimulations = 0 # count of recent stimulations, behaves as adaptation multiplier
        self.last_stimulation = 0 # most recent stimulation time
        self.recent_interactions = 0
        self.last_interaction = 0

        #: Current states
        self.current = {}
        self.current['arousal'] = 0.0
        self.current['valence'] = 0.0

        #: Data
        self.data = {}
        self.data['arousal'] = np.zeros(n_steps + 1)
        self.data['valence'] = np.zeros(n_steps + 1)

    def habituate(self, change):
        """Habituate an agent self with some change. We expect
            the outcome of a stimulus to be reflected at the next time step.

        Args:
            self (obj): Agent object.
            change (double): Change amount.

        """
        self.hab_scalar += change

    def stimulate(self, stimulus):
        """Stimulate an agent self with stimulus. We expect
            the outcome of a stimulus to be reflected at the next time step.

        Args:
            self (obj): Agent object.
            stimulus (obj): Stimulus object.

        """
        #: Set current arousal of self to linearly weighted stimulation
        change = (self.amp - self.current['arousal']) * stimulus['magnitude']
        self.current['arousal'] = change * np.power(self.hab_rate, self.hab_scalar) + self.current['arousal']
        self.habituate(change)

    def perceive(self, other, weight):
        """Agent self percieves from expressing agent other with
            weight directed other --> self. We expect the outcome of
            the perception to be reflected at the time step.

        Args:
            self, other (obj): Agent object.
            weight w (double): weight value between agents b --> a.

        Returns:
            double: Returns new weight.

        """
        #scalar = 1 / (1 - np.exp(-other.current['arousal']))

        #: Set current arousal of self to linearly weighted interaction stimulation
        change = weight * (self.amp - self.current['arousal'])
        self.current['arousal'] = change * np.power(self.hab_rate, self.hab_scalar) + self.current['arousal']
        self.habituate(change)

        #: Update directed weight
        weight = (1 - weight) * (0.1) + weight

        #: return new weight
        return weight

    def express(self, other, weight):
        """Agent self expresses toward agent other with
            weight directed other --> self. We expect the the outcome of
            the expression to be reflected at the next time step.

        Args:
            self, other (obj): Agent object.
            weight (double): Weight value between agents b --> a.

        Returns:
            double: Returns new weight.

        """
        #scalar = 1 / (1 - np.exp(-self.current['arousal']))

        #: Set current arousal of self to linearly weighted interaction stimulation
        change = weight * (self.amp - self.current['arousal'])
        self.current['arousal'] = change * np.power(self.hab_rate, self.hab_scalar) + self.current['arousal']

        #: Update directed weight
        weight = (1 - weight) * (0.1) + weight

        #: return new weight
        return weight

    def above_rec_thr(self):
        """Check if agent self is above recharge threshold at time step.

        Args:
            self (obj): Agent object.

        Returns:
            bool: Returns True if above recharge threshold.

        """

        if self.current['arousal'] > self.rec_thr:
            return True
        else:
            return False

    def above_act_thr(self):
        """Check if agent self is above activation threshold at time step.

        Args:
            self (obj): Agent object.

        Returns:
            bool: Returns True if above activation threshold.

        """

        if self.current['arousal'] > self.act_thr:
            return True
        else:
            return False

    def update(self, step, dt):
        """Update an agent self.

        Args:
            self (obj): Agent object.

        """

        decay = 1 / (1 + self.dec_rate * dt)
        self.data['arousal'][step + 1] = decay * self.current['arousal']
        self.data['valence'][step + 1] = self.current['valence']

        self.current['arousal'] = self.data['arousal'][step + 1]
        self.current['valence'] = self.data['valence'][step + 1]

        if self.hab_scalar > 0:
            self.hab_scalar -= 0.1
