import random


def rand_numbers():

    sum_random_num = 0
    for i in range(10):
        randnums = random.randrange(10)
        sum_random_num = sum_random_num + randnums
        print("Random number is", randnums, end=" ")
        print("The sum is", sum_random_num)


rand_numbers()


print(rand_numbers)


def even_odd():
    a = int(input("enter any number"))
    if (a % 2) == 0:
        print("it's even")
    else:
        print("it's odd")


even_odd()

print(even_odd())
