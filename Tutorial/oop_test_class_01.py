from turtle import *

class MyTurtle(Turtle):
    def __init__(self, speed=0, git chccolor="yellow"):
        Turtle.__init__(self, shape="turtle")
        self.speed(speed)
        self.color(color)

    def __str__(self):
        nm = input("Your Name? ")
        return "I will hypnotize you {}!".format(nm)

    def draw(self, r, a):
            self.range = r
            self.angle = a
            for x in range(self.range):
                self.forward(x)
                self.left(self.angle)
            done()

if __name__ == '__main__':

    reset()
    bgcolor("black")
    test = MyTurtle(0, "yellow")
    print(test)
    test.draw(500, 300)


