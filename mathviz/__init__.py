
import os
import pathlib
import mathviz.turtle_graphics


def run():
    os.system(f'streamlit run {pathlib.Path(__file__).parent}/MathViz.py')

__all__ = [
    'run',
    'turtle_graphics'
]