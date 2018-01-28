#!/usr/bin/env python2

#program:		script to implement the pathogenic spread of disease
#			as predicted by the ising model
#author	:		Jack Cummins
#created:		26th Jan 2018
#last edited:		26th Jan 2018

import medical as med
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
#==========================================================================================
#=============================constants/variable===========================================
#==========================================================================================

N=30		#matrix x size
M=30		#matrix y size
time=10000	#time evaluated over
immunity_rate=99#herd immunity
Virility=100	#disease virility
mort_r= 10.	#mortality rate in percent
surv_r=1.	#effectiveness of medicine 

#==========================================================================================
#==========================healthy =========================================================
#==========================================================================================


#create a plot of the healthy population
health=med.healthy_population(N,M)
plt.imshow(health,interpolation='none', cmap=plt.get_cmap('RdYlGn',4))

plt.title("a healthy population"+" \n Immunity= "+ str(immunity_rate) + 
	 "\n Virility= " + str(Virility) + " \n mortality rate= "+str(mort_r) +
	 "\n recovery rate= " + str(surv_r))

#we set the colorbar to be normalised from one plot to another
plt.clim(-2,1)
plt.colorbar(ticks=range(-3,3), label= 'Healthy and Infected')

#show
plt.show()

#==========================================================================================
#===========================seed infection=================================================
#==========================================================================================

#creat a plot of an infection seeded population (1 infection)
infection_seed=med.infection_seed(N,M, health)

plt.imshow(infection_seed,interpolation='none', cmap=plt.get_cmap('RdYlGn',4))
plt.title("a population with 1 seeded carrier"+" \n Immunity= "+ str(immunity_rate) + 
	 "\n Virility= " + str(Virility) + " \n mortality rate= "+str(mort_r) +
	 "\n recovery rate= " + str(surv_r))

#normalise cb
plt.clim(-2,1)
plt.colorbar(ticks=range(-3,3), label= 'Healthy and Infected')

#show
plt.show()

#==========================================================================================
#==============================disease spread=============================================
#==========================================================================================


#we check how the disease develops as a function of time
#note that this save A LOT of figures (creation of gif)


for i in range (0,time,50):
	
	#create a plot showing the spread of disease throughout the population
	check= med.infection(N,M, i, infection_seed, immunity_rate, Virility, mort_r, time)
	plt.imshow(check,interpolation='none', cmap=plt.get_cmap('RdYlGn',4))
	plt.title("a population where disease has been allowed to spread"+" \n Immunity= "+ str(immunity_rate) + 
		 "\n Virility= " + str(Virility) + " \n mortality rate= "+str(mort_r) +
		 "\n recovery rate= " + str(surv_r) + "\n generations:" + str(i))
	
	#normalise cb
	plt.clim(-2,1)
	plt.colorbar(ticks=range(-3,3), label= 'Healthy and Infected')
	
	#show
	plt.savefig("infection_"+str(N)+ "_" +str(i*50), bbox_inches = 'tight')
	plt.close()

#===========================================================================
#==========================Medical treatment================================
#===========================================================================

#see what the 'before' looks like
plt.imshow(check,interpolation='none', cmap=plt.get_cmap('RdYlGn',4))

#normailse the cb
plt.clim(-2,1)
plt.colorbar(ticks=range(-4,3), label= 'Healthy and Infected')

#show
plt.show()

#apply medicine to the problem
bad_time=med.infection(N,M,time, infection_seed, immunity_rate, Virility, mort_r, time)
plt.imshow(bad_time,cmap=plt.get_cmap('RdYlGn',4), interpolation='none')

#normalise the colorbar
plt.clim(-2,1)
plt.colorbar(ticks=range(-3,3), label= 'Healthy and Infected')
plt.title("Prior to application of medicine")
plt.show()


for i in range (0,50): 
	recovery=med.recovery(N,M,time, bad_time, surv_r)
	plt.imshow(recovery, interpolation='none',cmap=plt.get_cmap('RdYlGn',4))
	plt.clim(-2,1)
	plt.colorbar(ticks=range(-3,3), label= 'Healthy and Infected')
	plt.title("after medicine")
	plt.savefig("11medicine_"+str(N)+ "_" +str(i), bbox_inches = 'tight')
	plt.close()
	i+=1


























