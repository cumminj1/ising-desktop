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
time_upper=1000
immunity_rate=99#herd immunity
Virility=100		#disease virility
mort_r= 95.	#mortality rate in percent

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


#we check how the disease develops as a function of time


for time in range (0,time_upper,50):
	#create a plot showing the spread of disease throughout the population
	check= med.infection(N,M, time, infection_seed, immunity_rate, Virility, mort_r, time_upper)
	plt.imshow(check,interpolation='none', cmap=plt.get_cmap('RdYlGn',4))
	plt.title("a population where disease has been allowed to spread"+" \n Immunity= "+ str(immunity_rate) + 
		 "\n Virility= " + str(Virility) + " \n mortality rate= "+str(mort_r) +
		 "\n recovery rate= " + str(surv_r) + "\n generations:" + str(time))
	#normalise cb
	plt.clim(-2,1)
	plt.colorbar(ticks=range(-3,3), label= 'Healthy and Infected')
	#show
	plt.savefig("infection_"+str(N)+ "_" +str(time*50), bbox_inches = 'tight')
	plt.close()
plt.imshow(check,interpolation='none', cmap=plt.get_cmap('RdYlGn',4))


#normailse the cb
plt.clim(-2,1)
plt.colorbar(ticks=range(-4,3), label= 'Healthy and Infected')
#show
plt.show()

