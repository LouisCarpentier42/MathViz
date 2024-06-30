
import re
from typing import Dict
from mathviz.turtle_graphics.TurtleGraphics import TurtleGraphics


class SubstitutionTurtleGraphics:

    def __init__(self,
                 start: str = 'x',
                 substitutions: Dict[str, str] = None,
                 nb_substitutions: int = 5,
                 angle: float = 60):
        self.start: str = start
        self.substitutions: Dict[str, str] = substitutions or {
            'x': 'y + x + y',
            'y': 'x - y - x'
        }
        self.nb_substitutions: int = nb_substitutions
        self.angle: float = angle
        self.turtle_graphics: TurtleGraphics = TurtleGraphics()

    def run(self):
        self.turtle_graphics.reset()

        string = self.start
        for _ in range(self.nb_substitutions):
            pattern = re.compile("|".join(re.escape(key) for key in self.substitutions))
            string = pattern.sub(lambda m: self.substitutions[m.group(0)], string)

        xs, ys = [self.turtle_graphics.x], [self.turtle_graphics.y]
        self.turtle_graphics.step(1.0)
        xs.append(self.turtle_graphics.x)
        ys.append(self.turtle_graphics.y)
        for char in string:
            if char == '-':
                self.turtle_graphics.rotate(-self.angle)
                self.turtle_graphics.step(1.0)
                xs.append(self.turtle_graphics.x)
                ys.append(self.turtle_graphics.y)
            elif char == '+':
                self.turtle_graphics.rotate(self.angle)
                self.turtle_graphics.step(1.0)
                xs.append(self.turtle_graphics.x)
                ys.append(self.turtle_graphics.y)
        return xs, ys
