# MathViz

Welcome to `MathViz`, a Python project designed to bring mathematical 
patterns to life through visualizations. Oftentimes, mathematics starts
from a simple set of rules. However, intricate patterns may arise by 
applying these rules. The goal of `MathViz` is to play around with these
rules and see the patterns that come to live!

## Installation

The latest version of `MathViz` can be pip-installed using the url to 
the GitHub repository:
```bash
pip install https://github.com/LouisCarpentier42/MathViz
```
`MathViz` was developed using Python 3.11, but it should also work for 
other Python versions, as long as the dependencies in [requirements.txt](requirements.txt)
can be installed. 

## Usage

Once you installed `MathViz`, you only need the following code to start the application:

```python
import mathviz
mathviz.run()
```

## Current features

1. [Turtle graphics](mathviz/turtle_graphics/README.md). We let a turtle walk around 
   according to a simple set of rules. By adding a pen to the turtle, we can visualize
   his path! 
2. [Random moving point](mathviz/random_moving_point/README.md). We have a set of points
   in a 2D plane. We also have one special point, that randomly moves towards one of the
   other points. Where will the point be located? 
3. More features will be added in the future! 

## Contributing

Contributions are welcome! If you have a new visualization idea or 
improvements for existing ones, feel free to open an issue or submit 
a pull request. Let's work together to expand the mathematical MathViz.

## License

    MIT License
    
    Copyright (c) 2024 Louis Carpentier
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.