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
N=30
M=30
steps=6000000000
immunity_rate=1000.#herd immunity
Virility=10001.0		#disease virility
T=50
J=1
Kb=1
mort_r=20.0	#mortality rate in percent
surv_r=50. 



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

for steps in range (0,1000,50):
	#create a plot showing the spread of disease throughout the population
	check= med.infection(N,M, steps, infection_seed, immunity_rate, Virility)
	plt.imshow(check,interpolation='none', cmap=plt.get_cmap('RdYlGn',4))
	plt.title("a population where disease has been allowed to spread"+" \n Immunity= "+ str(immunity_rate) + 
		 "\n Virility= " + str(Virility) + " \n mortality rate= "+str(mort_r) +
		 "\n recovery rate= " + str(surv_r) + "\n generations:" + str(steps))
	#normalise cb
	plt.clim(-2,1)
	plt.colorbar(ticks=range(-3,3), label= 'Healthy and Infected')
	#show
	plt.savefig("infection_"+str(N)+ "_" +str(steps*50))
	plt.close()


#create a plot showing the fatalities due to the disease
death_check= med.death(N,M,steps, check, mort_r)
plt.imshow(death_check, interpolation='none', cmap=plt.get_cmap('RdYlGn',4))
plt.title("The spread of disease related death in a population"+" \n Immunity= "+ str(immunity_rate) + 
	 "\n Virility= " + str(Virility) + " \n mortality rate= "+str(mort_r) +
	 "\n recovery rate= " + str(surv_r))
#normailse the cb
plt.clim(-2,1)
plt.colorbar(ticks=range(-4,3), label= 'Healthy and Infected')
#show
plt.show()

