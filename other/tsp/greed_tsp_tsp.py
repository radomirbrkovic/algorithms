import random
from itertools import permutations

import matplotlib.pyplot as plt
from time import clock
from collections import Counter

aCity = complex


# Calculate total distance for salesman tour
def distanceTour(aTour):
    return sum(distancePoints(aTour[i -1], aTour[i]) for i in range(len(aTour)))


# Calculate absolute distance between tow cities
def distancePoints(first, second):
    return abs(first - second)

def generateCities(numberOfCities):
    seed = 111; width = 500; height = 300
    random.seed((numberOfCities, seed))
    return frozenset(aCity(random.randint(1, width), random.randint(1, height)) 
        for c in range(numberOfCities))

def greedyAlgorithm(cities, start=None):
    C = start or first(cities)
    tour = [C]
    unvisited = set(cities - {C})
    while unvisited:
        C = nearestNeighbor(C, unvisited)
        tour.append(C)
        unvisited.remove(C)

    return tour

def first(collection):
    return next(iter(collection))

def nearestNeighbor(A, cities):
    return min(cities, key=lambda C:distancePoints(C, A))           

def visualizeTour(tour, style='bo-'):
    if len(tour) > 1000:
        plt.figure(figsize=(15, 10))

    start = tour[0:1]
    visualizeSegment(tour + start, style)
    visualizeSegment(start, 'rD')

def visualizeSegment(segment, style = 'bo-'):
    plt.plot([X(c) for c in segment], [Y(c) for c in segment], style, clip_on=False)
    plt.axis('scaled')    
    plt.axis('off')

def X(city):
    "X axis"
    return city.real

def Y(city):
    "Y axis"
    return city.imag    


def run():
    cities = generateCities(2000)
    t0 = clock()
    tour = greedyAlgorithm(cities)
    t1 = clock()

    assert Counter(tour) == Counter(cities) # Every city apears exactly once in tour

    visualizeTour(tour)
    print ("greedyAlgorithm: 2000 cities => tour length {:.0f} (in {:.3f} sec)".format(distanceTour(tour), t1 - t0))

    plt.show()
run()    