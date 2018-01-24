#!/usr/bin/env python2
import numpy as np
import lattice as lt
	
#define our constants and variables
N=20
M=20
steps=10*N*M
sweeps= steps/(N*M)
Kb=1
T=1
B=0
J=1
temp_array=np.arange(0.1,5,0.05)	

#create the initial matrix
state_init=lt.lattice("state_init")
print state_init.vanilla_lattice_make()

	#calling all function for a specified lattice size
for T in (temp_array):
	matrix=lt.metro_alg(steps, state_init, T, B, J)

		#magnetisation
	mag_= lt.magnetisation(matrix)
		#print("the normalised magnetisation is equal to " + str(mag_) + " for Temperature= " + str(T))
	plt.plot(T, mag_, 'ro')

		#magnetic succeptibility
	succ= lt.succeptibility(matrix, T)
		#print("the mag susceptibility is equal to " + str(succ) + " for Temperature= " + str(T))
	plt.plot(T, succ, 'ro')

		#energy
	enerplot=lt.En(matrix)
	plt.plot(T, enerplot, 'ro')
	
		#heat cap
	spec111=lt.spec_heat(matrix)	
	plt.plot(T, spec111, 'ro')

	#printing the max values
	#create a temperature array over which we check the magnetisation
	
print("for a matrix of dimensions: " + str(N)+ " x " +str(M))
	#print("The critical temperature is equal to: " + str(where())
print("The max magnetisation is equal to: " + str(max(mag_)))
print("The max magnetic susceptibility is equal to: " + str(max(succ)))
print("The max energy value is equal to: " + str(max (enerplot)))
print("The max heat capacity is equal to: " + str(max(spec111)))


