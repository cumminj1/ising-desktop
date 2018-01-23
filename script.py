#!/usr/bin/env python2

from lattice import ising_model_lattice as lt
	
temp_array=np.arange(0.1,5,0.05)	
	#calling all function for a specified lattice size
for T in (temp_array):
	matrix=metro_alg(steps, state_init, T, B, J)

		#magnetisation
	mag_= magnetisation(matrix)
		#print("the normalised magnetisation is equal to " + str(mag_) + " for Temperature= " + str(T))
	plt.plot(T, mag_, 'ro')

		#magnetic succeptibility
	succ= succeptibility(matrix, T)
		#print("the mag susceptibility is equal to " + str(succ) + " for Temperature= " + str(T))
	plt.plot(T, succ, 'ro')

		#energy
	enerplot=En(matrix)
	plt.plot(T, enerplot, 'ro')
	
		#heat cap
	spec111=spec_heat(matrix)	
	plt.plot(T, spec111, 'ro')

	#printing the max values
	#create a temperature array over which we check the magnetisation
	
print("for a matrix of dimensions: " + str(N)+ " x " +str(M))
	#print("The critical temperature is equal to: " + str(where())
print("The max magnetisation is equal to: " + str(max(mag_)))
print("The max magnetic susceptibility is equal to: " + str(max(succ)))
print("The max energy value is equal to: " + str(max (enerplot)))
print("The max heat capacity is equal to: " + str(max(spec111)))
