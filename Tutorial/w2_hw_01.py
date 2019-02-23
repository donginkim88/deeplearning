def operation():
    while True:
        f = int(input("What is the first number? "))
        if f < 0:
            raise ValueError

        s = int(input("What is the second number? "))
        if s < 0:
            raise ValueError

        q1 = int(input("{} + {}: ".format(f, s)))

        if q1 == (f+s):
            q2 = int(input("{} - {}: ".format(f, s)))
            if q2 == (f-s):
                q3 = int(input("{} * {}: ".format(f, s)))
                if q3 == (f*s):
                    q4 = float(input("{} / {}: ".format(f, s)))
                    if q4 == (f/s):
                        print("You got it!")
                        break
                    else:
                        raise ValueError
                else:
                    raise ValueError
            else:
                raise ValueError
        else:
            raise ValueError

operation()


