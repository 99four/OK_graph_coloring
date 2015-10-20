#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Damian'

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from bruteforce import *
import random as rnd

color_scheme = ['red', 'green', 'blue', 'yellow', 'darkviolet', 'orange', 'grey', 'aqua', 'olive' ]

class Graph:
    def __init__(self, size,original_matrix):
        self.matrix = original_matrix
        self.size = size

    def plot(self, coloring=None):
        G = nx.Graph(self.matrix)
        pos = nx.spring_layout(G)
        colors_to_use = coloring if coloring is not None else self.coloring
        nx.draw_networkx_nodes(G, pos, node_color=[color_scheme[x] for x in colors_to_use], node_size=1000,
                       alpha=0.7)
        labels={}
        for i in range(0, self.size):
            #letterASCII = ord('a') + i
            #character = chr(letterASCII)
            num = 0 + i
            labels[i] = r'$'+str(num)+'$'

        nx.draw_networkx_labels(G,pos,labels,font_size=16)
        nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.9, edge_color='g')
        plt.show()

    def fill(self,n, saturation):
        self.size = n
        p = n * (n - 1) * saturation
        self.matrix = np.zeros((n,n))
        while p > 0:
            x = rnd.randint(0, n - 1)
            y = rnd.randint(0, n - 1)

            self.matrix[x][y] = 1
            self.matrix[y][x] = 1
            p -= 1

    def add_edge(self, vA, vB):
        self.matrix[vA,vB] = 1
        self.matrix[vB,vA] = 1

    def return_neighbour(self, number):
        helper_list = []
        for i,n in enumerate(self.matrix[number]):
            if i == number:
                continue
            if n == 1:
                helper_list.append(i)
        return helper_list

    def check_if_correct(self, coloring):
        assert len(coloring) == self.matrix.shape[0]
        for v in range(0, self.matrix.shape[0]):
            neighbours = self.return_neighbour(v)
            for n in neighbours:
                if coloring[n] == coloring[v]:
                    return False
        self.coloring = coloring
        return True

n = 6
b = Bruteforce(n,5)

colorings = b.range()

myGraph = Graph(None, None)
myGraph.fill(n, .5)

def BruteForceAlgo(instance):
    generator = Bruteforce(digits=instance.size, bound=instance.size)
    colorings = generator.range()
    for c in colorings:
        #myGraph.plot(coloring=c)
        if instance.check_if_correct(c):
            #print ("znalazlem")
            #myGraph.plot()
            break


if __name__ == "__main__":
    print("dd")