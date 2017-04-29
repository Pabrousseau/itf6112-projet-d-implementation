# coding: utf-8
# !/usr/bin/env python
"""Cell"""
__author__ = "Pierre-Andre Brousseau"
__copyright__ = ""
__credits__ = [""]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Pierre-Andre Brousseau"
__email__ = "pabrousseau@videotron.ca"
__status__ = "In Progress"

# Package imports
from copy import copy, deepcopy
import os
import time
import sys


class Cell:
    def __init__(self, dna, state=0):
        self.dna_ = dna
        self.state_ = state
        self.sight_ = 0

    def get_state(self):
        return self.state_

    def set_state(self, state):
        self.state_ = state

    def set_sight(self, sight):
        self.sight_ = sight

    def move(self):
        move = self.dna_ >> ((255 - self.sight_) << 2) & 7
        return move
