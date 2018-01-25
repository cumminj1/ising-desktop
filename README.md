# ising-desktop

Lattice.py is a module with functions to create lattices and associated properties of an ising lattice, 
script1 is the script to call and run the ising simulations
medical is a module which modifies the ising simulation to model the spread of pathogenic diseases


this is a computational version of the ising model, applied first to an NxM lattice,
with information about the lattice collected; magnetisiation, mag susceptibility,
heat capacity, and total energy of the lattice. have collected graphs for each of these
quantities over a range of temperatures. Code is now to be adapted as a formal investiagtion
into a scientific topic, utilising the ising model as a tool.

The investigation centres upon the use of a heavily modified ising model with metropolis 
algorith to model the spread of pathogenic diseases as a function of both the virility of the disease
and the immunity of the population.

the disease is generalised and can be modified to vary the mortality rate of the disease in addition to
the recovery rate from illness  (death and recovery are controlled by independent functions)
