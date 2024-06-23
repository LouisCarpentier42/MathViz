# Turtle Graphics

Imagine a turtle walking around on an infinitely large plane. The 
turtle has two possible options:
1. Move forward a certain distance.
2. Rotate a certain angle.

Now imagine the turtle is holding a pen, such that we can follow its
tracks. 

> This visualization - and in fact this entire project - was inspired by 
> Matt Henderson, who showed this principle in a [video](https://youtu.be/tkC1HHuuk7c?si=Vq04vwa7FscY7ZMp) 
> on Numberphile.

## Rule sets

It is possible to manually control a turtle, which allows to draw any line
of connected, straight segments. Alternatively, it is possible to use some 
rule set to define how the turtle moves. The idea is that, by only giving
a small set of rules, the turtle can still create very interesting patterns. 
Several rule sets were implemented in this project. These are briefly described
below.

### Increasing angle

The turtle will iteratively step forward a distance of 1, and then rotate
a specific angle. Given some starting angle $\alpha$. The first rotation will
be $\alpha$, the second rotation will be $2\cdot\alpha$, the third rotation will
be $3\cdot\alpha$, and so on. Generally speaking, the rotation $i$ will have 
an angle of $i\cdot\alpha$. By slightly changing the starting angle, the final
path of the turtle will dramatically change! 

### Substitution based

Given some initial string, and a dictionary of substitutions. Each occurrence of 
a dictionary-key in the string will be replaced by its corresponding value to create
a new string. This process can be repeated a few times. Say for example that we start
from the string `"x"` and have the following substitution dictionary:
```json
{
    "x": "y + x + y", 
    "y": "x - y - x"
}
```

If we apply 1 substitution, we obtain the string `"y + x + y"` (the first item in
the substitution dictionary). In the next iteration, we replace each `"x"` by `"y + x + y"`
and each `"y"` by `"x - y - x"`. Thus, for the second iteration we obtain the string
`"(x - y - x) + (y + x + y) + (x - y - x)"`. Note that the brackets should technically
not be included, but are only added to make this process clear. The original two `"+"`
symbols in the string remain. By following this procedure, we get the following 
sequence of strings:
1. `"x"`
2. `"y + x + y"`
3. `"x - y - x + y + x + y + x - y - x"`
4. `"y + x + y - x - y - x - y + x + y + x - y - x + y + x + y + x - y - x + x - y - x + y + x + y - x - y - x - x - y - x"`
5. ...

The resulting string after some number of iterations can be used to move the turtle around. 
The turtle will read over the string and apply some action for certain symbols. Given a 
fixed angle $\alpha$. If the turtle reads a `"+"`, then it will step a distance of 1 and 
rotate with an angle of $\alpha$. If the turtle reads a `"-"`, then it will step a 
distance of 1 and rotate with an angle of $-\alpha$ (notice the minus sign). Try this out
and see what path the turtle follows! 

### Follow the number

Given the decimal expansion of some number, for example $\frac{1}{7}$ or $\pi$. The turtle
reads the numbers of the decimal expansion, and moves accordingly. For each number it sees, 
it will first make a step of distance 1, and then rotates according to the value of the number. 
Specifically, if the turtle reads the number $i$, then it rotates $\frac{i}{10}$ of a circle. 
For example if it reads the number '4', it will rotate 4 tenths of a full circle, or 144°
(because a circle is 360°). 

Notice that this path is fixed, but only for a given base! Above we used the standard 
decimal values, but we can also look in other bases, such as binary or octal. In this 
case, instead of dividing the number by 10, the turtle will divide the number by the 
base we are working in. For example, for base 2 or binary, the turtle will rotate an
angle of 0° if it encounters an '0', and it will rotate 180° if it sees a '1'. This 
means that the path of a turtle in binary would be a straight line, which is quiet 
boring. However, for other bases, some interesting patterns may present themselves! 
