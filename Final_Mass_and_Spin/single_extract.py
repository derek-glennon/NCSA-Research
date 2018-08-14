#!/usr/bin/env python

#/projects/ncsa/grav/more_sims_for_Extraction/simulations


import sys
import os
import matplotlib.pyplot as plt
import numpy as np

path = sys.argv[1]
sim_name = sys.argv[2]

problem_outputs = []


####################
#Get output Paths
####################
path_dirs = sorted(os.listdir(path + "/" + sim_name))
output_dirs = []

for i in range(len(path_dirs)):
	if "output" in path_dirs[i]:
		output_dirs = np.append(output_dirs, path_dirs[i])


#########################
#Combine Output Data
#########################

time = []
irr_mass = []
spin = []
mass = []

file_exists = True
file_access = True


for i in range(len(output_dirs)):
	temp_path = path + "/" + sim_name + "/" + output_dirs[i] + "/" + sim_name + "/quasilocalmeasures-qlm_scalars..asc"
	if os.path.isfile(temp_path) is True and os.access(temp_path, os.R_OK) is True:
		time = np.append(time, np.genfromtxt(temp_path, usecols=(1)))
		irr_mass = np.append(irr_mass, np.genfromtxt(temp_path, usecols=(19)))
		spin = np.append(spin, np.genfromtxt(temp_path, usecols=(37)))
		mass = np.append(mass, np.genfromtxt(temp_path, usecols=(58)))
	elif os.path.isfile(temp_path) is False:
		file_exists = False
		problem_outputs = np.append(problem_outputs, sim_name + "-" + output_dirs[i] + "-no scalars file")
	elif os.access(temp_path, os.R_OK) is False:
		file_access = False
		problem_outputs = np.append(problem_outputs, sim_name + "-" + output_dirs[i] + "-no access")

##########
#Mass
##########

mass_index = 0

for i in range(len(mass)):
	if mass[i] != 0:
		mass_index = i
		break

mass_index = mass_index + 10

mass_cut = mass[mass_index:]

mass_avg = np.average(mass_cut)

print(mass_avg)


##########
#Spin
##########

spin_index = 0

for i in range(len(spin)):
	if spin[i] != 0:
		spin_index = i
		break

spin_index = spin_index + 10

spin_cut = spin[spin_index:]

spin_avg = np.average(spin_cut)

print(spin_avg)



print(problem_outputs)

##########
#Plot
##########


plt.plot(time, mass)
plt.show()







