import numpy as np
import random

a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

array_sum = a + b

print("Array sum is", array_sum)


c = np.array([[1, 2, 3],
             [4, 5, 6]])

mult_result = c * 2

print("Mult result is", mult_result)

d = []


def rand_list(d):

    for i in range(10):
        ran_nums = random.randint(1, 10)
        d.append(ran_nums)
        print(d)


rand_list(d)

print(rand_list(d))

j = []


def myMax():
    f = print(rand_list(d))
    print(f.max())

mymax




