# Research-Project

This project is part of the TU Delft Q4 CSE3000 Research Project of 2023 and acts as support for the research paper and project that was conducted in the 10 weeks that this project lasted. 

It implements a Reaction-Diffusion model in a Cellular Automata, in the form of a class called ReactionDiffusion, in orer to create Turing patterns. The class also includes a formula and calculation steps for the order parameter, which acts as an indicator of the segregation state of the world. 

Helper files are used, taken from the book [Think Complexity](https://www.dbooks.org/think-complexity-1492040207/):

Firstly, Cell2d.py holds a basic implementation of a Cellular Automata, with some methods like animate() or draw() which help in the steps and visualization of the Cellular Automata at any point of the simulations. It acts as a parent class for our implementation. 
The second file, utils.py, implements functionalities which are not directly related to the functionality of the Cellular Automata, with methods such as decorate() or set_palette(), which help in the customiation of the visualization; and three_frame(), an important method to our simulations since it is able to draw three different time steps next to each other from the same ReactionDiffusion class.

A ReactionDiffusion object is initialized with the following parameters:
-   [n]{.underline} is the length of the world. The Cellular Automata
    will be represented as a 2D array of size $n \cdot n$.

-   [$r_i$ and $r_o$]{.underline} are the kernel radii values, which
    indicate the number of neighbors that there will be when computing
    the next state.

-   [random]{.underline} is a Boolean value that expresses how the world
    will be initialized. If true, each cell in the world will be
    initialized to 0 or 1 with the attribute *probabilities* defining
    how likely the cell is to be each value. Else, an arbitrary patch of
    20\*20 cells will be set to 1 in a random position in the world,
    while the rest of the world is set to 0. The default value is set to
    True.

-   [static_neighbors]{.underline} is another Boolean value. If true
    (the default value), we will use four neighbors to calculate
    $\epsilon(t)$. Otherwise, we will use as many cells as there are
    inside the circle of radius $r_i$.

-   [probabilities]{.underline} only comes into play when *random* is set to True, and it is a floating point number that expresses the probability that the cells in the world are randomly initialized to 0. The probability that the cells are initialized to 1 is set as 1 - probabilities. Its default value is 0.5.


After implementing such a model, different evaluation methods and approaches are taken to verify that the model produces Turing patterns, as well as assert that the order parameter works as intended. Such evaluation methods are explained in depth and divided according to their contribution to the different parts of the project. A deeper overview of these methods is included in the notebook.
