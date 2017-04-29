# coding: utf-8
# !/usr/bin/env python
"""Genetic Algorithm"""
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
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime
import sys
import random
from Colony import Colony

TARGET = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
          0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
          0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
          0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
          0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
          0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
          0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def show(target):
    os.system('cls' if os.name == 'nt' else 'clear')
    for x in range(15):
        for y in range(15):
            if target[x*15+y] == 1:
                print('X', end=" ")
            else:
                print('.', end=" ")
        print()

def gen_rand_dna():
    x = 0
    for i in range(256):
        x = int(int(int(x) << 4) + int(random.randint(0, 4)))
    return x


def fitness(colony):
    n = 0
    for i in range(225):
        if colony[i] == TARGET[i]:
            n += 1
    return n*n*n*n*n*n*n*n/1000000000000000


def crossover(p1, p2):
    cross_dna = []
    choices = [0, 0]
    for i in range(256):
        choices[0] = p1 >> ((255 - i) << 2) & 7
        choices[1] = p2 >> ((255 - i) << 2) & 7
        cross_dna.append(np.random.choice(choices, 1))
    return cross_dna


def mutate(dna, p=0.05):
    for i in range(256):
        if random.uniform(0, 1) < p:
            dna[i] = random.randint(0, 4)
    x = 0
    for i in range(256):
        x = int(int(int(x) << 4) + int(dna[i]))
    return x


class GeneticEvolution:
    def __init__(self):
        self.mean_scores_ = []
        self.pop_ = []
        self.scores_ = np.array([0 for x in range(100)])
        self.dna_pool_ = [0 for x in range(100)]

        for i in range(100):
            self.pop_.append(Colony(dna=gen_rand_dna(), size=(15, 15), quantity=49))
        for i in range(100):
            self.dna_pool_[i] = self.pop_[i].get_dna()

    def population(self):
        self.pop_ = []
        for i in range(100):
            self.pop_.append(Colony(dna=self.dna_pool_[i], size=(15, 15), quantity=49))

    def selection(self):
        for i in range(100):
            self.pop_[i].simulate()
            self.scores_[i] = fitness(self.pop_[i].get_states())

        self.pop_[np.argmax(self.scores_)].show()
        self.mean_scores_.append(np.mean(self.scores_, dtype=np.float64))
        print()
        print(np.min(self.scores_))
        print(np.mean(self.scores_, dtype=np.float64))
        print(np.max(self.scores_))
        print()
        self.scores_ = self.scores_ / np.sum(self.scores_)

    def reproduction(self):
        new_pool = []
        new_pool.append(self.dna_pool_[np.argmax(self.scores_)])
        for i in range(99):
            p1 = np.random.choice(self.dna_pool_, 1, p=self.scores_)[0]
            p2 = np.random.choice(self.dna_pool_, 1, p=self.scores_)[0]
            cross_dna = crossover(p1, p2)
            new_pool.append(mutate(cross_dna))

        self.dna_pool_ = copy(new_pool)

    def get_mean_scores(self):
        return self.mean_scores_


def main():
    begin = datetime.datetime.now()
    G = GeneticEvolution()
    for i in range(100):
        G.selection()
        G.reproduction()
        G.population()

    plt.interactive(False)
    plt.figure()
    plt.plot(G.get_mean_scores())
    plt.savefig('img.png')
    print(datetime.datetime.now() - begin)

if __name__ == '__main__':
    #show(TARGET)
    main()

