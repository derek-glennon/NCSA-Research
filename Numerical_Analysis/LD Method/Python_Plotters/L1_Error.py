# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:38:28 2017

@author: Derek Glennon
"""

# -*- coding: utf-8 -*-
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams.update({'font.size': 25})
csfont = {'fontname':'Times New Roman'}

T = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FD_Error_Final_Test_50.dat", usecols=(0))

error_LD2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FD_Error_Final_Test_50.dat", usecols=(1))
error_LD4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FD_Error_Final_Test_50.dat", usecols=(2))
error_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FD_Error_Final_Test_50.dat", usecols=(3))
error_RK4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FD_Error_Final_Test_50.dat", usecols=(4))
error_LD6 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FD_Error_Final_Test_50.dat", usecols=(5))
error_RK6 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FD_Error_Final_Test_50.dat", usecols=(6))
error_LD8 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\FD_Error_Final_Test_50.dat", usecols=(7))

fig = plt.figure()
ax = plt.subplot(111)

ax.semilogy(T, error_RK2, 'orange', lw = 3, linestyle = '--', label = "RK2 FD50")

ax.semilogy(T, error_LD2 , 'b-', lw = 3, alpha = 0.5, label = "LD2 FD50")

ax.semilogy(T, error_RK4, 'r-', lw = 3, linestyle = '--', label = "RK4 FD50")

ax.semilogy(T, error_LD4, 'm-', lw = 3,  alpha = 0.5, label = "LD4 FD50")

ax.semilogy(T, error_RK6, 'y-', lw = 3, linestyle = '--', alpha = 0.5, label = "RK6 FD50")

ax.semilogy(T, error_LD6, 'c-', lw = 3, alpha = 0.5, label = "LD6 FD50")

ax.semilogy(T, error_LD8, 'k-', lw = 3, alpha = 0.5, label = "LD8 FD50")

#plt.legend(loc = 'best')

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

ax.set_xlabel("Time")
ax.set_ylabel("$L^1$ Error")
#plt.title("Courant Number = 0.31831 & FD")

plt.ylim([10**(-16),10**(0)])


manager = plt.get_current_fig_manager()
manager.window.showMaximized()

plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\FD_L1_Error.pdf")



fig = plt.figure()
ax = plt.subplot(111)

T = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS_Final_Test.dat", usecols=(0))

error_LD2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS_Final_Test.dat", usecols=(1))
error_LD4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS_Final_Test.dat", usecols=(2))
error_RK2 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS_Final_Test.dat", usecols=(3))
error_RK4 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS_Final_Test.dat", usecols=(4))
error_LD6 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS_Final_Test.dat", usecols=(5))
error_RK6 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS_Final_Test.dat", usecols=(6))
error_LD8 = np.genfromtxt("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Data\\Error_PS_Final_Test.dat", usecols=(7))

ax.semilogy(T, error_RK2, 'orange', lw = 3, linestyle = '--', label = "RK2 PS")

ax.semilogy(T, error_LD2 , 'b-', lw = 3, alpha = 0.5, label = "LD2 PS")

ax.semilogy(T, error_RK4, 'r-', lw = 3, linestyle = '--', label = "RK4 PS")

ax.semilogy(T, error_LD4, 'm-', lw = 3,  alpha = 0.5, label = "LD4 PS")

ax.semilogy(T, error_RK6, 'y-', lw = 3, linestyle = '--', alpha = 0.5, label = "RK6 PS")

ax.semilogy(T, error_LD6, 'c-', lw = 3, alpha = 0.5, label = "LD6 PS")

ax.semilogy(T, error_LD8, 'k-', lw = 3, alpha = 0.5, label = "LD8 PS")

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

#plt.legend(loc = ([.78,.16]))
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

ax.set_xlabel("Time")
ax.set_ylabel("$L^1$ Error")
#plt.title("Courant Number = 0.31831 & Fourier PS")

ax.set_xlim([0,15])
ax.set_ylim([10**(-15),10**(-1)])


manager = plt.get_current_fig_manager()
manager.window.showMaximized()

plt.savefig("C:\\Users\\eagle\\Desktop\\Research\\FD_Paper\\Python_Plots\\Pseudospectral_L1_Error.pdf")


plt.show()