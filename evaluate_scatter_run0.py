# -*- coding: utf-8 -*-
"""
Example script to serve as starting point for evaluating scatter results

The current script reads results from run_scatter_0 and displays them comparing 
with the truth (i.e. simulation input and simulation scatter output)

run_scatter_0.sh run the standard SSS scatter estimation algorithm on the 
simulated data, and then runs FBP.  With this exercise you get an idea
of what the scatter looks like and how accurate the scatter estimation is
in the ideal case (i.e. where the model exactly matches the actual scatter generation).

Prerequisite:
You should have executed the following on your command prompt
    ./run_simulations_thorax.sh
    ./run_scatter_0.sh

Author: Kris Thielemans
"""
#%% Initial imports
import matplotlib.pyplot as plt
import stir
from stirextra import *
import os
#%% go to directory with input files
# adapt this path to your situation (or start everything in the exercises directory)
os.chdir('/home/stir/exercises')
#%% run scatter 0 case (if you haven't done it yet)
print(os.popen('./run_scatter_0.sh').read())
#%% change directory to where the output files are
os.chdir('working_folder/GATE1')
#%% read in data from GATE1
# original scatter as generated by the simulation
org_scatter=to_numpy(stir.ProjData.read_from_file('my_scatter_g1.hs'));
# estimated scatter
estimated_scatter=to_numpy(stir.ProjData.read_from_file('scatter_estimate_run0.hs'));
#%% Display bitmaps of a middle sinogram
maxforplot=org_scatter.max()*1.1;

plt.figure()
ax=plt.subplot(1,2,1);
plt.imshow(org_scatter[10,:,:,]);
plt.clim(0,maxforplot)
ax.set_title('Original simulated scatter');
plt.axis('off');

ax=plt.subplot(1,2,2);
plt.imshow(estimated_scatter[10,:,:,]);
plt.clim(0,maxforplot);
ax.set_title('estimated scatter');
plt.axis('off');
#%% Display central profiles through the sinogram
plt.figure()
plt.plot(org_scatter[10,:,192/2],'b');
plt.hold(True)
plt.plot(estimated_scatter[10,:,192/2],'c');
plt.legend(('original','estimated'));
#%% Read in images
org_image=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('FDG_g1.hv'));
fbp_result=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('FBP_recon_with_scatter_correction_run0.hv'));
#%% bitmap display of images
maxforplot=org_image.max()*1.1;

slice=10;
plt.figure();
plt.subplot(1,2,1);
plt.imshow(org_image[slice,:,:,]);
plt.colorbar();
plt.clim(0,maxforplot);
plt.set_title('input for simulation')
plt.axis('off');

plt.subplot(1,2,2);
plt.imshow(fbp_result[slice,:,:,]);
plt.clim(0,maxforplot);
plt.colorbar();
plot.set_title('FBP after scatter correction')
plt.axis('off');
#%% horizontal profiles through images
plt.figure();
plt.plot(org_image[10,154/2,:],'b');
plt.hold(True);
plt.plot(fbp_result[10,154/2,:],'c');
plt.legend(('Input for simulation','Reconstruction'));
#%% close all plots
plt.close('all')
