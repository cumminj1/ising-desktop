#!/usr/bin/env python2

#program:		Ising model implementation.
#author	:		Jack Cummins
#created:		4th Jan 2018
#last edited:		16th Jan 2018

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

"""Define the lattice fucntions etc as a class to keep
everything organised and in the one place"""

"""Need to include all the dependencies in the description
of __init__ so anything below that has access to them. Current
working arguments:
N= 	no of x elements in the array
M=	no of y elements in the array
B=	the magnetic field applied to the lattice
T= 	the temperature applied to the lattice""" 
N=60
M=60
steps=800*N*M
sweeps= steps/(N*M)
Kb=1
T=1
B=1
J=1

	
#empty list to store energy values		

class ising_model_lattice:
#==============================================================================================		
#==============================initialisation==============================================
#==============================================================================================
	
	def __init__(self, N, M, B, T, Energy):                            #the init (says arguments etc)
		self.N=N
		self.M=M
		self.B=B
		self.T=T
		

#==============================================================================================
#===========================intial matrix maker=============================================	
#==============================================================================================
	
	def vanilla_lattice_make(N,M):                             #fucntion which makes lattice
		matrix=np.zeros((N,M))
		for i in range(0,N):
			for j in range (0,M):
				matrix[i,j]= random.choice([-1,1])
		return matrix
	
	state_init=vanilla_lattice_make(N,M)

#==============================================================================================
#============================metropolois algorithm===============================================	
#============================================================================================== 
	
	def metro_alg(steps, state_init, T, B, J):
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
			elif random.random() < np.exp((1*dE)/(Kb*T)):
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
	
	#state_final_check=metro_alg(steps, state_init, T, B, J)
	#plt.imshow(state_final_check)
	#plt.show()

#==============================================================================================	
#==========================================magnetisation=========================================
#==============================================================================================
	#here define the magnetisation as the sum of all spins, normalised, absolute
	def magnetisation(matrix):
		mags= abs(np.sum(matrix)/(N*M))
		return mags

	#create a temperature array over which we check the magnetisation
	temp_array=np.arange(0.1,4,0.25)	
	
	#create a for loop of temperature arrays so we can see how magnetisation 
	#changes as a function of temperature
	#for T in (temp_array):
	#	state_final=metro_alg(steps, state_init, T, B, J)
	#	mag_= magnetisation(state_final)
	#	print("the normalised magnetisation is equal to " + str(mag_) + " for Temperature= " + str(T))
	#	plt.plot(T, mag_, 'ro')
	
	#preparing the plot of magnetisation as a function of temperature
	#plt.xlabel('Temperature')
	#plt.ylabel("net magnetisation")
	#plt.title('magnetisation as function of temperature for an '+ str(N) + ' x ' + str(M) + ' matrix ')
	#plt.show()

#==============================================================================================	
#=================================magnetic succeptibility===================================	
#==============================================================================================

	#Mag supt is defined as X= [1/T][<M**2>-<M>**2]
	def succeptibility(matrix, T):
		mags= abs((np.sum(matrix*matrix))/(N*M))
		mags2= abs(np.sum((matrix)/(N*M))**2)
		suscept = (1/T)*(mags-mags2)
		return suscept

	for T in (temp_array):
		state_final=metro_alg(steps, state_init, T, B, J)
		succ= succeptibility(state_final, T)
		print("the mag susceptibility is equal to " + str(succ) + " for Temperature= " + str(T))
		plt.plot(T, succ, 'ro')
	#preparing the plot of mag suscept. as a function of temperature
	plt.xlabel('Temperature')
	plt.ylabel("mag suscept.")
	plt.title('mag suscept. as function of temperature for an '+ str(N) + ' x ' + str(M) + ' matrix ')
	plt.show()

"""#=======================================================================================================
		#printing the graph of the final state
		print("Now Plotting The Final state...                             ")
		plt.imshow(state_init, interpolation='none', cmap=plt.cm.get_cmap('bone', 2))
		plt.title("final state of " + str(N) + ' x ' + str(M) + " spin matrix, with " + str(sweeps) + " sweeps")					
		plt.colorbar(ticks=range(-1,2), label= 'Spin')
		plt.clim(-1,1)
		plt.show()	

	



#=========================================================================================

	#printing a graph of the initial matrix state
	tester= vanilla_lattice_make(N,M)
	#print(tester)
	plt.imshow(tester, interpolation='none', cmap=plt.cm.get_cmap('bone', 2))
	plt.title('Initial Spin Map for '+ str(N) + ' x ' +str(M) + ' matrix ')
	
	#discretising the colorbar to show spins
	plt.colorbar(ticks=range(-1,2), label='Spin')
	plt.clim(-1,1)

	plt.show()

	metrotest=metro_alg(steps, state_init, T, B, J)	#taken by cutpaste from the end	
	#plt.imshow(metrotest)
	plt.show()
#=========================================================================="""


	




