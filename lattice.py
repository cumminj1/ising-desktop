#!/usr/bin/env python

#program:		Ising model implementation.
#author	:		Jack Cummins
#created:		4th Jan 2018
#last edited:		8th Jan 2018

from numpy import random
import numpy as np
from matplotlib import pyplot as plt
import math 
#from pylab import cm


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
N=25
M=25
step= 50
Kb=1.3e-23
T=1.5
B=0

class ising_model_lattice:

	def __init__(self, N, M, B, T):                            #the init (says arguments etc)
		self.N=N
		self.M=M
		self.B=B
		self.T=T

	def vanilla_lattice_make(N,M):                             #fucntion which makes lattice
		matrix=np.zeros((N,M))
		for i in range(0,N):
			for j in range (0,M):
				matrix[i,j]= random.choice([-1,1])
		return matrix
	state_init=vanilla_lattice_make(N,M)
	#def Energy_check(self, xpos, ypos):                        #check energy of one state
            
 	 
    	def metro_alg(self, state_init):                                 #metropolis algorithm function
             #for i in range(N):
              #   for j in range(M):
                     
                     #choose the initial spin si
                     #note that need to go 1 higher with randint
                     x_pos=np.random.randint(self.N+1)
                     y_pos=np.random.randint(self.M+1)
                     si=state_init[x_pos,y_pos]
                     
                     #think about the effect of its nearest neigbours
                     nearest= (state_init[x_pos+1,y_pos]+ 
                              state_init[x_pos-1,y_pos]+
                              state_init[x_pos,y_pos+1]+
                              state_init[x_pos,y_pos-1])
                     
                     #now need to try to flip the spin and
                     #see how the energy changes
                     dE= 2*si*nearest
                     
                     #set the test conditions
                     
                     # if energy is less than 0
                     #accetp the flip
                     if dE <= 0:
                         si *= -1
                     
                    #if energy is greater than 0
                    #only accept the flip with a certain probability:
                     elif random() < math.exp(dE/Kb*T):
                        si *= -1
                        
                    #else there is  no change but
                    #this doesn't need to be specified.
                     state_init[x_pos,y_pos]= si
                
                
 
	tester= vanilla_lattice_make(N,M)
	print(tester)
	#cmap= cm.get_cmap('RGB', 3)
	plt.imshow(vanilla_lattice_make(N,M), interpolation='none')
	plt.title('Spin Map')

	plt.colorbar()

	plt.show()
		
