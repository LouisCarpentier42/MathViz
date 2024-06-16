
from turtle_graphics.TurtleGraphics import TurtleGraphics


class IncreasingAngleTurtleGraphics:

    def __init__(self, angle: float = 1.0, nb_iterations: int = 1000):
        self.angle = angle
        self.nb_iterations: int = nb_iterations
        self.turtle_graphics: TurtleGraphics = TurtleGraphics()

    def run(self):
        self.turtle_graphics.reset()
        xs, ys = [self.turtle_graphics.x], [self.turtle_graphics.y]
        current_angle = self.angle
        for i in range(self.nb_iterations):
            self.turtle_graphics.rotate(current_angle)
            self.turtle_graphics.step(1.0)
            xs.append(self.turtle_graphics.x)
            ys.append(self.turtle_graphics.y)

            current_angle += self.angle
            if current_angle > 360.0:
                current_angle -= 360.0

        return xs, ys


def main():
    turtle = IncreasingAngleTurtleGraphics(1.002, 10000)
    xs, ys = turtle.run()

    from turtle_graphics.visualize import visualize
    visualize(xs, ys)


if __name__ == '__main__':
    main()
