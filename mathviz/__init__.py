
import os
import pathlib

import mathviz.turtle_graphics
import mathviz.random_moving_point

def run():
    os.system(f'streamlit run {pathlib.Path(__file__).parent}/MathViz.py')

def readme(module: str) -> str:
    with open(pathlib.Path(__file__).parent / module / 'README.md', 'r') as file:
        return file.read()

__all__ = [
    'run',
    'readme',
    'turtle_graphics',
    'random_moving_point'
]