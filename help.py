import random
import time
import numpy as np
N = 10**7

a = []
for _ in range(N):
    a.append(random.randint(1, N))

start = time.perf_counter()
a.sort()
end = time.perf_counter()
print(f"classic took {end-start}")

a = np.random.randint(1, N, N)
start = time.perf_counter()
a.sort()
end = time.perf_counter()
print(f"NumPy took {end-start}")