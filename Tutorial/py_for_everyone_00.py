import turtle as t

# #cross
# for j in range(4):
#     t.pensize(3)
#     t.color("blue")
#     t.forward(100)
#     t.left(180)
#     t.forward(100)
#     t.right(90)
#
# #circles
# for i in range(4):
#     t.pensize(1)
#     t.color("yellow")
#     t.circle(50)
#     t.left(90)
# #bigger circle
# t.pensize(3)
# t.color("blue")
# t.left(90)
# t.forward(100)
# t.left(90)
# t.circle(100)

#Create a class
class MyTurtle:
    def __init__(self):
        import turtle as t
        t.reset()
        t.up()
        t.left(90)
        t.forward(300)
        t.left(90)
        t.forward(300)
        t.right(180)
        t.down()
        t.shape("turtle")

    def zigzag(self, times, size, color):
        for i in range(times):
            t.pensize(size)
            t.color(color)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.left(90)

if __name__ == '__main__':
    test = MyTurtle()
    test.zigzag(12, 5, "blue")

# t.reset()
# n = 50
# t.pensize(0.5)
# t.bgcolor("black")
# t.color("green")
# t.speed(0)
# for x in range(n):
#     t.circle(80)
#     t.left(360/n)
#
# class MyGeom():
#     def __init__(self, speed, background, color):
#         import turtle as t
#         self.speed = speed
#         self.bg = background
#         self.color = color
#     def draw(self, range, angle):
#         t.speed(self.speed)
#         t.
#         self.range = range
#         self.angle = angle
#         for x in range(range):
#             t.forward(x)
#             t.left(angle)
#
# t.reset()
# angle = 89
# t.bgcolor("black")
# t.color("purple")
# t.speed(0)
# for x in range(800):
#     t.forward(x)
#     t.left(angle)
#
# t.done()