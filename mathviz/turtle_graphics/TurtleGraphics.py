
import math


class TurtleGraphics:

    def __init__(self, x: float = 0.0, y: float = 0.0, angle: float = 0.0):
        self.x: float = x
        self.initial_x: float = x
        self.y: float = y
        self.initial_y: float = y
        self.angle: float = angle
        self.initial_angle: float = angle

    def reset(self, x: float = None, y: float = None, angle: float = None) -> None:
        self.x = x or self.initial_x
        self.y = y or self.initial_y
        self.angle = angle or self.initial_angle

    def step(self, distance: float) -> None:
        self.x += distance * math.cos(self.angle)
        self.y += distance * math.sin(self.angle)

    def rotate(self, angle: float) -> None:
        self.angle += (angle*math.pi) / 180
