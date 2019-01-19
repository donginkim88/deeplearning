import random
import time

def timed_operation():

    for i in range(3):
        x = random.randint(10, 99)
        y = random.randint(10, 99)

        print("{} + {}? ".format(x, y))
        t = time.time()
        z = input("input: ")
        if ((time.time()-t) > 10):
            print((time.time() - t))
            print("time out!")
        elif (int(z) == (x + y)):
            print("correct!")
        else:
            print(x + y)
            print("incorrect!")

timed_operation()