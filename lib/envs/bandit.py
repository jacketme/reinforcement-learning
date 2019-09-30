# coding='utf-8'

import numpy as np
from gym.envs.toy_text import discrete
from gym import Env, spaces


# class BanditEnv(discrete.DiscreteEnv):
#     metadata = {'render.modes': []}
#
#     def __init__(self, nA, value):
#         assert len(value) == nA, "value's length must equal nA"
#         nA = nA
#         nS = 1
#         self.nA_means = list(value)
#
#         P = {}
#         isd = np.ones(nS) / nS
#         super(BanditEnv, self).__init__(nS, nA, P, isd)
#
#     def _render(self, mode='human'):
#         pass
#
#     def step(self, a):
#         reward = round(self.np_random.randn(), 2) + self.nA_means[int(a)]
#         self.s = self.s
#         self.lastaction = a
#         return self.s, reward, False, {"prob": 1/self.nA}


class BanditEnv(Env):
    def __init__(self, nA, means):
        self.nA = nA
        self.means = means
        self.action_space = spaces.Discrete(nA)
        self.observation_space = spaces.Discrete(1)

    def reset(self):
        return None

    def step(self, a):
        reward = np.random.randn() + self.means[int(a)]
        return None, reward, False, " "

    def _render(self):
        pass
