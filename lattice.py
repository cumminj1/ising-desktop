#!/usr/bin/env python2

#program:		Ising model functions.
#author	:		Jack Cummins
#created:		4th Jan 2018
#last edited:		23th Jan 2018

from numpy import random
import numpy as np
from matplotlib import pyplot as plt
import math as math
#plt.switch_backend('TkAgg') 
plt.switch_backend('QT4Agg')
from pylab import cm
import matplotlib.animation as anim
import time

#first we're going to need to write code for a lattice


"""Need to include all the dependencies in the description. Current
working arguments:

N= 	no of x elements in the array
M=	no of y elements in the array
B=	the magnetic field applied to the lattice
T= 	the temperature applied to the lattice
J=	the exchange energy of interaction""" 	
#empty list to store energy values		

#class lattice:
#==============================================================================================		
#==============================initialisation==============================================
#==============================================================================================
"""stopped using a class based module for ease of use in the script.
	the use of a class can be seen in the version history"""

#==============================================================================================
#===========================intial matrix maker=============================================	
#==============================================================================================
	
def vanilla_lattice_make(N,M):                             #fucntion which makes lattice
	matrix=np.zeros((N,M))
	for i in range(0,N):
		for j in range (0,M):
			matrix[i,j]= random.choice([-1,1])
	return matrix

#==============================================================================================
#============================metropolois algorithm===============================================	
#============================================================================================== 
	
def metro_alg(N, M,steps, state_init, T, B, J, Kb):
	for i in range(0,steps):
		#choose the initial spin si
		#note that need to go 1 higher with randint
		
		#x_pos=np.random.randint(self.N+1)
		#y_pos=np.random.randint(self.M+1)
		x_pos=np.random.choice(N)
		y_pos=np.random.choice(M)
		si=state_init[x_pos,y_pos]

		#think about the effect of its nearest neigbours
		#add the modulus division as periodic boundary cond.
		nearest= (state_init[(x_pos+1)%N,y_pos]+ 
			state_init[(x_pos-1)%N,y_pos]+
			state_init[x_pos,(y_pos+1)%M]+
			state_init[x_pos,(y_pos-1)%M])

		#now need to try to flip the spin and
		#see how the energy changes
		dE= +2*si*B - 2*J*si*nearest

		#set the test conditions
	 	#print random.random()
		# if energy is less than 0
		#accetp the flip
		if dE >= 0:
			si *= -1
		#if energy is greater than 0
		#only accept the flip with a certain probability:
		elif random.random() < np.exp((1*dE)/(Kb*(T))):
			si *= -1

		else: 
			si*=1

		#else there is  no change but
		#this doesn't need to be specified.... or does it..?
		state_init[x_pos,y_pos]= si
			
		#adding a progress monitor to the loop, with overwrite in terminal
		print "Sweeps are " + str((100*float(i))/steps) + '% complete' + "\r" ,
		i=+1
	return state_init
	
#create a temperature array over which we check the magnetisation

#==============================================================================================	
#==========================================magnetisation=========================================
#==============================================================================================
	#here define the magnetisation as the sum of all spins, normalised, absolute
def magnetisation(N, M, matrix):
	print"Working on magnetisation..." + "\r" ,
	mags= abs(np.sum(matrix)/(N*M))
	return mags


#==============================================================================================	
#=================================magnetic succeptibility===================================	
#==============================================================================================

	#Mag supt is defined as X= [1/T][<M**2>-<M>**2]
def succeptibility(N, M, matrix, T):
	print"Working on susceptibility..." + "\r" ,
	mags= abs((np.sum(matrix*matrix))/(N*M))
	mags2= abs(np.sum((matrix)/(N*M))**2)
	suscept = (1/T)*(mags-mags2)
	return suscept


#==============================================================================================	
#====================================energy===================================================	
#==============================================================================================
	#creating a function to calculate the energy of a configuration
def En(N, M, J, matrix):
	print"Working on average energy..." + "\r" ,
	energy=0
	for i in range (N):
		for j in range (M):
				
			#renaming i,j sheerly for consistency and ease of reading
			x_pos=i
			y_pos=j

				#si is a spin state in the matrix
			si=matrix[x_pos,y_pos]
			
				#the boundary conditions w/ modulo
			nearest= (matrix[(x_pos+1)%N,y_pos]
				+ matrix[(x_pos-1)%N,y_pos]
				+matrix[x_pos,(y_pos+1)%M]
				+matrix[x_pos,(y_pos-1)%M])

				#update the energy from zero with each iteration
			energy += -si*nearest*0.5*J
		
		#making sure to normalise the energy to the array size
	return (energy)/(N*M)


#==============================================================================================	
#===================================Heat capacity==========================================	
#==============================================================================================	
#this should be fairly similar in application as magnetic susceptibility was
#(1/Kb*T)/T   *   [<E**2>-<E>**2]= C
def spec_heat(N, M, J, matrix, T, Kb):
	print"Working on specifit..." + "\r" ,
	energy=0
	energy2=0
	for i in range (N):
		for j in range (M):
			
			#renaming i,j sheerly for consistency and ease of reading
			x_pos=i
			y_pos=j

			#si is a spin state in the matrix
			si=matrix[x_pos,y_pos]
			
			#the boundary conditions w/ modulo
			nearest= (matrix[(x_pos+1)%N,y_pos]
				+ matrix[(x_pos-1)%N,y_pos]
				+matrix[x_pos,(y_pos+1)%M]
				+matrix[x_pos,(y_pos-1)%M])

				#update the energy from zero with each iteration
			energy  +=  (( +0.25*J*si*nearest))
			energy2 +=( + 0.25*J*si*nearest)
	E1=(energy**1)/(N*M)	
	E2= (((energy2)/(N*M))**2)
	#print ("The value of specific heat is equal to: " +str(E1-E2)+ "For a temperature of: " +str(T))
	#E2=(ising_model_lattice.En(self, matrix))**2
		
	spec= (+E1-E2)/(Kb*(T**2))
	#print (spec)
	return spec
			

"""#=======================================================================================================
		#printing the graph of the final state
		print("Now Plotting The Final state...                             ")
		plt.imshow(state_init, interpolation='none', cmap=plt.cm.get_cmap('bone', 2))
		plt.title("final state of " + str(N) + ' x ' + str(M) + " spin matrix, with " + str(sweeps) + " sweeps")					
		plt.colorbar(ticks=range(-1,2), label= 'Spin')
		plt.clim(-1,1)
		plt.show()	
================================================================"""

	



