
import random
from typing import List, Tuple

class RandomMovingPoint:

    def __init__(self, points: List[Tuple[float, float]], start_x: float, start_y: float, alpha: float):
        self.points: List[Tuple[float, float]] = points
        self.start_x: float = start_x
        self.current_x: float = start_x
        self.start_y: float = start_y
        self.current_y: float = start_y
        self.alpha: float = alpha

    def step(self) -> Tuple[float, float]:
        selected_point = random.choice(self.points)
        self.current_x = self.alpha * selected_point[0] + (1 - self.alpha) * self.current_x
        self.current_y = self.alpha * selected_point[1] + (1 - self.alpha) * self.current_y
        return self.current_x, self.current_y

    def n_steps(self, n: int) -> List[Tuple[float, float]]:
        return [self.step() for _ in range(n)]
