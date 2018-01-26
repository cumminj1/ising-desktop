#!/usr/bin/env python2
#!/usr/bin/env python2

#program:		Ising model implementation script.
#author	:		Jack Cummins
#created:		23th Jan 2018
#last edited:		25th Jan 2018

import numpy as np
import lattice as lt
import matplotlib.pyplot as plt
from matplotlib import rc
#define our constants and variables
N=60
M=60

steps=50*N*M
sweeps= steps/(N*M)
Kb=1
T=1
B=0
J=1
temp_array=np.arange(0.1,5,0.05)	
#================================================================================
#=======================Initial state  ==========================================
#================================================================================

#create the initial matrix
state_init=lt.vanilla_lattice_make(N,M)
plt.imshow(state_init, interpolation='none', cmap=plt.cm.get_cmap('bone', 2))
plt.colorbar(ticks=range(-1,2), label= 'Spin')
plt.title("Spin map of initial state\n for  " 
		+ str(N) + ' x ' +str(M) + "lattice.")
plt.show(block=True)
plt.pause(0)
plt.close()
#view the change of matrix with temperature

for T in (temp_array):
	evo=lt.metro_alg(N, M,steps, state_init, T, B, J, Kb)
	plt.imshow(evo, interpolation='none',cmap=plt.cm.get_cmap('bone', 2))
	plt.clim(-1,1)
	plt.colorbar(ticks=range(-1,2), label= 'Spin')
	plt.title("Spin map of final state\n for  " 
		+ str(N) + ' x ' +str(M) + "lattice.\n Temperature= " +str(T) )
	plt.savefig("temp_eq_"+str(T*10)+"_" + str(N*M)+".png", bbox_inches = 'tight')
	plt.close()
#================================================================================
#====================calculating the observables==========================================
#================================================================================

"""
#configure a plot for magnetisation:
fig1=plt.figure().add_subplot(111)
fig1.set_title("Magnetisation as a function of temperature \n for  " 
		+ str(N) + ' x ' +str(M) + "lattice. \n" + str(sweeps) + " sweeps" )
fig1.set_xlabel("Temperature (T)")
fig1.set_ylabel("Magnetisation (M)")

#configure a plot for mag susceptibility:
fig2=plt.figure().add_subplot(111)
fig2.set_title("Magnetic Susceptibility as a function of temperature  \n for  " 
		+ str(N) + ' x ' +str(M) + "lattice. \n" + str(sweeps) + " sweeps" )
fig2.set_xlabel("Temperature (T)")
fig2.set_ylabel("Magnetic Susceptibility (X)")

#configure a plot for the average energy:
fig3=plt.figure().add_subplot(111)
fig3.set_title("Average Energy as a function of temperature \n for  " 
		+ str(N) + ' x ' +str(M) + "lattice. \n" + str(sweeps) + " sweeps" )
fig3.set_xlabel("Temperature (T)")
fig3.set_ylabel("Average Energy (<E>)")

#configure a plot for the specific heat:
fig4=plt.figure().add_subplot(111)
fig4.set_title("Specific Heat as a function of temperature \n for  " 
		+ str(N) + ' x ' +str(M) + "lattice. \n" + str(sweeps) + " sweeps" )
fig4.set_xlabel("Temperature (T)")
fig4.set_ylabel("Specific heat (Cv)")

#================================================================================
#=======================Function calling=========================================
#================================================================================

#calling all function for a specified lattice size over a range of temperatures
for T in (temp_array):
	matrix=lt.metro_alg(N, M, steps, state_init, T, B, J, Kb)

	#magnetisation
	mag_= lt.magnetisation(N, M,matrix)
	#print("the normalised magnetisation is equal to " + str(mag_) + " for Temperature= " + str(T))
	fig1.plot(T, mag_, 'ro')	
	

	#magnetic succeptibility
	succ= lt.succeptibility(N, M,matrix, T)
	#print("the mag susceptibility is equal to " + str(succ) + " for Temperature= " + str(T))
	fig2.plot(T, succ, 'ro')	
	

	#energy
	enerplot=lt.En(N, M, J,matrix)
	fig3.plot(T, enerplot, 'ro')
	
	
	#heat cap
	spec111=lt.spec_heat(N, M, J, matrix, T, Kb)	
	fig4.plot(T, spec111, 'ro')
	
	
plt.show()
"""





	#printing the max values
	#create a temperature array over which we check the magnetisation
	
#print("for a matrix of dimensions: " + str(N)+ " x " +str(M))
#print("The max magnetisation is equal to: " + str(max(mag_)))
#print("The max magnetic susceptibility is equal to: " + str(max(succ)))
#print("The max energy value is equal to: " + str(max (enerplot)))
#print("The max heat capacity is equal to: " + str(max(spec111)))


