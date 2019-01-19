def googoo(x):
    for i in range(1, 10):
        print("{} X {} = {}".format(x, i, x * i))

googoo(9)
#

#
# def manyArgs(*args):
#     temp = 1
#     for i in args:
#         temp *= i
#     print(temp)
#
#
# manyArgs(2,2,2,10,1000)