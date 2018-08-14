# -*- coding: utf-8 -*-
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math

styles = ["-" , "--" , "-." , ":","-"]
colors = ["b" , "r" , "g" , "m","c"]
alphas = [1, 1, 1, 1, 0.50]

SimNames = [["M0004", "M0008"] , ["L0037", "L0038", "L0039", "L0040"]]

lw = 3.0

max_x_dists = [[0,0,0,0,0],[0,0,0,0]]
nearest_ten_mins = [[0,0,0,0,0],[0,0,0,0]]
 
upper_limit_y = math.log10(40)
  
order = 8

past_merger = 150

matplotlib.rcParams.update({'font.size': 30})
csfont = {'fontname':'Times New Roman'}

for k in range(len(SimNames)):
    
    for j in range(len(SimNames[k])):
        
        plt.figure(k + 1)

        print(SimNames[k][j]+" is starting")    
    
        progress = True
        
        path = "C:\\Users\\eagle\\Desktop\\Convergence\\" +str(order)+ "th_Order\\Data\\exportDataCombined_"+SimNames[k][j]+".dat"

        if progress is True:
            data_x = np.genfromtxt(path, usecols=(0))
            data_y = np.genfromtxt(path, usecols=(1))

            data_merger_x = np.genfromtxt(path, usecols=(2))
            data_merger_y = np.genfromtxt(path, usecols=(3))

            data_x = np.abs(data_x)
            data_y = np.abs(data_y)

            plt.axes().set_yscale("log")
            
            plt.plot(data_x,data_y,ls = styles[j] , color = colors[j], alpha = alphas[j], linewidth = lw , label = SimNames[k][j])
            
            plt.xlabel("Time [M]", **csfont)
            plt.ylabel("|Phase Error| [rad]", **csfont) 
    
            print(SimNames[k][j]+" is done")
            
          
path = "C:\\Users\\eagle\\Desktop\\Convergence\\8th_Order\\Plots\\"       
          
plt.figure(1)
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.legend(loc = 'best')
final_x_lim = np.max(max_x_dists[0])
final_ten_min = np.min(nearest_ten_mins[0]))
plt.savefig(path + "Phase_Error_Others.png")
plt.savefig(path + "Phase_Error_Others.pdf")

plt.figure(2)
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.legend(loc = 'best')
final_x_lim = np.max(max_x_dists[1])
final_ten_min = np.min(nearest_ten_mins[1])
plt.savefig(path + "Phase_Error_q_5_and_half-2.png")
plt.savefig(path + "Phase_Error_q_5_and_half-2.pdf")
    

plt.show()
