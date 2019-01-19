import random

n = random.randint(1, 30)

while True:
    x = input("take a guess: ")
    g = int(x)
    if g == n:
        print("correct!")
        break
    if g < n:
        print("too small!")
    if g > n:
        print("too big!")