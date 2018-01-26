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


#the infection function is a heavily modified metropolis algorith with and extra set of conditions
#which allows people to die provided the virility is greater than the immunity and that the infected
#is below the normalised mortality rate.

def infection(N, M,time, state_init, immunity_rate, Virility, mortality_rate, time_upper):
	for i in range(0,time):
		#choose the initial spin si
		#note that need to go 1 higher with randint

		x_pos=np.random.choice(N)
		y_pos=np.random.choice(M)
		si=state_init[x_pos,y_pos]

		#think about the effect of its nearest neigbours
		#add the modulus division as periodic boundary cond.
		n1=state_init[(x_pos+1)%N,y_pos]
		n2=state_init[(x_pos-1)%N,y_pos]
		n3=state_init[x_pos,(y_pos+1)%M]
		n4=state_init[x_pos,(y_pos-1)%M]
	
		nearest= (n1+n2+n3+n4)
		#=============================================================================
		#=======================infection probability=================================
		#=============================================================================
		#now need to try to flip the spin and
		#see how the energy changes
		inf= immunity_rate -Virility

		#set the test conditions:

		#we need the immunity to be lower than the virility
		#we need at least 1 nearest neighbour to be ill
		#we need to prevent the dead from coming back to life
		if (inf <= 0 and nearest<4 and si != (-2) and (n1 or n2 or n3 or n4 == (-1))) :
			si = -1
		#otherwise the site will remain in good health (1)

		else: 
			si*=1
		#=========================================================================		
		#=======================death probability=================================
		#=========================================================================
		#create a random number between 0 and 1
		rand=random.random(1)
		print rand
		
		#if rand is below the normalised mortality rate the site dies
		if si == (-1) and (rand < float(mortality_rate/(0.25*time_upper))):
				si*=2
		else:
				si*=1
		#updating the site in the lattice of population
		state_init[x_pos,y_pos]= si
			
		#adding a progress monitor to the loop, with overwrite in terminal
		print "Sweeps are " + str((100*float(i))/time) + '% complete' + "\r" ,
		
		#iterate		
		i=+1
	
	#return the result
	return state_init



#we define the recovery function separately since the application of medicine to such 
#diseases is generally rolled out as a blanket solution ie. not incrementally
def recovery(N,M,steps,matrix, survival_rate):
	for i in range (0, steps):	
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

















