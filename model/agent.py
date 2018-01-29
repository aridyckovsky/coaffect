# agent.py

""" agent.py

Class: Agent.

    Attributes:
        amp (double): Maximum arousal for agent.
        act_thr (double): Activation threshold for agent to express.
        rec_thr (double): Recharge threshold fora gent to recharge arousal.
        decay_rate (double): Rate of arousal decay for agent.

"""

import numpy as np
import math

class Agent():

    def __init__(self, id, n_steps, position):

        # Agent identifier
        self._id = id
        self.position = position

        # Specs
        self.amp = 10.0
        self.act_thr = 7.0
        self.rec_thr = 3.0
        self.dec_rate = .5

        # Agent memory characteristics
        self.recent_stimulations = 0 # count of recent stimulations, behaves as adaptation multiplier
        self.last_stimulation = 0 # most recent stimulation time
        self.recent_interactions = 0
        self.last_interaction = 0

        #: Memory of stimuli and interactions
        self.memory = {}
        self.memory['stimulus'] = {}
        self.memory['perception'] = {}
        self.memory['expression'] = {}

        #: Current states
        self.current = {}
        self.current['arousal'] = 0.0
        self.current['valence'] = 0.0

        #: Data
        self.data = {}
        self.data['arousal'] = np.zeros(n_steps + 1)
        self.data['valence'] = np.zeros(n_steps + 1)

    def expectation(self, stimulus):
        """Expectation of a stimulus relative to previous experiences
            and looming potential stimulus.

            Args:
                self (dict): Agent object.
                potential (dict): kind and known features of
                    potential stimulus

        """

        #: displacement of potential stimulus relative to agent position
        d = self.position - stimulus.position

    def habituation(self, category, identifier, time):
        """Habituation to a given stimulus category and kind from past occurrences.

        Args:
            self (dict): Agent object.
            category (str): Category of event (i.e., stimulus, expression)
            identifier (str): Identifier of event (i.e., stimulus, expression)
            time (float): time of event

        Returns:
            habituation (float)

        """
        past = self.memory[category][identifier]
        _sum = 0
        for s in past:
            # impacts scaled by time since past event
            _sum += s['impact']/(time - s['time'] + 1)
            return min(_sum, 5) / 5 # TEMP scaling from 0 to 1

    def stimulate(self, stimulus, time, dt):
        """Stimulate an agent self with stimulus. We expect
            the outcome of a stimulus to be reflected at the next time step.

        Args:
            self (obj): Agent object.
            stimulus (obj): Stimulus object.

        """
        kind = stimulus['kind']
        strength = stimulus['strength']
        direction = stimulus['direction']

        #: get habituation to calculate excitation of given stimulus
        if kind not in self.memory['stimulus']:
            self.memory['stimulus'][kind] = []
            habituation = 0
        else:
            habituation = self.habituation('stimulus', kind, time)
        excitation = strength * (1 - habituation) * dt * self.amp + self.current['arousal']

        #: Update current arousal and valence relative to stimulus
        if excitation > self.amp:
            self.current['arousal'] = self.amp
        else:
            self.current['arousal'] = excitation # cannot be above self.amp

        self.current['valence'] = direction # TODO

        #: Update memory of given stimulus kind
        self.memory['stimulus'][kind].append({
            'time': time, # time of stimulus event
            'impact': strength, # impact/amount of feeling
        })

    def perceive(self, other, perception, time, dt):
        """Agent self percieves from expressing agent other with
            weight directed self --> other. We expect the outcome of
            the perception to be reflected at the time step.

        Args:
            self, other (obj): Agent object.
            perception (dict): perception details, attrs from a --> b
            time (float): time of perception

        Returns:
            dict: Returns new strength and liking factors.

        """

        strength = perception['strength']
        liking = perception['liking']
        displacement = perception['displacement']

        if other._id not in self.memory['perception']:
            self.memory['perception'][other._id] = []
            habituation = 0
        else:
            habituation = self.habituation('perception', other._id, time)
        excitation = strength * (1 - habituation) * dt * self.amp + self.current['arousal']

        if excitation > self.amp:
            self.current['arousal'] = self.amp
        else:
            self.current['arousal'] = excitation # cannot be above self.amp

        self.current['valence'] = 0 # TODO

        #: Update memory of perception with other id of agent
        self.memory['perception'][other._id].append({
            'time': time, # time of stimulus event
            'impact': strength, # impact/amount of feeling
        })

        return {
            'strength': strength,
            'liking': liking
        }

    def express(self, other, expression, time, dt):
        """Agent self expresses toward agent other with
            weight directed self --> other. We expect the the outcome of
            the expression to be reflected at the next time step.

        Args:
            self, other (obj): Agent object.
            expression (dict): expression details, attrs from a --> b
            time (float): time of expression

        Returns:
            float: Returns new weight.

        """

        strength = expression['strength']
        liking = expression['liking']
        displacement = expression['displacement']

        if other._id not in self.memory['expression']:
            self.memory['expression'][other._id] = []
            habituation = 0
        else:
            habituation = self.habituation('expression', other._id, time)
        excitation = strength * (1 - habituation) * dt * self.amp + self.current['arousal']

        if excitation > self.amp:
            self.current['arousal'] = self.amp
        else:
            self.current['arousal'] = excitation # cannot be above self.amp

        self.current['valence'] = 0 # TODO

        #: Update memory of perception with other id of agent
        self.memory['expression'][other._id].append({
            'time': time, # time of stimulus event
            'impact': strength, # impact/amount of feeling
        })

        return {
            'strength': strength,
            'liking': liking
        }

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
        self.data['arousal'][step + 1] = self.current['arousal']
        self.data['valence'][step + 1] = self.current['valence']

        #: set starting arousal and valence states for next step
            #: TODO these should be relative to stimulus and interactions conditionally
        decay = 1 / (1 + self.dec_rate * dt)
        self.current['arousal'] = decay * self.data['arousal'][step + 1]
        self.current['valence'] = self.data['valence'][step + 1]
