""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2016 Allen Downey
MIT License: http://opensource.org/licenses/MIT
"""

import numpy as np
import matplotlib.pyplot as plt

# Here's how animate works
# https://stackoverflow.com/questions/24816237/ipython-notebook-clear-cell-output-in-code
# https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.clear_output
    
from time import sleep
from IPython.display import clear_output

from utils import underride


class Cell2D:
    """Parent class for 2-D cellular automata."""

    def __init__(self, n, m=None):
        """Initializes the attributes.

        n: number of rows
        m: number of columns
        """
        m = n if m is None else m
        self.array = np.zeros((n, m), np.uint8)

    def add_cells(self, row, col, *strings):
        """Adds cells at the given location.

        row: top row index
        col: left col index
        strings: list of strings of 0s and 1s
        """
        for i, s in enumerate(strings):
            self.array[row+i, col:col+len(s)] = np.array([int(b) for b in s])

    def loop(self, iters=1):
        """Runs the given number of steps."""
        for i in range(iters):
            self.step()

    def draw(self, three_frame=False, **options):
        """Draws the array.
        """
        random_par = 'Random' if self.random else 'Segregated'
        neighbour_str = 'Four-neighbour' if self.static_neighbours else 'Dynamic-size'

        draw_array(self.array, **options)
        if not three_frame:
            plt.title(f'{self.n} by {self.n} model \n{random_par} initialization \n{neighbour_str} order parameter kernel \nInside radius: {self.r_i}, Outside radius: {self.r_o} \n\n Step {self.steps}')

    def animate(self, frames, interval=None, step=None):
        """Animate the automaton.
        
        frames: number of frames to draw
        interval: time between frames in seconds
        iters: number of steps between frames
        """
        random_par = 'Random' if self.random else 'Segregated'
        neighbour_str = 'Four-neighbour' if self.static_neighbours else 'Dynamic-size'

        if step is None:
            step = self.step
            
        plt.figure()
        try:
            for i in range(frames):
                self.draw()
                plt.title(f'{self.n} by {self.n} model \n{random_par} initialization \n{neighbour_str} order parameter kernel \nInside radius: {self.r_i}, Outside radius: {self.r_o} \n\nStep {self.steps}')
                
                perct = np.around(self.greens / (self.n**2) * 100, 2)
                plt.xlabel(f'Order parameter: {self.order_parameter}')
                
                plt.show()
                if interval:
                    sleep(interval)
                step()
                clear_output(wait=True)
            self.draw()
            plt.title(f'{self.n} by {self.n} model \n{random_par} initialization \n{neighbour_str} order parameter kernel \nInside radius: {self.r_i}, Outside radius: {self.r_o} \n\nStep {self.steps}')
            
            perct = np.around(self.greens / (self.n**2) * 100, 2)
            plt.xlabel(f'Order parameter: {self.order_parameter}')

            plt.show()
        except KeyboardInterrupt:
            pass
        

def draw_array(array, **options):
    """Draws the cells."""
    n, m = array.shape
    options = underride(options,
                        cmap='Greens',
                        alpha=0.7,
                        vmin=0, vmax=1, 
                        interpolation='none', 
                        origin='upper',
                        extent=[0, m, 0, n])

    plt.axis([0, m, 0, n])
    plt.xticks([])
    plt.yticks([])

    return plt.imshow(array, **options)
