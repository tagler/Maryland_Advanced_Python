from scoop import futures
import scoop
import random

def pi(_):
    if random.random()**2 + random.random()**2 <= 1:
        return 1
    return 0

if __name__ == '__main__':
    samples = 10000
    parallel = futures.map_as_completed(pi, range(samples))
    print("Estimated Pi value is:", 4*sum(parallel)/samples)

