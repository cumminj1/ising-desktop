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
N=100
M=100
steps=100*N*M
sweeps= steps/(N*M)
Kb=1
T=1
B=0
J=1

	
#empty list to store energy values		

class ising_model_lattice:
		
#=======================================================================================
	def __init__(self, N, M, B, T, Energy):                            #the init (says arguments etc)
		self.N=N
		self.M=M
		self.B=B
		self.T=T
		self.Energy=Energy

#=======================================================================================	

	def vanilla_lattice_make(N,M):                             #fucntion which makes lattice
		matrix=np.zeros((N,M))
		for i in range(0,N):
			for j in range (0,M):
				matrix[i,j]= random.choice([-1,1])
		return matrix
	
	state_init=vanilla_lattice_make(N,M)
#======================================================================================	 
	"""def metro_alg(steps, state_init, T, B, J):
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
			i=+1"""
#====================================================================================================		
	def energy(steps, state_init, T, B, J):
		#the energy of 1 flip is as above
		for i in range (0,N):
			for j in range (0,M):			
			
				totalE=[]

				x_pos=i
				y_pos=j
				si=state_init[x_pos,y_pos]

				#think about the effect of its nearest neigbours
				#add the modulus division as periodic boundary cond.
				nearest= (state_init[(x_pos+1)%N,y_pos]+ 
					state_init[(x_pos-1)%N,y_pos]+
					state_init[x_pos,(y_pos+1)%M]+
					state_init[x_pos,(y_pos-1)%M])
				solo_energy= si*B - J*si*nearest
				totalE.append(solo_energy)
		E=sum(totalE)/(N*M)
		print E
		print(totalE[0])
	enertest=energy(steps, state_init, T, B, J)
	print(enertest)
	
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

	metrotest=metro_alg(steps, state_init, T, B, J)
	#plt.imshow(metrotest)
	plt.show()
#==========================================================================
"""
	
	




