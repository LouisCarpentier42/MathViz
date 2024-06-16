
import mpmath
from turtle_graphics.TurtleGraphics import TurtleGraphics
from decimal import Decimal, getcontext


class NumberTurtleGraphics:

    def __init__(self, number=(1,0), base: int = 10, nb_iterations: int = 1000):
        self.number = number
        self.base: int = base
        self.nb_iterations: int = nb_iterations
        self.turtle_graphics: TurtleGraphics = TurtleGraphics()

    def run(self):
        self.turtle_graphics.reset()
        xs, ys = [self.turtle_graphics.x], [self.turtle_graphics.y]
        for digit in self.get_digits_in_base():
            self.turtle_graphics.rotate(digit/self.base * 360)
            self.turtle_graphics.step(1.0)
            xs.append(self.turtle_graphics.x)
            ys.append(self.turtle_graphics.y)
        return xs, ys

    def get_digits_in_base(self):
        # Set the precision for the decimal module
        getcontext().prec = self.nb_iterations + 10

        # Convert the number to Decimal for high precision arithmetic
        if isinstance(self.number, tuple):
            number = Decimal(self.number[0]) / Decimal(self.number[1])
        else:
            mpmath.mp.dps = self.nb_iterations + 10
            if self.number == 'pi':
                number_str = str(mpmath.mp.pi)
            elif self.number == 'e':
                number_str = str(mpmath.mp.e)
            elif self.number == 'phi':
                number_str = str(mpmath.mp.phi)
            else:
                raise Exception('Invalid number given!')
            number = Decimal(number_str)

        # Separate the integer and fractional parts
        int_part = int(number)
        frac_part = number - int_part

        # Convert integer part to the given base
        int_digits = []
        while int_part > 0:
            int_digits.append(int_part % self.base)
            int_part //= self.base
        int_digits = int_digits[::-1] or [0]

        # Convert fractional part to the given base
        frac_digits = []
        while len(frac_digits) < self.nb_iterations - 1:
            frac_part *= self.base
            digit = int(frac_part)
            frac_digits.append(digit)
            frac_part -= digit

        # Combine integer and fractional parts
        return int_digits + frac_digits

def main():
    turtle = NumberTurtleGraphics('pi', 4, 10000)
    xs, ys = turtle.run()

    from turtle_graphics.visualize import visualize
    visualize(xs, ys)


if __name__ == '__main__':
    main()
