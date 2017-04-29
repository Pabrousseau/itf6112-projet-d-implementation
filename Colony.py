from __future__ import print_function

# coding: utf-8
# !/usr/bin/env python
"""Colony"""
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
import random
from Cell import Cell


class Colony:
    def __init__(self, dna=0, size=(15, 15), quantity=0):
        self.dna_ = dna
        self.size_ = size
        self.quantity_ = quantity
        self.cells_ = [[Cell(self.dna_) for i in range(self.size_[0])] for j in range(self.size_[1])]
        self.sights_ = [[0 for x in range(self.size_[0])] for y in range(self.size_[1])]

        for i in range(7):
            for j in range(7):
                self.cells_[2*i+1][2*j+1].set_state(1)

    def get_dna(self):
        return self.dna_

    def get_sight(self, x, y):
        if x == 0 and y == 0:
            i = 0
            i = int(int(int(i) << 1) + int(self.cells_[self.size_[0] - 1][self.size_[1] - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[self.size_[0] - 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[self.size_[0] - 1][y + 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][self.size_[1] - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][y + 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][self.size_[1] - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y + 1].get_state()))
            self.sights_[x][y] = copy(i)
        elif x == self.size_[0] - 1 and y == 0:
            i = 0
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][self.size_[1] - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y + 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][self.size_[1] - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][y + 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[0][self.size_[1] - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[0][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[0][y + 1].get_state()))
            self.sights_[x][y] = copy(i)
        elif x == 0 and y == self.size_[1] - 1:
            i = 0
            i = int(int(int(i) << 1) + int(self.cells_[self.size_[0] - 1][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[self.size_[0] - 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[self.size_[0] - 1][0].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][0].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][0].get_state()))
            self.sights_[x][y] = copy(i)
        elif x == self.size_[0] - 1 and y == self.size_[1] - 1:
            i = 0
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][0].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][0].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[0][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[0][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[0][0].get_state()))
            self.sights_[x][y] = copy(i)
        elif self.size_[0] - 1 > x > 0 == y:
            i = 0
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][self.size_[1] - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y + 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][self.size_[1] - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][y + 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][self.size_[1] - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y + 1].get_state()))
            self.sights_[x][y] = copy(i)
        elif x == self.size_[0] - 1 and 0 < y < self.size_[1] - 1:
            i = 0
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y + 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][y + 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[0][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[0][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[0][y + 1].get_state()))
            self.sights_[x][y] = copy(i)
        elif 0 == x < y < self.size_[1] - 1:
            i = 0
            i = int(int(int(i) << 1) + int(self.cells_[self.size_[0] - 1][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[self.size_[0] - 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[self.size_[0] - 1][y + 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][y + 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y + 1].get_state()))
            self.sights_[x][y] = copy(i)
        elif 0 < x < self.size_[0] - 1 and y == self.size_[1] - 1:
            i = 0
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][0].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][0].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][0].get_state()))
            self.sights_[x][y] = copy(i)
        else:
            i = 0
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x - 1][y + 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x][y + 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y - 1].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y].get_state()))
            i = int(int(int(i) << 1) + int(self.cells_[x + 1][y + 1].get_state()))
            self.sights_[x][y] = copy(i)
        return self.sights_

    def move_all(self):
        for x in range(self.size_[0]):
            for y in range(self.size_[1]):
                if self.cells_[x][y].get_state() == 1:
                    self.get_sight(x, y)
                    self.cells_[x][y].set_sight(self.sights_[x][y])
                    move = self.cells_[x][y].move()
                    if x == 0 and y == 0:
                        if move == 0:
                            pass
                        elif move == 1:
                            if self.cells_[self.size_[0] - 1][y].get_state() == 0:
                                self.cells_[self.size_[0] - 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 2:
                            if self.cells_[x + 1][y].get_state() == 0:
                                self.cells_[x + 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 3:
                            if self.cells_[x][self.size_[1] - 1].get_state() == 0:
                                self.cells_[x][self.size_[1] - 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 4:
                            if self.cells_[x][y + 1].get_state() == 0:
                                self.cells_[x][y + 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                    elif x == self.size_[0] - 1 and y == 0:
                        if move == 0:
                            pass
                        elif move == 1:
                            if self.cells_[x - 1][y].get_state() == 0:
                                self.cells_[x - 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 2:
                            if self.cells_[0][y].get_state() == 0:
                                self.cells_[0][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 3:
                            if self.cells_[x][self.size_[1] - 1].get_state() == 0:
                                self.cells_[x][self.size_[1] - 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 4:
                            if self.cells_[x][y + 1].get_state() == 0:
                                self.cells_[x][y + 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                    elif x == 0 and y == self.size_[1] - 1:
                        if move == 0:
                            pass
                        elif move == 1:
                            if self.cells_[self.size_[0] - 1][y].get_state() == 0:
                                self.cells_[self.size_[0] - 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 2:
                            if self.cells_[x + 1][y].get_state() == 0:
                                self.cells_[x + 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 3:
                            if self.cells_[x][y - 1].get_state() == 0:
                                self.cells_[x][y - 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 4:
                            if self.cells_[x][0].get_state() == 0:
                                self.cells_[x][0].set_state(1)
                                self.cells_[x][y].set_state(0)
                    elif x == self.size_[0] - 1 and y == self.size_[1] - 1:
                        if move == 0:
                            pass
                        elif move == 1:
                            if self.cells_[x - 1][y].get_state() == 0:
                                self.cells_[x - 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 2:
                            if self.cells_[0][y].get_state() == 0:
                                self.cells_[0][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 3:
                            if self.cells_[x][y - 1].get_state() == 0:
                                self.cells_[x][y - 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 4:
                            if self.cells_[x][0].get_state() == 0:
                                self.cells_[x][0].set_state(1)
                                self.cells_[x][y].set_state(0)
                    elif self.size_[0] - 1 > x > 0 == y:
                        if move == 0:
                            pass
                        elif move == 1:
                            if self.cells_[x - 1][y].get_state() == 0:
                                self.cells_[x - 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 2:
                            if self.cells_[x + 1][y].get_state() == 0:
                                self.cells_[x + 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 3:
                            if self.cells_[x][self.size_[1] - 1].get_state() == 0:
                                self.cells_[x][self.size_[1] - 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 4:
                            if self.cells_[x][y + 1].get_state() == 0:
                                self.cells_[x][y + 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                    elif x == self.size_[0] - 1 and 0 < y < self.size_[1] - 1:
                        if move == 0:
                            pass
                        elif move == 1:
                            if self.cells_[x - 1][y].get_state() == 0:
                                self.cells_[x - 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 2:
                            if self.cells_[0][y].get_state() == 0:
                                self.cells_[0][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 3:
                            if self.cells_[x][y - 1].get_state() == 0:
                                self.cells_[x][y - 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 4:
                            if self.cells_[x][y + 1].get_state() == 0:
                                self.cells_[x][y + 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                    elif 0 == x < y < self.size_[1] - 1:
                        if move == 0:
                            pass
                        elif move == 1:
                            if self.cells_[self.size_[0] - 1][y].get_state() == 0:
                                self.cells_[self.size_[0] - 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 2:
                            if self.cells_[x + 1][y].get_state() == 0:
                                self.cells_[x + 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 3:
                            if self.cells_[x][y - 1].get_state() == 0:
                                self.cells_[x][y - 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 4:
                            if self.cells_[x][y + 1].get_state() == 0:
                                self.cells_[x][y + 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                    elif 0 < x < self.size_[0] - 1 and y == self.size_[1] - 1:
                        if move == 0:
                            pass
                        elif move == 1:
                            if self.cells_[x - 1][y].get_state() == 0:
                                self.cells_[x - 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 2:
                            if self.cells_[x + 1][y].get_state() == 0:
                                self.cells_[x + 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 3:
                            if self.cells_[x][y - 1].get_state() == 0:
                                self.cells_[x][y - 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 4:
                            if self.cells_[x][0].get_state() == 0:
                                self.cells_[x][0].set_state(1)
                                self.cells_[x][y].set_state(0)
                    else:
                        if move == 0:
                            pass
                        elif move == 1:
                            if self.cells_[x - 1][y].get_state() == 0:
                                self.cells_[x - 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 2:
                            if self.cells_[x + 1][y].get_state() == 0:
                                self.cells_[x + 1][y].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 3:
                            if self.cells_[x][y - 1].get_state() == 0:
                                self.cells_[x][y - 1].set_state(1)
                                self.cells_[x][y].set_state(0)
                        elif move == 4:
                            if self.cells_[x][y + 1].get_state() == 0:
                                self.cells_[x][y + 1].set_state(1)
                                self.cells_[x][y].set_state(0)

    def simulate(self):
        for i in range(100):
            self.move_all()

    def get_states(self):
        s = []
        for x in range(self.size_[0]):
            for y in range(self.size_[1]):
                s.append(self.cells_[x][y].get_state())
        return s

    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for x in range(self.size_[0]):
            for y in range(self.size_[1]):
                if self.cells_[x][y].get_state() == 1:
                    print('X', end=" ")
                else:
                    print('.', end=" ")
            print()
