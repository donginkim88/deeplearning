from random import choice

start = 0
print("동인이가~~ 좋아하는~~ 베스킨 라빈스 떠리~~원!!!!!! (^오^)/   ")
while start < 31:
    p = int(input("나:  "))
    if (p > 3) or (p < 0):
        raise ValueError

    start += p
    if start >= 31:
        print("You lost! you drew {} and the current point is {}".format(p, start))
        break
    else:
        # print("You drew {} and the current point is {}".format(p, start))
        for i in range(start-p+1, start+1):
            print ("나: ", i, "!")
        c = choice(range(1,3))
        start += c
        if start >= 31:
            print("You won! computer drew {} and the current point is {}".format(c, start))
            break
        else:
            # print("computer drew {} and the current point is {}".format(c, start))
            for i in range(start - c + 1, start + 1):
                print ("컴퓨터: ",i, "!")
            pass
