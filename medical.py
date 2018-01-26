#!/usr/bin/env python2

#program:		Ising model medical.
#author	:		Jack Cummins
#created:		25th Jan 2018
#last edited:		25th Jan 2018

"""the aim here is to create a modified version of some
ising model functions such that it can be used to model
the spread of pathogenic diseases under and outside the 
effects of herd immunisation"""

"""So we will use the same -1,1 matrix, iniitialised 
to (1+) but want to amend it such that
a second metropolis algorithm will take any (-1) values
which arise and change them to 2 with a given probability
+1	= healthy
-1	= infected
-2	= dead
"""

""""we will also increase the number of nearest numbers to 8 to 
approximate the frequency of inter-population contact more 
frequently"""

#vir is the virility of the disease from 0-1
#B is the immunity
#Mort=mortality rate
#basic metropolis to apply inital infirmment
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

N=30
M=30
steps=8000
immunity_rate=10001.#herd immunity
Virility=1000.0		#disease virility
T=50
J=1
Kb=1
mort_r=20.0	#mortality rate in percent
surv_r=50.       #the survivabiliity rate
def healthy_population(N,M):
	matrix=np.ones((N,M))
	return matrix

#health=healthy_population(N,M)
#plt.imshow(health)
#plt.colorbar()
#plt.ion()
#plt.show()

def infection_seed(N,M, matrix):
		#x_pos=np.random.choice(N)
  		#y_pos=np.random.choice(M)
		x_pos=N/2
		y_pos=M/2
		matrix[x_pos, y_pos]*=(-1)
		
		return matrix

#seed_population= infection_seed(N, M, health)
#plt.imshow(seed_population)
#plt.show()
def infection(N, M,steps, state_init, immunity_rate, Virility):
	for i in range(0,steps):
		#choose the initial spin si
		#note that need to go 1 higher with randint

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
		inf= immunity_rate -Virility
		#inf=(immunity_rate-Virility)*nearest
		#print(inf)
		#set the test conditions
	 	#print random.random()
		# if energy is less than 0
		#accetp the flip
		if inf <= 0 and nearest < 4:
			si = -1
		#if energy is greater than 0
		#only accept the flip with a certain probability:
		
		#the probability of being an independednt contractor of the disease				
		#elif random.random() < float(Virility/100.):
		#	si *= -1

		else: 
			si*=1

		#else there is  no change but
		#this doesn't need to be specified.... or does it..?
		state_init[x_pos,y_pos]= si
			
		#adding a progress monitor to the loop, with overwrite in terminal
		print "Sweeps are " + str((100*float(i))/steps) + '% complete' + "\r" ,
		i=+1
	return state_init
	


#check= infection(N,M, steps, seed_population, immunity_rate, Virility)
#plt.imshow(check, interpolation='none',cmap=plt.cm.get_cmap('RdYlGn', 2))
#plt.colorbar(ticks=range(-1,2), label= 'Healthy and Infected')

#plt.ion()
#plt.show()


#death is a function that affects the infected population 
#depending on a randomised number. If this number falls below
# the oserved mortality rate of the disease
def death(N,M,steps,matrix, mortality_rate):
	for i in range (steps):	
		x_pos=np.random.choice(N)
		y_pos=np.random.choice(M)
		si=matrix[x_pos,y_pos]
		rand=random.random()
		print rand
		#print si
		#print float(mortality_rate/100.)
		if si == (-1) and (rand < float(mortality_rate/100.0)):
				si*=2
		else:
				si*=1
		#now here i should add in a bit such that people can recover.
		#thats not fun		
		matrix[x_pos,y_pos]= si
		i+=1
	return matrix
#death_check= death(N,M,steps, check, mort_r)
#plt.imshow(death_check, interpolation='none', cmap=plt.get_cmap('RdYlGn',4))
#plt.colorbar(ticks=range(-4,3), label= 'Healthy and Infected')
#plt.title("The spread of disease related death in a population")
#plt.ion()
#plt.show()

def recovery(N,M,steps,matrix, survival_rate):
	for i in range (steps):	
		x_pos=np.random.choice(N)
		y_pos=np.random.choice(M)
		si=matrix[x_pos,y_pos]
		rand=random.random()
		print rand
  
		if si==(-1) and (rand< float(survival_rate/100)):
				si*=-1
              
		else:
				si*=1
		matrix[x_pos,y_pos]=si
		i+=1
	return matrix
 

"""recovtest= recovery(N,M, steps, check, surv_r)
plt.imshow(recovtest, interpolation='none')
plt.colorbar()
plt.show()
"""

















