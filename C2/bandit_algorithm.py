# coding='utf-8'

import numpy as np
import sys
if "../" not in sys.path:
  sys.path.append("../")
from lib.envs.bandit import BanditEnv


arms_mean = [1.0, 0.8, 0.5, 1.3, 1.55, 1.2, 1.1, 1.4, 0.9, 1.23]
env = BanditEnv(10, arms_mean)
# def bandit_algorithm(nA=10, value):
#     """
#
#     :param nA:
#     :param value:
#     :return:
#     """
#     q = np.zeros(nA)
