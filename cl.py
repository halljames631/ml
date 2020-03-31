import turtle

class Polygon:
    def __init__(self, sides, name, size=100, color="black"):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides

    def draw(self):
        turtle.color(self.color)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)
        turtle.done()


stop = Polygon(size=50, sides=8, name='stop sign', color='red')
stop.draw()