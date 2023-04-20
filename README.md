# Reduce plugin for PyMOL

This very simple extension of the PyMOL command line allows the usage of MolProbity's reduce tool from inside PyMOL for applications such as protein structure preparation for molecular docking. 

## Installation
Proven only on Linux systems. 
Download the reduce executable:

`wget https://github.com/rlabduke/MolProbity/tree/master/bin/linux/reduce`

and place in desired location. Then adapt the reduce.py file in this repo to reflect the correct location.
Now from PyMOL, install the plugin by simply selecting the updated reduce.py file. 

## Usage
Only exposes the command `reduce` to the PyMOL commandline:

`reduce obj1`

This will generate a .pdb file in your working directory of the input and generated reduce output. The output .pdb will be loaded in PyMOL as obj1_H.
