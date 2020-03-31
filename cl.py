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
      

class Square(Polygon):
    def __init__(self, size, color="black"):
        super().__init__(4, "square", size, color)

    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()

square = Square(size=100)

square.draw()

turtle.done()