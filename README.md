# ising-desktop

Lattice.py is a module with functions to create lattices and associated properties of an ising lattice, 
script1 is the script to call and run the ising simulations
medical is a module which modifies the ising simulation to model the spread of pathogenic diseases
medsctipt is a script which calls the medical module to run biological simulations


this is a computational version of the ising model, applied first to an NxM lattice,
with information about the lattice collected; magnetisiation, mag susceptibility,
heat capacity, and total energy of the lattice. have collected graphs for each of these
quantities over a range of temperatures. Code is now to be adapted as a formal investiagtion
into a scientific topic, utilising the ising model as a tool.

![alt text](https://github.com/cumminj1/ising-desktop/blob/master/isingmodeltemp.gif)

This gif shows how the ferromagnetic properties of a material change with temperature, especially given the phase change at a curie temperature = 2.4 for the purposes of this simulation

![alt text](https://github.com/cumminj1/ising-desktop/blob/master/FotoJet.png)

above we see the graphs of the observable quantities we examined in the course of this investigation, all as labelled in each graph

The investigation centres upon the use of a heavily modified ising model with metropolis 
algorith to model the spread of pathogenic diseases as a function of both the virility of the disease
and the immunity of the population.

the disease is generalised and can be modified to vary the mortality rate of the disease in addition to
the recovery rate from illness  (death and recovery are controlled by independent functions)

![alt text](https://github.com/cumminj1/ising-desktop/blob/master/non-fatal.gif)

This gif shows the spread of a disease with a 0% mortality rate throughout a population of 900 


![alt text](https://github.com/cumminj1/ising-desktop/blob/master/low-fatality.gif)

This gif shows the spread of a disease with a low mortality rate through the population

![alt text](https://github.com/cumminj1/ising-desktop/blob/master/mid-fatality.gif)

This gif shows the spread of a disease with a middling mortality rate through the population


![alt text](https://github.com/cumminj1/ising-desktop/blob/master/high-fatality.gif)

This gif shows the spread of a disease with a high mortality rate through the population


![alt text](https://github.com/cumminj1/ising-desktop/blob/master/medicine.png)

Above is a png of a population ravaged by a particularly virile, althought not very dangerous disease.
We take this to be a starting point for the application of antibiotics, which, assuming prompt distribution 
act extremely quickly since they do not have a dependence upon the state of the people they come into contact with.


![alt text](https://github.com/cumminj1/ising-desktop/blob/master/recovery.gif)

This gif shows the removal of infection with the treatment of antibiotics over time. Note
that the recovery does not depend on the nearest neighbours' state of infection/health, UNLIKE
the infection function
