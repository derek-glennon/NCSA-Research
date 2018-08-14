#!/usr/bin/env python

#/projects/ncsa/grav/more_sims_for_Extraction/simulations


import sys
import os
import os.path
import matplotlib.pyplot as plt
import numpy as np

path = sys.argv[1]

mass_list = []
spin_list = []

problem_sims = []


print(os.access("/projects/ncsa/grav/more_sims_for_Extraction/simulations/J0068_N_40", os.R_OK))

#########################
#Get Simulation Paths
#########################
all_sims = []
sim_names = []
all_sims = sorted([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
for i in range(len(all_sims)):
	if "N40" in all_sims[i] or "N_40" in all_sims[i]:
		sim_names = np.append(sim_names, all_sims[i])


print(sim_names)

###############
#Start Loop
###############
for i in range(len(sim_names)):

	print(sim_names[i] + " Starting")

	####################
	#Get Output Paths
	####################
	dir_access = True
	if  os.access(path + "/" + sim_names[i], os.R_OK) is True:
		path_dirs = sorted(os.listdir(path + "/" + sim_names[i]))
	else:
		dir_access = False
		problem_sims = np.append(problem_sims, sim_names[i] +  "-no access")
		continue

	
	
	
	output_dirs = []

	for j in range(len(path_dirs)):
		if "output" in path_dirs[j] and "active" not in path_dirs[j]:
			output_dirs = np.append(output_dirs, path_dirs[j])


	#########################
	#Combine Output Data
	#########################

	#time = []
	#irr_mass = []
	#spin = []
	#mass = []

	#file_exists = True
	#file_access = True

	#for j in range(len(output_dirs)):
	#	temp_path = path + "/" + sim_names[i] + "/" + output_dirs[j] + "/" + sim_names[i] + "/quasilocalmeasures-qlm_scalars..asc"
	#	if os.path.isfile(temp_path) is True and os.access(temp_path, os.R_OK) is True:
	#		time = np.append(time, np.genfromtxt(temp_path, usecols=(1)))
	#		irr_mass = np.append(irr_mass, np.genfromtxt(temp_path, usecols=(19)))
	#		spin = np.append(spin, np.genfromtxt(temp_path, usecols=(37)))
	#		mass = np.append(mass, np.genfromtxt(temp_path, usecols=(58)))
	#	elif os.path.isfile(temp_path) is False:
	#		file_exists = False
	#		problem_sims = np.append(problem_sims, sim_names[i] + "-" + output_dirs[j] + "-no scalars file")
	#	elif  os.access(temp_path, os.R_OK) is False:
	#		file_access = False
	#		problem_sims = np.append(problem_sims, sim_names[i] + "-" + output_dirs[j] + "-no access")
	
	#########################
        #Get Last Output Data
	#########################
	time = []
	irr_mass = []
	spin = []
	mass = []

	last_outputs = [output_dirs[-4], output_dirs[-3], output_dirs[-2], output_dirs[-1]]

	print(last_outputs)

	file_exists = True
	file_access = True

	for j in range(len(last_outputs)):
		temp_path = path + "/" + sim_names[i] + "/" + last_outputs[j] + "/" + sim_names[i] + "/quasilocalmeasures-qlm_scalars..asc"
		if os.path.isfile(temp_path) is True and os.access(temp_path, os.R_OK) is True:
			time = np.append(time, np.genfromtxt(temp_path, usecols=(1)))
			irr_mass = np.append(irr_mass, np.genfromtxt(temp_path, usecols=(19)))
			spin = np.append(spin, np.genfromtxt(temp_path, usecols=(37)))
			mass = np.append(mass, np.genfromtxt(temp_path, usecols=(58)))
			print(len(mass))
		#elif os.path.isfile(temp_path) is False:
			#file_exists = False
			#problem_sims = np.append(problem_sims, sim_names[i] + "-" + last_outputs[j] + "-no scalars file")
			#print("No Scalars")
		#elif os.access(temp_path, os.R_OK) is False:
			#file_access = False
			#problem_sims = np.append(problem_sims, sim_names[i] + "-" + last_outputs[j] + "-no access")
			#print("No Access")
		


	#Check if mass and spin are long enough
	if len(mass) < 100 and file_exists is True and file_access is True:
		problem_sims = np.append(problem_sims, sim_names[i] + "-mass not long enough")
		continue

	if len(spin) < 100 and file_exists is True and file_access is True:
		problem_sims = np.append(problem_sims, sim_names[i] + "-spin not long enough")
		continue



	##########
	#Mass
	##########

	if file_exists is True and file_access is True:
		#Grab the mass 100 indicies away from the end
		mass_grab = mass[-100]

		#Add mass of this simulation to the list of masses from each simulation
		mass_list = np.append(mass_list, mass_grab)


	##########
	#Spin
	##########

	if file_exists is True and file_access is True:
		#Grab the spin 100 indicies away from the end
		spin_grab = spin[-100]

        	#Add spin of this simulation to the list of spins from each simulation
		spin_list = np.append(spin_list, spin_grab)




	print(sim_names[i] + " Ending")


#########################
#Cut Out Problem Sims
#########################
sim_names_cut = []
index = []

for i in range(len(problem_sims)):
	for j in range(len(sim_names)):
		if sim_names[j] in problem_sims[i]:
			index = np.append(index, j)
			continue


sim_names_cut = np.delete(sim_names, index)


#########################
#Get AAS Sims
#########################
AAS_sims = sorted(["E0001", "J0005", "J0045", "E0013", "E0017", "K0001", "J0061", "J0065", "M0004", "J0047", "K0024", "L0020"])
ecc_sims = [0.060, 0.070, 0.068, 0.067, 0.078, 0.120, 0.065, 0.080, 0.060, 0.120, 0.210, 0.190]
ratio_sims = [1.0, 2.5, 3.0, 1.5, 2.0, 2.0, 4.0, 4.5, 3.5, 4.0, 5.5, 1.0]
sim_names_AAS = []
mass_AAS = []
spin_AAS = []
ecc_AAS = []
ratio_AAS = []
index = []

for i in range(len(sim_names_cut)):
	for j in range(len(AAS_sims)):
		if AAS_sims[j] in sim_names_cut[i]:
			sim_names_AAS = np.append(sim_names_AAS, sim_names_cut[i])
			mass_AAS = np.append(mass_AAS, mass_list[i])
			spin_AAS = np.append(spin_AAS, spin_list[i])
			continue


for i in range(len(sim_names_AAS)):
	for j in range(len(AAS_sims)):
		if AAS_sims[j] in sim_names_AAS[i]:
			ecc_AAS = np.append(ecc_AAS, ecc_sims[j])
			ratio_AAS = np.append(ratio_AAS, ratio_sims[j])





###############
#Export Data
###############
export_data = np.zeros(sim_names_cut.size, dtype=[('var1', 'U9'), ('var2', float), ('var3', float)])
export_data['var1'] = sim_names_cut
export_data['var2'] = mass_list
export_data['var3'] = spin_list

np.savetxt("output.txt", export_data, fmt = "%s %15.8f %15.8f")


####################
#Export AAS Data
####################
export_data_AAS = np.zeros(sim_names_AAS.size, dtype=[('var1', 'U9'), ('var2', float), ('var3', float), ('var4', float), ('var5', float)])
export_data_AAS['var1'] = sim_names_AAS
export_data_AAS['var2'] = mass_AAS
export_data_AAS['var3'] = spin_AAS
export_data_AAS['var4'] = ecc_AAS
export_data_AAS['var5'] = ratio_AAS

np.savetxt("output_AAS.txt", export_data_AAS, fmt = "%s %15.8f %15.8f %15.8f %15.8f")





print(sim_names)
print(sim_names_cut)
print(sim_names_AAS)
print(problem_sims)

##########
#Plot
##########


#plt.plot(time[spin_index:], spin_cut)
#plt.show()







