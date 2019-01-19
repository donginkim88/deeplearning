#input

import time

input("hit return and count 20 sec")
start = time.time()  #returns unix time
input("again hit return after counting 20 sec")
end = time.time()
et = end - start

print("time taken:", et, "sec")
print("difference:", abs(et - 20), "sec")

