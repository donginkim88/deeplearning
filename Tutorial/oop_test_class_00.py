from turtle import *

class MyTurtle(Turtle):
    def __init__(self, speed=0, color="yellow"):
        Turtle.__init__(self, shape="turtle")
        self.speed(speed)
        self.color(color)

    def draw(self, r, a):
            self.range = r
            self.angle = a
            for x in range(self.range):
                self.forward(x)
                self.left(self.angle)
            done()

if __name__ == '__main__':
    nm = input("Your Name? ")
    print("I will hypnotize you {}!".format(nm))
    reset()
    bgcolor("black")
    test = MyTurtle(0, "yellow")
    test.draw(500, 300)


