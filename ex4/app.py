#!/usr/bin/env python3
# example of single threaded matrix multiplication
from os import environ
from time import time
import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 8000

if len(sys.argv) > 2:
    environ['OMP_NUM_THREADS'] = sys.argv[2]
else:
    environ['OMP_NUM_THREADS'] = '1'
from numpy.random import rand

# record the start time
start = time()
# size of arrays

# create an array of random values
data1 = rand(n, n)
data2 = rand(n, n)
# matrix multiplication
result = data1.dot(data2)
# calculate and report duration
duration = time() - start
print(f'Took {duration:.3f} seconds for array size {n} with {environ["OMP_NUM_THREADS"]} threads.')
