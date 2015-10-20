#!/usr/bin/env python
# -*- coding: utf-8 -*-
from graph import Graph, BruteForceAlgo
from time import clock
import numpy as np
import matplotlib.pyplot as plt
__author__ = 'Damian'

class Benchmark:
    def __init__(self, repeats, instances):
        self.repeats = repeats
        self.instances = instances
        self.times = np.zeros((len(instances), repeats))

    def Profile(self):
        for i, (n, saturation) in enumerate(self.instances):
            print(n)
            for repeat in range(self.repeats):
                instance = Graph(None,None)
                instance.fill(n, saturation)
                start = clock()
                BruteForceAlgo(instance)
                stop = clock()
                self.times[i, repeat] = stop - start


b = Benchmark(3, [[3, .7],
                   [4, .7],
                   [5, .7],
                   [6, .7],
                   [7, .7]
                   ])
b.Profile()
results = b.times
np.save('dd', results)

y = np.mean(results, axis=1)
x = [3,4,5,6,7]

plt.plot(x, y)
plt.show()

print(results)



