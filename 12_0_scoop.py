from os import system
from scoop import futures
import scoop

def square(n):
    print(__name__, scoop.worker, 'is working on', n)
    return n*n

if __name__ == '__main__':
    data = list(range(-10,10))
    parallel = futures.map(square, data)
    print(list(parallel))

