####################################################
#
# Written by Chris Karwin; 2020; Clemson University
# Based on orignal code from Marco Ajello, Vaidehi Paliya, and Abhishek Desai
#
# Classes:
#	1) joint_likelihood(superclass)
#	2) standard_analysis(joint_likelihood)
#
# Purpose: 
#	1) Add indivual TS profiles to obtain the stacked profile
#	2) Obtain corresponding statistics of stacked profile
#	3) Make plots
#
# Index of functions:
#
#	joint_likelihood(superclass):
#		- combine_joint_likelihood(savefile, working_directory, bin_stacking_input, make_array_image) 
#		- plot_final_array(savefig,array,calc_UL,calc_marginal_error)
#		- make_bins()
#		- get_UL(flux_list,array)
#		- get_UL_2(srcname,index,working_directory)
#		- JL_bayesian_upper_limit(working_directory,srcname)
#		- get_marginal_error(array,index,flux)
#		- interpolate_array()
#
#	standard_analysis(joint_likelihood):
#		- combine_likelihood(savefile, working_directory, bin_stacking_input, make_array_image)
#
###################################################

###################################################
#imports
import pandas as pd
import numpy as np
import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import os
import math
from scipy.stats import norm
import matplotlib.mlab as mlab
import sys
import numpy as np
from scipy.ndimage.filters import gaussian_filter
from astropy.convolution import convolve, Gaussian2DKernel
from matplotlib.cm import register_cmap,cmap_d
from scipy import stats, interpolate, optimize
from matplotlib import ticker, cm
from scipy.stats.contingency import margins
import pyLikelihood
from BinnedAnalysis import *
from fermipy.gtanalysis import GTAnalysis
import PopStudies as PS
from IntegralUpperLimit import calc_int
from UpperLimits import UpperLimits
from SummedLikelihood import *
from astropy.io import fits

############################
#The joint likelihood class:
class joint_likelihood:

	def __init__(self,exclusion_list):

		#define paths:
		self.preprocessing_path = "/zfs/astrohe/ckarwin/Stacking_Analysis/LLAGN/Preprocessed_Sources/"
		self.stacking_path = "/zfs/astrohe/ckarwin/Stacking_Analysis/LLAGN/Stacking_Results/"
		self.add_stacking_path = "/zfs/astrohe/ckarwin/Stacking_Analysis/LLAGN/Control_Center/add_stacking/"
		self.data_path = "/zfs/astrohe/ckarwin/Stacking_Analysis/LLAGN/Sample/"	
	
		#upload source catalog:
		this_file = self.data_path + "LLAGN_sample.dat"
		df = pd.read_csv(this_file,delim_whitespace=True,skiprows=[0,1,2,3,4,5,6])
		self.name_list = df["name"].tolist()
		ra_list = df["ra(J2000)"].tolist()
		dec_list = df["dec(J2000)"].tolist()

                #use control sample instead of source sample:
                hdu = fits.open(self.data_path + "LLAGN_control_sample_full.fits")
                data = hdu[1].data
                #self.name_list = data["Name_1"].strip().tolist()
                #ra_list = data["_RAJ20001"].tolist()
                #dec_list = data["_DEJ20001"].tolist()

                #use HII sample:
                hdu = fits.open(self.data_path + "HII_Sample_Master.fits")
                data = hdu[1].data
                #self.name_list = data["Name1_1"].strip().tolist()
                #ra_list = data["_RAJ20001"].tolist()
                #dec_list = data["_DEJ20001"].tolist()
        
                #use significant sources:
                #self.name_list = ["NGC_1275","NGC_4486","NGC_315","NGC_4261"]

                #define list to exclude in stacked sum:
                self.exclusion_list = exclusion_list
            
	#####################################
	#combine profiles to a summed array:
	def combine_joint_likelihood(self, savefile, working_directory, likelihood_directory, bin_stacking_input, make_array_image):

		####################
		#
		# Input definitions:
		#
		# savefile: Prefix of array to be saved. Do not include ".npy" at the end of name; it's already included.
		#
		# working_directory: The directory of the run (not the full path). It should be the same for adding, stacking, and preprocessing.
		#
		# likelihood_directory: The directory containing the null likelihood. 
		#
		# bin_stacking_input: Whether or not to stack in bins. Needs to be a list of size 2. First element is a boolean; second element is which bin to add. 
		#
		# make_array_image: Whether or not to make an array image of all TS profiles. Needs to be a list of size 3. 
		# First element is a boolean; second element is number of rows for image; third element is number of columns for image.		
		#
		####################

		#make print statement:
		print
		print "********** Add Stacking Module ************"
		print "Running combine_joint_likelihood..."
		print
		
		#get current working directory:
		home = os.getcwd()

		#specify working directory:
		working_directory = str(working_directory)

		#specify likelihood directory:
		likelihood_directory = str(likelihood_directory)

		#specify output file:
		savefile = savefile

		#whether or not to stack in bins:
		bin_stacking = bin_stacking_input[0]
		this_sublist = bin_stacking_input[1]

		#whether or not to make array image:
		make_array_image_switch = make_array_image[0]
		rows = make_array_image[1]
		columns = make_array_image[2]

		#write save directories:
		if os.path.exists("Numpy_Arrays") == False:
			os.system("mkdir Numpy_Arrays")

		#perform stacking in bins:
		if bin_stacking == True:
			sublist1, sublist2 = self.make_bins() 
			if this_sublist == 1:
				sublist = sublist1
			if this_sublist == 2:
				sublist = sublist2
		if bin_stacking == False:
			sublist = self.name_list
		
		#for manuel test:
		#sublist = ["NGC_4151"] 

		#make stack:

		total_counter = 0

		plot_list = []
		
		#make an array image of TS profiles for each source
		if make_array_image_switch == True:
			#setup benchmark figure:
			fig = plt.figure(figsize=(18,22))
			columns = columns
			rows = rows
		
		#iterate through sources:
		for s in range(0,len(self.name_list)):
	
			srcname = self.name_list[s]
			counter = 0
			
			j_counter = 0
			for j in [0,1,2,3]:
	
				likelihood_dir = self.preprocessing_path + "%s/%s/output/null_likelihood_%s.txt" %(likelihood_directory,srcname,j)
				stacking_dir = self.stacking_path + "%s/Likelihood_%s/%s" %(working_directory,j,srcname)
				
				if os.path.exists(stacking_dir) == False or os.path.exists(likelihood_dir) == False:
					if j_counter == 0:
						#print 
						#print 'Does not exist: ' + srcname
						#print 
						j_counter += 1

				#here you can specify which sources to stack:
	                        if srcname not in self.exclusion_list and os.path.exists(likelihood_dir) == True and os.path.exists(stacking_dir) == True:	
					os.chdir(stacking_dir)
	
					array_list = []

					#Need to use 1.0001 and 2.0001 for lum stacking.
                                        #index_list = np.arange(1,4.1,0.1) #for flux stacking
				        index_list = np.arange(0.5,1.7,0.1) #alpha list, for alpha-beta stacking
					
                                        f = open(likelihood_dir,'r')
					lines = f.readlines()
					null = float(lines[0])
	
					for i in range(0,len(index_list)):
						this_index = str(index_list[i])
						this_file = "%s_stacking_LLAGN_%s.txt" %(srcname,this_index)

						#print this_file
						df = pd.read_csv(this_file,delim_whitespace=True,names=["flux","index","likelihood","quality","status"])
                                                
						flux = df["flux"]
						index = df["index"]
						likelihood = df["likelihood"].tolist()
						TS = 2*(df["likelihood"]-null)
						TS = TS.tolist()
				
						array_list.append(TS)

					final_array = np.array(array_list)
					if counter == 0:
						summed_array = final_array
					if counter > 0:
						summed_array = np.add(summed_array,final_array)
					counter += 1

                        if srcname not in self.exclusion_list and os.path.exists(likelihood_dir) == True and os.path.exists(stacking_dir) == True:
				
				#save each individual source array:
                		source_array_file = self.add_stacking_path + "/%s/Numpy_Arrays/Individual_Sources/" % working_directory
                		if os.path.exists(source_array_file) == False:
                        		os.system("mkdir %s" % source_array_file)
                		source_array_file += str(srcname) + "_array"
                		np.save(source_array_file,summed_array)
	
					
				plot_list.append(srcname)

				if total_counter == 0:
					total_summed_array = summed_array
				if total_counter > 0:
					total_summed_array = np.add(total_summed_array,summed_array)
				total_counter += 1
	
				if make_array_image_switch == True:
					
					#######################
					#plot 
	        			#setup figure:
                			fig.add_subplot(rows,columns,total_counter)
                			ax = plt.gca()

					#this is here for now to fix last column of plot:
					new_col = summed_array.sum(1)[...,None]
					for i in range(0,new_col.shape[0]):
        					new_col[i] = 0
                			summed_array = np.append(summed_array,new_col,axis=1)

					ind = np.unravel_index(np.argmax(summed_array,axis=None),summed_array.shape)                

					max_value = np.amax(summed_array)
                			min_value = np.amin(summed_array)

					if max_value<1:
                				max_value = 1
	
					index_list = [-1*x for x in index_list]
					best_index = index_list[ind[0]]                

					flux_list = np.linspace(-5,-1,num=41,endpoint=True) #for efficiency stacking
					#flux_list = np.linspace(-13,-9,num=41,endpoint=True) #for flux stacking
                			#flux_list = np.linspace(39,43,num=41,endpoint=True)  #for luminosity stacking
					for i in range(0,len(flux_list)):
                        			flux_list[i] = 10**flux_list[i]
					best_flux = flux_list[ind[1]]		

					img = ax.pcolormesh(flux_list,index_list,summed_array,cmap="inferno",vmin=0,vmax=max_value)
					plt.plot(best_flux,best_index,marker="+",ms=12,color="black")               
 
					ax.set_xscale('log')
                			y_ticks = [-1.0,-1.2,-1.4,-1.6,-1.8,-2.0,-2.2,-2.4,-2.6,-2.8,-3.0,-3.2]
                			ax.set_yticks(y_ticks)
                			plt.xticks(fontsize=14)
                			plt.yticks(fontsize=14)

					#plot colorbar
                			cbar = plt.colorbar(img,fraction=0.045)
                			cbar.ax.tick_params(labelsize=14)

                			plt.title(srcname,fontsize=22,fontweight='bold',y=1.04)
                			plt.ylabel('Photon Index',fontsize=16)
                			plt.xlabel(r'$\epsilon_{\mathrm{UFO}}$',fontsize=16) #for efficiency stacking
					#plt.xlabel(r'$\mathregular{\gamma}$-Ray Luminosity [erg s$\mathregular{^{-1}}$]',fontsize=16) #for luminosity stacking

                			ax.set_aspect('auto') #set aspect ration to make square image (aspect = smaller_axis_bins/larger_axis_bins, or vice versa depending on layout)
                			ax.tick_params(axis='both',which='major',length=7)
                			ax.tick_params(axis='both',which='minor',length=4)
					
					

		print
		print "Number of sources included in sum: " + str(len(plot_list))
		print plot_list
		print

		#exit code if no sources were added:
		if len(plot_list) == 0:
			print "There are no sources that met your criterion."
			print "Exiting code."
			sys.exit() 

		
		#save image:
		if make_array_image_switch == True:
			plt.tight_layout()
			savefig = self.add_stacking_path + "%s/Images/" % working_directory
			if os.path.exists(savefig) == False:
                        	os.system("mkdir %s" % savefig)
			plt.savefig(savefig + "TS_profiles.png")
			plt.show()
			plt.close()
		
		#save array:
		total_array_file = self.add_stacking_path + "/%s/Numpy_Arrays/" % working_directory
		if os.path.exists(total_array_file) == False:
                	os.system("mkdir %s" % total_array_file)
		total_array_file += savefile
		np.save(total_array_file,total_summed_array)

		#return to home:
		os.chdir(home)
		
		return
		
	################################################
	#plot final array and get erors from the array:
	def plot_final_array(self,savefig,array,calc_UL,calc_marginal_error):

		#####################
		# 
		# Input definitions:
		# 
		# savefig: Name of image file to be saved. 
		#
		# array: Name of input array to plot. Must include ".npy".
		#
		# calc_UL: boolean, whether or not to calculate UL
		# 
		# marginal_error: boolean, whether or not to calculate marginal error. 
		#
		####################

		#make print statement:
		print
		print "********** Add Stacking Module **********"
		print "Running plot_final_array..."
		print

		#specify the savefigure:
		savefig = "Images/" + savefig

		#specify the array to plot:
		array = array
	
		#specify wether or not to calculate an UL:
		calc_UL = calc_UL

		#specify wether or not to calculate marginal error:
		calc_marginal_error = calc_marginal_error

		#make save directory:
		if os.path.exists("Images") == False:
			os.system("mkdir Images")

		#setup figure:
		fig = plt.figure(figsize=(9,9))
		ax = plt.gca()

		#upload summed array:
		summed_array = np.load("Numpy_Arrays/" + array)

		#get min and max:
		max_value = np.amax(summed_array)
		min_value = np.amin(summed_array)

		#corresponding sigma for 2 dof:
		num_pars = 2
		sigma = stats.norm.ppf(1.-stats.distributions.chi2.sf(max_value,num_pars)/2.)

		#significane contours for dof=2:
		first = max_value - 2.3 #0.68 level
		second = max_value - 4.61 #0.90 level
		third =  max_value - 9.21 #0.99 level

		#find indices for max values:
		ind = np.unravel_index(np.argmax(summed_array,axis=None),summed_array.shape)
		best_index_value = ind[0]
		best_flux_value = ind[1]

		#get best index:
                #index_list = np.arange(1,4.1,0.1) #for flux stacking
                index_list = np.arange(0.5,1.7,0.1) #alpha_list, for alpha-beta stacking
                
                best_index = index_list[ind[0]]

		#get best flux:
		#flux_list = np.linspace(-13,-9,num=40,endpoint=True) #for flux stacking
                #flux_list = np.linspace(38,42,num=40,endpoint=True) #for lum stacking
	        #flux_list = 10**flux_list #uncomment for flux and lum stacking
                flux_list = np.arange(38,40.2,0.1) #beta_list, for alpha-beta stacking

		#flux_list = 10**flux_list #for flux stacking
                best_flux = flux_list[ind[1]]

		#smooth array:
		gauss_kernel = Gaussian2DKernel(1.5)
		filtered_arr = convolve(summed_array, gauss_kernel, boundary='extend')

		#################
		#Below I define 3 different methods to plot the array, just with different styles.
		#Use method 1 as the default.

		#method 1
		def plot_method_1():

			img = ax.pcolormesh(flux_list,index_list,summed_array,cmap="inferno",vmin=0,vmax=max_value)
			plt.contour(flux_list,index_list,summed_array,levels = (third,second,first),colors='black',linestyles=["-.",'--',"-"], alpha=1,linewidth=2*4.0)
			plt.plot(best_flux,best_index,marker="+",ms=12,color="black")
			ax.set_xscale('log')
			#y_ticks = [-1.0,-1.2,-1.4,-1.6,-1.8,-2.0,-2.2,-2.4,-2.6,-2.8,-3.0,-3.2,-3.4,-3.6,-3.8,-4.0]
			#ax.set_yticks(y_ticks)
			plt.xticks(fontsize=16)
			plt.yticks(fontsize=16)
			#plt.xlim(1e-13,1e-9)

			return img

		#method 2 
		def plot_method_2():

			#clip the array at zero for visualization purposes:
			for i in range(0,summed_array.shape[0]):
				for j in range(0,summed_array.shape[1]):
					if summed_array[i,j] < 0:
						summed_array[i,j] = 0

			img = ax.contourf(flux_list,index_list,summed_array,100,cmap="inferno")
			plt.contour(flux_list,index_list,summed_array,levels = (third,second,first),colors='black',linestyles=["-.",'--',"-"], alpha=1,linewidth=4.0)
			plt.plot(best_flux,best_index,marker="+",ms=12,color="black")
			#ax.set_xscale('log')
			#y_ticks = [-1.0,-1.2,-1.4,-1.6,-1.8,-2.0,-2.2,-2.4,-2.6,-2.8,-3.0]
			#ax.set_yticks(y_ticks)
			#plt.xticks(fontsize=14)
			plt.yticks(fontsize=14)
			#plt.ylim(0.9,1.1)
                        #plt.xlim(1,2)
			return img

		#method 3
		def plot_method_3():

			img = ax.imshow(summed_array,origin="upper",cmap='inferno',vmin=0,vmax=max_value)
			ax.contour(summed_array,levels = (third,second,first),colors='black',linestyles=["-.",'--',"-"], alpha=1,linewidth=4.0)

			#y_tick_labels = [-1.0,-1.2,-1.4,-1.6,-1.8,-2.0,-2.2,-2.4,-2.6,-2.8,-3.0]
			#y_ticks = [0,2,4,6,8,10,12,14,16,18,20]
			#ax.set_yticks(y_ticks)
			#ax.set_yticklabels(y_tick_labels,fontsize=14)

			#x_tick_labels = [1e-13,1e-12,1e-11,1e-10,7.9e-10]
			#x_ticks = [0,10,20,30,39]
			#ax.set_xticks(x_ticks)
			#ax.set_xticklabels(x_tick_labels,fontsize=14)

			return img

		#make plot with this method:
		img = plot_method_1()

		#plot colorbar
		cbar = plt.colorbar(img,fraction=0.045)
		cbar.set_label("TS",size=16,labelpad=12)
		cbar.ax.tick_params(labelsize=12)

		#plt.title("Stacked LLAGN (Run 4)",fontsize=25,y=1.04)
		#plt.ylabel('Photon Index',fontsize=22)
		plt.ylabel("Alpha",fontsize=22) #for alpha-beta
                #plt.xlabel(r'$\mathregular{\gamma}$-Ray Flux [ph $\mathrm{cm^2}$  s$\mathregular{^{-1}}$]',fontsize=22) #for flux
                #plt.xlabel(r'$\mathregular{\gamma}$-Ray Luminosity [erg  s$\mathregular{^{-1}}$]',fontsize=22) #for luminosity
                plt.xlabel('Beta',fontsize=22) #for alpha-beta

		#ax.set_aspect(1.67) #set aspect ration to make square image (aspect = smaller_axis_bins/larger_axis_bins, or vice versa depending on layout)
		ax.set_aspect('auto')

		ax.tick_params(axis='both',which='major',length=9)
		ax.tick_params(axis='both',which='minor',length=5)
	
		plt.savefig(savefig,bbox_inches='tight')
		plt.show()
		plt.close()

		#################
		#find 1 sigma error from the 2d array

		#important note: the for loop is constrained to scan the respective list only once;
		#otherwise it will loop through numerous times.

		#get 1 sigma index upper error (lower direction of map):
		for j in range(0,len(index_list)-best_index_value):
	
			if math.fabs(summed_array[ind[0]+j][ind[1]] - max_value) < 2.3:
				pass 
			if math.fabs(summed_array[ind[0]+j][ind[1]] - max_value) >= 2.3:
				index_sigma_upper = math.fabs(index_list[ind[0]] - index_list[ind[0]+j])
				break
			if j == (len(index_list)-best_index_value-1):
				index_sigma_upper = 0 #in this case the index is not constrained toward bottom of map

		#get 1 sigma index lower error (upper direction of map):
		for j in range(0,best_index_value):

        		if math.fabs(summed_array[ind[0]-j][ind[1]] - max_value) < 2.3:
                		pass
        		if math.fabs(summed_array[ind[0]-j][ind[1]] - max_value) >= 2.3:
                		index_sigma_lower = math.fabs(index_list[ind[0]] - index_list[ind[0]-j])
				break
			if j == best_index_value-1:
				index_sigma_lower = 0 #in this case the index is not constrained toward top of map
		

		#get 1 sigma flux upper error:
		for j in range(0,len(flux_list)-best_flux_value):

        		if math.fabs(summed_array[ind[0]][ind[1]+j] - max_value) < 2.3:
                		pass
        		if math.fabs(summed_array[ind[0]][ind[1]+j] - max_value) >= 2.3:
                		flux_sigma_upper = math.fabs(flux_list[ind[1]] - flux_list[ind[1]+j])
                		break
			if j == (len(index_list)-best_index_value - 1):
				flux_sigma_upper = 0 #in this case the flux is not constrained toward right of map

		#get 1 sigma flux lower error:
		for j in range(0,best_flux_value):

        		if math.fabs(summed_array[ind[0]][ind[1]-j] - max_value) < 2.3:
                		pass
        		if math.fabs(summed_array[ind[0]][ind[1]-j] - max_value) >= 2.3:
                		flux_sigma_lower = math.fabs(flux_list[ind[1]] - flux_list[ind[1]-j])
                		break
			if j == best_flux_value-1:
				flux_sigma_lower = 0 #in this case the index is not constrained toward left of map

		print 
		print "max TS: " + str(max_value) + "; sigma: " + str(sigma)
		print "indices for max TS: " + str(ind)
		print "Sanity check on indices: " + str(summed_array[ind])
		print "Best index: " + str(best_index) + ", Error:  +" + str(index_sigma_upper) + ", -" + str(index_sigma_lower)  
		print "Best flux: " + str(best_flux)  + ", Error: +" + str(flux_sigma_upper) + ", -" + str(flux_sigma_lower)
		print

		###############
		#calculate UL:
		if calc_UL == True:
			self.get_UL(flux_list,summed_array)

		################
		#get marginal error:
		if calc_marginal_error == True:
			self.get_marginal_error(summed_array,index_list,flux_list)

		return
	
	####################################
	#make bins for stacking:
	def make_bins(self):

		#make print statement:
		print
		print "********** Add Stacking Module **********"
		print "Running make_bins..."
		print

		#########################
		#upload UFO parameters:
		ufo_df = pd.read_csv(self.data_path + "UFO_properties.dat",delim_whitespace=True)
		ufo_name = ufo_df["Name"]
		ufo_power_low = ufo_df["PL"]
		ufo_PLE = ufo_df["PLE"]
		ufo_power_high = ufo_df["PH"]
		ufo_PHE = ufo_df["PHE"]
		ufo_BH = ufo_df["BH"]
		ufo_BHE = ufo_df["BHE"]
		ufo_Bol = ufo_df["Bol"]
	
		mid = ((ufo_power_low - ufo_PLE) + (ufo_power_high + ufo_PHE))/2.0
		kp_mean = np.mean(mid)	
		kp_var = np.var(mid)	
		kp_high = kp_mean + kp_var
		kp_low = kp_mean - kp_var

		print "$$$$$$$$$$$$$$"	
		print 10**kp_mean
		print 10**kp_high
		print 10**kp_low
		
		#Eddington ratio:
		Edd_list = 1.38e38*(10**ufo_BH)
		Edd_list = (10**ufo_Bol)/Edd_list

		#define lists:
		power_mean_list = []
		power_mean_error_list = []
		mid_list = []
		sublist1 = []
		sublist2 =[]
		bin_1 = []
		bin_1_error = []
		bin_2 = []
		bin_2_error = []
		sigma2_list = []
		ratio_list = []

		#bin divids:
		low_divide = 42.9
		high_divide = 45.2
		mean_divide = 44.2
		mid_divide = 44.3
		bh_divide = 7.64
		bol_divide = 44.4
		ratio_divide = 0.0457 

		#switches for calculation:
		high_calc = False
		mean_calc = False
		low_calc = False
		mid_calc = True
		bh_calc = False
		bol_calc = False
		Edd_calc = False

		#make bins:
		for i in range(0,len(ufo_name)):

			this_name = ufo_name[i]
			this_low = ufo_power_low[i]
			this_high = ufo_power_high[i]
			this_low_error = ufo_PLE[i]
			this_high_error = ufo_PHE[i]	
			this_bh = ufo_BH[i]
			this_bhE =  ufo_BHE[i]
			this_bol = ufo_Bol[i]
			this_edd = Edd_list[i]

			this_mean = (this_low + this_high)/2.0
			this_mean_error = (this_low_error + this_high_error)/2.0
			power_mean_list.append(this_mean)
			power_mean_error_list.append(this_mean_error)	

			this_mid = ((this_low-this_low_error) + (this_high+this_high_error))/2.0
			mid_list.append(this_mid)

			sigma2 = ((this_low-this_low_error) - (this_high+this_high_error))**2
			sigma2_list.append(sigma2)
	

			if mid_calc == True:
				if this_mid < mid_divide:
					sublist1.append(this_name)
					bin_1.append(this_mid)
				if this_mid >= mid_divide:
					sublist2.append(this_name)
					bin_2.append(this_mid)

			if high_calc == True:
				if this_high < high_divide:
					sublist1.append(this_name)
					bin_1.append(this_high)
					bin_1_error.append(this_high_error)
				if this_high >= high_divide:
					sublist2.append(this_name)
					bin_2.append(this_high)
                			bin_2_error.append(this_high_error)
	
			if mean_calc == True:
				if this_mean < mean_divide:
                       			sublist1.append(this_name)
                       			bin_1.append(this_mean)
                       			bin_1_error.append(this_mean_error)
                		if this_mean >= mean_divide:
                       			sublist2.append(this_name)
                       			bin_2.append(this_mean)
                       			bin_2_error.append(this_mean_error)

			if low_calc == True:
				if this_low < low_divide:
					sublist1.append(this_name) 
					bin_1.append(this_low)
					bin_1_error.append(this_low_error)
				if this_low >= low_divide:
					sublist2.append(this_name)
					bin_2.append(this_low)
                			bin_2_error.append(this_low_error)

			if bh_calc == True:
				if this_bh < bh_divide:
					sublist1.append(this_name)
                        		bin_1.append(this_bh)
                        		bin_1_error.append(this_bhE)
                		if this_bh >= bh_divide:
                        		sublist2.append(this_name)
                        		bin_2.append(this_bh)
                        		bin_2_error.append(this_bhE)	

			if bol_calc == True:
				if this_bol < bol_divide:
					sublist1.append(this_name)
                        		bin_1.append(this_bol)
                      			bin_1_error.append(0)
                		if this_bol >= bol_divide:
                        		sublist2.append(this_name)
                        		bin_2.append(this_bol)
                        		bin_2_error.append(0)	
		
			if Edd_calc == True:
				if this_edd < ratio_divide:
					sublist1.append(this_name)
                        		bin_1.append(this_edd)
                      			bin_1_error.append(0)
                		if this_edd >= ratio_divide:
                        		sublist2.append(this_name)
                        		bin_2.append(this_edd)
                        		bin_2_error.append(0)	
	

		#get bin1 stats:
		bin_1 = np.array(bin_1)
		bin_1_mean = np.mean(bin_1)
		bin_1_median = np.median(bin_1)
		err_1 = np.mean(bin_1_error)
		min_1 = np.min(bin_1)
		max_1 = np.max(bin_1)

		#get bin2 stats:
		bin_2 = np.array(bin_2)
		bin_2_mean = np.mean(bin_2)
		bin_2_median = np.median(bin_2)
		err_2 = np.mean(bin_2_error)
		min_2 = np.min(bin_2)
		max_2 = np.max(bin_2)


		#print values:
		print
		print "mean bolometric luminosity: " + str(np.mean(ufo_Bol))
		print "median bolometric luminosity: " + str(np.median(ufo_Bol))
		print "mean BH mass: " + str(np.mean(ufo_BH))
		print "median BH mass: " + str(np.median(ufo_BH))
		print "mean Eddington ratio: " + str(np.mean(Edd_list))
		print "median Eddington ratio: " + str(np.median(Edd_list))
		print "power  mean: " + str(np.mean(power_mean_list))
		print "power median: " + str(np.median(power_mean_list))
		print "mean power mid: " + str((np.mean(ufo_power_low - ufo_PLE) + np.mean(ufo_power_high + ufo_PHE))/2.0)
		print "mean power low: " + str(np.mean(ufo_power_low))
		print "mean power high: " + str(np.mean(ufo_power_high))
		print "median power low: " + str(np.median(ufo_power_low))
		print "median power high: " + str(np.median(ufo_power_high))
		print  
		print "sublist 1:"
		print sublist1
		print
		print "sublist 2:"
		print sublist2
		print 
		print "bin 1 mean: " + str(bin_1_mean) + " +/- " + str(err_1)
		print "bin 2 mean: " + str(bin_2_mean) + " +/- " + str(err_2)
		print "bin 1 median: " + str(bin_1_median)
		print "bin 2 median: " + str(bin_2_median) 
		print "bin 1 range: " + str(min_1) + ", " + str(max_1)
		print "bin 2 range: " + str(min_2) + ", " + str(max_2)
		print

		#plot histogram:
		plt_hist = False
		if plt_hist == True:
			fig = plt.figure(figsize=(8,6))
			#plt.hist(power_mean_list,bins=50,range=(41,48),edgecolor="black",facecolor='green',alpha=0.75) #for number of srcs
			plt.hist(ufo_power_low,bins=50,range=(41,45),density=True,edgecolor="black",facecolor='green',alpha=0.75) #for fitting normal 

			#make distribution:
			(mu,sigma) = norm.fit(ufo_power_low)
			xmin, xmax = plt.xlim()
			x = np.linspace(xmin,xmax,100)
			p = norm.pdf(x,mu,sigma)
			plt.plot(x,p,"r--",linewidth=2)

			str1 = "mean: " + str(format(mu,'.2f'))
			str2 = "sigma: " + str(format(sigma,'.2f'))
			plt.annotate(str1,xy=(41,2))
			plt.annotate(str2,xy=(41,1.9))

			print 
			print "Gaussian fit:"
			print "mean: " + str(mu)
			print "sigma: " + str(sigma)
			print 

			plt.title("Minimum Kinetic Power",fontsize=18)
			plt.xlabel("$\dot{E}_{\mathrm{Kin}}$ [$\mathrm{erg \ s^{-1}}$]",fontsize=16)
			#plt.ylabel("Normalized Probability Density",fontsize=16)
			plt.grid(True,ls=":",alpha=0.4)
			plt.savefig("kinetic_power_low_dist.pdf")
			plt.show()
			plt.close()

		#return sublists:
		return sublist1, sublist2
	
	##################################
	#find flux UL
	#Use likelihood profile method
	def get_UL(self,flux_list,array):

		######################
		# 
		# Calculate ULs from the 2D arrays.
		# See get_UL_2 for ULs from the preprocessing step (needed when there is zero signal).
		# This methed is not applicable if TS<1.
		# The default index is set to -2.0. You can change it below.
		#
		# Inputs definitions:
		#
		# flux_list: list of flux values
		#
		# array: 2D array to calculate UL from 
		#
		######################

		#make print statement:
		print
		print "********** Add Stacking Module **********"
		print "Running get_UL..."
		print

		summed_array = array
		flux_list = flux_list

		fig = plt.figure(figsize=(8,6.2))
		ax = plt.gca()

		#calculate for index = 2.0:
		profile = summed_array[10]
		profile =  (np.max(profile)- profile)
		flux_interp = interpolate.interp1d(flux_list,profile,bounds_error=False,kind="linear")

		max_fdist = np.max(profile)

		plt.semilogx(flux_list,profile,ls="",marker="s",label="95% UL")
		plt.semilogx(flux_list,flux_interp(flux_list),ls="--",color="green") #,label="interpolation")

		plt.hlines(2.71,1e-13,1e-9,linestyles="dashdot")
		plt.grid(True,ls=":")
		plt.xlabel("$\gamma$-ray Flux [$\mathrm{ph \ cm^{-2} \ s^{-1}}$]",fontsize=16)
		plt.ylabel("2($\mathrm{logL_{max} - logL}$)",fontsize=16)
		plt.title("Profile Likelihood",fontsize=18)
		plt.legend(loc=2,frameon=False)
		plt.xticks(fontsize=14)
		plt.yticks(fontsize=14)
		ax.tick_params(axis='both',which='major',length=7)
		ax.tick_params(axis='both',which='minor',length=4)
		plt.ylim(0,15)
		plt.savefig("likelihood_profile.png")
		plt.show()
		plt.close()

		#find min of function and corresponding x at min:
		#note: the last entry is the staring point for x, and it needs to be close to the min to converge. 
		print
		print "****************"
		print
		min_x = optimize.fmin(lambda x: flux_interp(x),np.array([1e-10]),disp=True)
			
		lower = 3e-11
		upper = 7e-10
		#error_left = optimize.brenth(lambda x: flux_interp(x)-2.71,lower,min_x[0],xtol=1e-13) # left
		error_right = optimize.brenth(lambda x: flux_interp(x)-2.71,min_x[0],upper,xtol=1e-13) # right
		print
		print "Flux marginal max and error:"
		print "best flux: " + str(min_x[0]) + " ph/cm^2/s"
		#print "Error left: " + str(min_x[0] - error_left) + " ph/cm^2/s"
		print "Error right: " + str(error_right - min_x[0]) + " ph/cm^2/s"
		print "95% Flux UL: " + str(error_right) + " ph/cm^2/s"
		print 	
	
		return 

	def get_UL_2(self,srcname,index,working_directory):

		#####################################
		#
		# Calculate UL from preprocessing step.
		#
		# See get_UL for getting UL from 2D array.
		# 
		# Input definitions:
		#
		# srcname: name of source to calculate UL for.
		#
		# index: index to use for UL calculation. Must give actaul value, either positive or negative. 
		#
		# working_directory: The directory of the run (not the full path). It should be the same for adding, stacking, and preprocessing.
		#
		######################################
		
		#make print statement:
		print
		print "********** Add Stacking Module **********"
		print "Running get_UL_2..."
		print

		#define inputs:
		srcname = srcname
		index = index
		preprocessing_directory = self.preprocessing_path + working_directory + "/" + srcname

		#get current working directory:
                home = os.getcwd()

		#change to working directory:
		os.chdir(preprocessing_directory)

		#define inputs:
		config_file = srcname + ".yaml"
                input_file =  "fit_model_3.npy"

		#correct source names with changed position:
		if srcname == "NGC_4151":
			srcname = "PS J1210.5+3927"
		
		gta = GTAnalysis(config_file)
		gta.load_roi(input_file)
		#gta.free_sources(free=False) #uncomment to fix point sources
		#gta.free_source(srcname,free=False)
		#gta.set_parameter(name=srcname,par="Index",value=index)
		#gta.free_source(srcname,pars="norm")
		#gta.free_source("galdiff",free=True) #uncomment to fix point sources
		#gta.free_source("isodiff",free=True) #uncomment to fix point sources
		fit = gta.fit(optimizer="MINUIT")
		gta.write_roi("get_ul",make_plots=False,save_model_map=False)
		
		fq = fit["fit_quality"]
		fs = fit["fit_status"]
		ll = fit["loglike"]
	
		p = np.load('output/get_ul.npy').flat[0]
		src = p['sources'][srcname]
		Flux_UL = '%.2e' %src['eflux_ul95']
		count_UL = '%.2e' %src['flux_ul95']
		
		print 
		print "source: " + srcname
		print "logL: " + str(ll)
		print "spectral index: " + str(index)
		print "enenrgy flux UL: " + str(Flux_UL) + " MeV/cm^2/s"
		print "photon flux UL: " + str(count_UL) + " ph/cm^2/s"
		print
		
		#return home:
		os.chdir(home)

		return
	
	def JL_bayesian_upper_limit(self,working_directory,srcname):
        	
		##################################################
		#
		# Calculate upper limits using both a bayesian approach and a frequentist approach.
		#
		# The frequentist appraoch uses the profile likelihood method, with 2.71/2 for 95% UL. This is standard in LAT analysis. 
		# However, when there is a physical boundary on a parameter (such as a normalization) the profile likelihood is always restricted 
		# to the physical region such that for a negative MLE the maximum is evaluated at zero.
		# 
		# The frequentist UL calculated here uses FermiTools. It should be the same as the value obtained from get_UL_2 above, 
		# which uses Fermipy, which in turn uses FermiTools. 
		#
		# For low significant sources the bayesian approach may be a better estimate (Thanks to Jean Ballet for pointing this out).
		#
		#################################################        

		#make print statement:
		print
		print "********** Add Stacking Module **********"
		print "JL_bayesian_upper_limit..."
		print
		
		#inputs:
		srcname = srcname
		preprocessing_directory = self.preprocessing_path + working_directory + "/" + srcname

		#get current working directory:
                home = os.getcwd()

		#change to working directory:
		os.chdir(preprocessing_directory)
		
		#Fix source names with new positions:
		if srcname == "NGC_4151":
			srcname = "PS J1210.5+3927"

		#define the likelihood objects for the different PSF classes:
		my_expCube = "/zfs/astrohe/ckarwin/Stacking_Analysis/UFOs/Make_LTCube/Extended_Time_Range_Emin_1GeV_zmax_105/UFOs_binned_ltcube.fits"
		irfs = "P8R3_SOURCE_V2"
		optimizer = "Minuit"
		#optimizer = "DRMNFB"

		my_ExpMap_0 = "output/bexpmap_roi_00.fits" 
		my_src_0 = "output/srcmap_00.fits" 
		my_xml_0 = "output/fit_model_3_00.xml"
		obs_0 = BinnedObs(srcMaps=my_src_0, expCube=my_expCube, binnedExpMap=my_ExpMap_0,irfs=irfs)
		like0 = BinnedAnalysis(obs_0, my_xml_0, optimizer=optimizer)
		
		my_ExpMap_1 = "output/bexpmap_roi_01.fits" 
		my_src_1 = "output/srcmap_01.fits" 
		my_xml_1 = "output/fit_model_3_01.xml"
		obs_1 = BinnedObs(srcMaps=my_src_1, expCube=my_expCube, binnedExpMap=my_ExpMap_1,irfs=irfs)
		like1 = BinnedAnalysis(obs_1, my_xml_1, optimizer=optimizer)
	 		
		my_ExpMap_2 = "output/bexpmap_roi_02.fits" 
		my_src_2 = "output/srcmap_02.fits" 
		my_xml_2 = "output/fit_model_3_02.xml"
		obs_2 = BinnedObs(srcMaps=my_src_2, expCube=my_expCube, binnedExpMap=my_ExpMap_2,irfs=irfs)
		like2 = BinnedAnalysis(obs_2, my_xml_2, optimizer=optimizer)
	
		my_ExpMap_3 = "output/bexpmap_roi_03.fits" 
		my_src_3 = "output/srcmap_03.fits" 
		my_xml_3 = "output/fit_model_3_03.xml"
		obs_3 = BinnedObs(srcMaps=my_src_3, expCube=my_expCube, binnedExpMap=my_ExpMap_3,irfs=irfs)
		like3 = BinnedAnalysis(obs_3, my_xml_3, optimizer=optimizer)
		
		#make the summedlikelihood object:
		summed_like = SummedLikelihood()
		summed_like.addComponent(like0)
		summed_like.addComponent(like1)
		summed_like.addComponent(like2)
		summed_like.addComponent(like3)	

		summedobj=pyLike.Minuit(summed_like.logLike)
	
		#set index=2.0 for UL calculation:
		summed_like.model[srcname].funcs['Spectrum'].getParam('Index').setValue(2.0)
		summed_like.model[srcname].funcs['Spectrum'].getParam('Index').setFree(False)
	
		#perform fit:
		ll = summed_like.fit(verbosity=0,covar=True,optObject=summedobj)
	
		#save outputs:
		like0.logLike.writeXml('output/jount_likelihood_0.xml')
		like1.logLike.writeXml('output/jount_likelihood_1.xml')
		like2.logLike.writeXml('output/jount_likelihood_2.xml')
		like3.logLike.writeXml('output/jount_likelihood_3.xml')
		
		#get convergence details:
		fit_quality = summedobj.getQuality()
		convergence = summedobj.getRetCode()

		#calculate ULs using frequentist approach:
		ul = UpperLimits(summed_like)	
		ul[srcname].compute(emin=1000,emax=800000)	
		
		#convert ul to float:
		this_string = str(ul[srcname].results[0])
		this_string = this_string.split()	
		freq_ul = float(this_string[0])

		print
		print "##########"
		print srcname
		print "-logL: " + str(ll)
		print 
		print "Frequentist 95% UL"
		print ul[srcname].results
		print 

		#calculate bayesian UL:
		#other optional inputs: freeze_all=True; skip_global_opt=True
		bays_ul,results = calc_int(summed_like,srcname,emin=1000, emax=800000,cl = 0.95)
       
        	print
		print "Bayesian 95% ULs:"
		print str(bays_ul) + " ph/cm^2/s" 
		print 

		#return home:
		os.chdir(home)
		
		return freq_ul, bays_ul, fit_quality, convergence 


	##########################################
	#find marginal error of an array:
	def get_marginal_error(self,array,index,flux):

		#make print statement:
		print
		print "######### *ASM* ###########"
		print "Running get_marginal_error..."
		print

		summed_array = array
		index_list = index
		flux_list = flux
		
		##########################
		#find marginal distribution of index:
	
		#clip the array at zero:
		for i in range(0,summed_array.shape[0]):
       			for j in range(0,summed_array.shape[1]):
               			if summed_array[i,j] < 0:
                       			summed_array[i,j] = 0


		#define index list to be positive for optimization
		index_list = [-1*x for x in index_list]

		#marginalize along each axis:
		idist, fdist = margins(summed_array)

		max_idist = np.max(idist)

		#interolate
		index_interp = interpolate.interp1d(index_list,idist.T[0],bounds_error=False)
	
		#invert function to find min:
		def index_dist(x):

			return -1 * index_interp(x)

		#plot marginal distribution:
		fig = plt.figure(figsize=(8,6))
		plt.plot(index_list,idist.T[0],ls="",marker="s",label="marginalized data")
		plt.plot(index_list,index_interp(index_list),ls="--",color="green",label="interpolation")
		plt.grid(True,ls=":")
		plt.xlabel("Photon Index",fontsize=14)
		plt.ylabel("Marginal Distribution",fontsize=14)
		plt.legend(loc=1,frameon=False)
		#plt.savefig("JL3_marginal_index_dist.png")
		plt.show()
		plt.close()

		#find min of function and corresponding x at min.
		#note: the last entry is the staring point for x, and it needs to be close to the min to converge. 
		print 
		print "***************"
		print 

		min_x = optimize.fmin(lambda x: index_dist(x),1, disp=True) 

		#note: the -1 is for 68% confidence level:
		error_left = optimize.brenth(lambda x: index_interp(x)-(max_idist-1),1,min_x) # minus: by substracting 1 to TSmax on the left side of the TS distribution
		error_right = optimize.brenth(lambda x: index_interp(x)-(max_idist-1),min_x,3) # plus: by substracting 1 to TSmax on the right side of the TS distribution

		print
		print "Index marginal max and error:"
		print "best index: " + str(min_x)
		print "Error left: " + str(min_x - error_left)
		print "Error right: " + str(error_right - min_x)

		##################################
		#find marginal distribution of flux

		#max value of fdist:
		max_fdist = np.max(fdist)

		#interolate
		flux_interp = interpolate.interp1d(flux_list,fdist[0],bounds_error=False)

		#invert function to find min:
		def flux_dist(x):
	
			return -1 * flux_interp(x)
	
		#plot marginal distribution:
		fig = plt.figure(figsize=(8,6))
		plt.semilogx(flux_list,fdist[0],ls="",marker="s",label="marginalized data")
		plt.semilogx(flux_list,flux_interp(flux_list),ls="--",color="green",label="interpolation")
		plt.grid(True,ls=":")
		plt.xlabel("$\gamma$-ray Flux [$\mathrm{ph \ cm^{-2} \ s^{-1}}$]",fontsize=14)
		plt.ylabel("Marginal Distribution",fontsize=14)
		plt.legend(loc=2,frameon=False)
		#plt.savefig("JL3_marginal_flux_dist.png")
		plt.show()
		plt.close()

		#find min of function and corresponding x at min:
		#note: the last entry is the staring point for x, and it needs to be close to the min to converge. 
		print
		print "****************"
		print
		min_x = optimize.fmin(lambda x: flux_dist(x),np.array([1e-11]),disp=True)

		#note: the -1 is for 68% confidence level:
		error_left = optimize.brenth(lambda x: flux_interp(x)-(max_fdist-1),1e-11,min_x,xtol=1e-13) # minus: by substracting 1 to TSmax on the left side of the TS distribution
		error_right = optimize.brenth(lambda x: flux_interp(x)-(max_fdist-1),min_x,4e-10,xtol=1e-13) # plus: by substracting 1 to TSmax on the right side of the TS distribution

		print
		print "Flux marginal max and error:"
		print "best flux: " + str(min_x)
		print "Error left: " + str(min_x - error_left)
		print "Error right: " + str(error_right - min_x)

		return

	def interpolate_array(self):

		################################################
		#
		# Allows you to interpolate array in order to stack in different parameters.
		#
		#################################################

		#make print statement:
		print
		print "********** Add Stacking Module **********"
		print "Running interpolate_array..."
		print
		
		#########################
                #upload parameters:
                this_file = self.data_path + "LLAGN_Sample_Master.fits"
                hdu = fits.open(this_file)
                data = hdu[1].data
                name_list = data["name"]
                d_list = data["distance[Mpc]"]
	
                total_array = np.zeros(shape=(31,40))
                Range = []

                #iterate through sources:
		for s in range(0,len(name_list)):

			flux_list = np.linspace(-13,-9,num=40,endpoint=True) #for luminosity stacking

			for j in range(0,len(flux_list)):
				flux_list[j] = 10**flux_list[j]

			index_list = [-1.0,-1.1,-1.2,-1.3,-1.4,-1.5,-1.6,-1.7,-1.8,-1.9,-2.0,-2.1,-2.2,-2.3,-2.4,-2.5,-2.6,-2.7,-2.8,-2.9,-3.0,-3.1,-3.2,-3.3,-3.4,-3.5,-3.6,-3.7,-3.8,-3.9,-4.0]
			index_list = np.array(index_list)
			
			#load array:
			this_name = name_list[s]
			this_d = d_list[s]
                        this_d = this_d * 3.086e24 #convert Mpc to cm
			
			this_file = "Numpy_Arrays/Individual_Sources/" + this_name + "_array.npy"
			array = np.load(this_file)
			
			########################	
			# convert array:
			#
			
			lum_range = np.linspace(38,42,num=40,endpoint=True)
                        for k in range(0,len(lum_range)):
                            lum_range[k] = 10**lum_range[k]	
			
			this_array = np.zeros(shape=(len(index_list),40))
			for y in range(0,len(index_list)):
				
				this_index = -1*index_list[y]
									
				lum_list = [] 
				for x in range(0,len(flux_list)):
			
					this_flux = flux_list[x]
					
                                        if this_index in [1.0,2.0,3.0,4.0]:
                                            this_index = this_index + 0.0001

					ergflux = PS.GetErgFlux(this_flux,this_index,1000,800000)
                                        lum = ergflux*4*math.pi*(this_d**2)
					lum_list.append(lum)
		
				#interpolate function:
				f = interpolate.interp1d(lum_list,array[y],kind="linear",bounds_error=False,fill_value="extrapolate")
				
                                #add row to to source array for given luminosity range:
				this_row = f(lum_range)
                                this_array[y] = this_row
                                
                                for each in lum_list:
                                    Range.append(each)	
	                
                        #save individual arrays:
			np.save("Numpy_Arrays/Individual_Sources/Luminosity_Arrays/" + this_name + "_lum_array",this_array)

                        #plot for diagnostics:
                        max_value = np.amax(this_array)
                        ax = plt.gca()
			img = ax.pcolormesh(lum_range,index_list,this_array,cmap="inferno",vmin=0,vmax=max_value)
			ax.set_xscale('log')
			y_ticks = [-1.0,-1.2,-1.4,-1.6,-1.8,-2.0,-2.2,-2.4,-2.6,-2.8,-3.0,-3.2,-3.4,-3.6,-3.8,-4.0]
			ax.set_yticks(y_ticks)
			plt.xticks(fontsize=16)
			plt.yticks(fontsize=16)
                        cbar = plt.colorbar(img,fraction=0.045)
                        plt.savefig("Images/Luminosity/" + this_name + ".png")
                        plt.close()
                        #plt.show()

                        total_array += this_array

                #save individual arrays:
                np.save("Numpy_Arrays/summed_array_Run_4_luminosity",total_array)
                
                #plot hist to find range:
                #logbins = np.logspace(34,45,90)
                #plt.hist(Range, bins=logbins,log=True)
                #plt.xscale('log')
                #plt.show()

		return

	def interpolate_array_alpha_beta(self,index_num):

		################################################
		#
		# Allows you to interpolate array in order to stack in alpha-beta.
		#
                # index_num: spectral index, used to interpolate array and convert flux to luminosity.
                #
		#################################################

		#make print statement:
		print
		print "********** Add Stacking Module **********"
		print "Running interpolate_array_alpha_beta..."
		print
		
		#########################
                #upload parameters:
                this_file = self.data_path + "LLAGN_Sample_Master.fits"
                hdu = fits.open(this_file)
                data = hdu[1].data
                name_list = data["name_1"]
                d_list = data["distance[Mpc]"]
	
                #for 15 GHz:
                Saikai_l_core = data["Saikai_L_peak_erg_s"]

                Nagar_ul_stat = data["Nagar_ULstat_15GHz"]
                Nagar_l_core = data["Nagar_LogLpeak_15GHz_erg_s"]

                detected_list = []
                ul_list = []
                total_list = []
                test_list = []
                test_list_counter = []
                problem_list = []
                #note: NGC_5970 and NGC_5982 have no radio data and so are given L15=0. (remove from stack!)

                for i in range(0,len(name_list)):
                    if Saikai_l_core[i] > 0:
                        detected_list.append(name_list[i])
                        total_list.append(Saikai_l_core[i])
                    if (Saikai_l_core[i] == 0):
                        ul_list.append(name_list[i])
                        total_list.append(Nagar_l_core[i])

                total_list = np.array(total_list)

                #for using fp as proxy for L15:
                OIII_lum = data["OIII_lum(erg/s)"]
                M_BH = data["log(BHmass/M_Sun)"]

                fp = 0.88*np.log10(OIII_lum) + 0.88*M_BH - 3.78 #from Saikai+18
                #fp = np.log10(OIII_lum) + M_BH
                good_fp_index = (OIII_lum > 0) & (M_BH > 0) & (~np.isnan(fp)) & (~np.isinf(fp))
                run_list = name_list[good_fp_index]

                #define flux list:
		flux_list = np.linspace(-13,-9,num=40,endpoint=True)
                for j in range(0,len(flux_list)):
		    flux_list[j] = 10**flux_list[j]
        
                #define index list:
                index_list = -1*np.arange(1,4.1,0.1)
                
                #define main alpha beta ranges:
                alpha_range = np.arange(0.1,1.7,0.1)
		beta_range = np.arange(37,40.1,0.1)
                #index_num = 6 #best-fit index from flux stack
                this_index = -1*index_list[index_num]
                
                #define total array:
                total_array = np.zeros(shape=(len(beta_range),len(alpha_range)))
                alpha_max_list = []
                alpha_min_list = []
                counter = 0

                #iterate through sources:
		for s in range(0,len(name_list)):

			#load array:
			this_name = name_list[s]
			this_d = d_list[s]
                        this_d = this_d * 3.086e24 #convert Mpc to cm
			this_L15 = total_list[s] #for VLA L15
                        #this_L15 = np.log10(OIII_lum[s]/10**38.4) #for OIII

                        #for fundamental plane:
                        this_L15 = fp[s]  
                        if (np.isnan(this_L15)) | (np.isinf(this_L15)):
                            continue 
                        
                        this_L15 = math.log10((10**this_L15)/(10**37)) #need to normalize the arguement!

			this_file = "Numpy_Arrays/Individual_Sources/" + this_name + "_array.npy"
			array = np.load(this_file)
			
			########################	
			# convert array:
			#
			this_array = np.zeros(shape=(len(beta_range),len(alpha_range)))
			for y in range(0,len(beta_range)):
				
                                this_beta = beta_range[y]
				alpha_list = [] 
				for x in range(0,len(flux_list)):
			
					this_flux = flux_list[x]
                                        ergflux = PS.GetErgFlux(this_flux,this_index,1000,800000)
                                        lum = ergflux*4*math.pi*(this_d**2)
                                        this_alpha = (np.log10(lum) - this_beta)/this_L15
                                        alpha_list.append(this_alpha)
                                        if this_L15 != 0:
                                            alpha_max_list.append(max(alpha_list))
                                            alpha_min_list.append(min(alpha_list))

				#interpolate function:
				f = interpolate.interp1d(alpha_list,array[index_num],kind="linear",bounds_error=False,fill_value="extrapolate")
				
                                #add row to to source array for given luminosity range:
				this_row = f(alpha_range)
                                this_array[y] = this_row
	                
                        #save individual arrays:
			np.save("Numpy_Arrays/Individual_Sources/Alpha_Beta_Arrays/" + this_name + "_alpha_beta_array",this_array)

                        #plot for diagnostics:
                        max_value = np.amax(this_array)
                        min_value = np.amin(this_array)
                        plot_each = False
                        if plot_each == True:
                            ax = plt.gca()
		            img = ax.pcolormesh(alpha_range,beta_range,this_array,cmap="inferno",vmin=min_value,vmax=max_value)
			    plt.xticks(fontsize=16)
			    plt.yticks(fontsize=16)
                            cbar = plt.colorbar(img,fraction=0.045)
                            plt.savefig("Images/Alpha_Beta/" + this_name + ".png")
                            plt.show()
                            plt.close()
                        
                        if (this_name not in self.exclusion_list) & (this_name not in ["NGC_3031"]):
                            counter += 1
                            total_array += this_array
                            test_list.append(np.amax(total_array))
                            test_list_counter.append(counter)
                            if np.amax(this_array) <= -1:
                                problem_list.append([this_name,np.amax(this_array)])
                
                print "TESTING************************************"
                print test_list
                print problem_list
                plt.plot(test_list_counter,test_list)
                plt.xlabel("number of srcs in array")
                plt.ylabel("max TS of summed array")
                plt.show()
                plt.close()

                #save individual arrays:
                np.save("Numpy_Arrays/summed_array_Run_4_alpha_beta",total_array)
                    
                max_value = np.amax(total_array)
                min_value = np.amin(total_array)
                num_pars = 3
                sigma = stats.norm.ppf(1.-stats.distributions.chi2.sf(max_value,num_pars)/2.)
                print 
                print "total max: " + str(max_value)
                print "index: " + str(this_index)
                print 
                print "sigma: " + str(sigma)
                print "length of total array: " + str(counter)
                print
                
                #plot total:
                plot_total = True
                if plot_total == True:
                    ax = plt.gca()
                
                    #transpose array to put alpha on y-axis:
                    total_array = total_array.T

                    #method 1:
                    img = ax.pcolormesh(beta_range,alpha_range,total_array,cmap="inferno",vmin=0,vmax=max_value)
                   
                    #method 2:   
		    #clip the array at zero for visualization purposes:
		    #for i in range(0,total_array.shape[0]):
		    #    for j in range(0,total_array.shape[1]):
		    #        if total_array[i,j] < 0:
		    # 	        total_array[i,j] = 0
                    #img = ax.contourf(beta_range,alpha_range,total_array,100,cmap="inferno")
		
		    #significane contours for dof=2:
		    first = max_value - 2.3 #0.68 level
		    second = max_value - 4.61 #0.90 level
		    third =  max_value - 9.21 #0.99 level

		    #find indices for max values:
		    ind = np.unravel_index(np.argmax(total_array,axis=None),total_array.shape)
		    best_alpha_value = ind[0]
		    best_beta_value = ind[1]

                    best_alpha = alpha_range[ind[0]]
                    best_beta = beta_range[ind[1]]
                    
                    plt.contour(beta_range,alpha_range,total_array,levels = (third,second,first),colors='black',linestyles=["-.",'--',"-"], alpha=1,linewidth=4.0)
		    plt.plot(best_beta,best_alpha,marker="+",ms=12,color="black")

                    cbar = plt.colorbar(img,fraction=0.045)
                    plt.xlabel("Beta")
                    plt.ylabel("Alpha")
                    ax.set_aspect('auto')
                    plt.savefig("Images/alpha_beta_interp_index_2p1.png")
                    plt.show()
                    plt.close()
                
                    #plot hist to find alpha range:
                    plt.hist(alpha_max_list,histtype="step",label="max")
                    plt.hist(alpha_min_list,histtype="step",label="min")
                    plt.xlabel("alpha")
                    plt.legend(loc=1,frameon=False)
                    plt.show()

		return max_value


        def power_law_2(self,N,gamma,E,Emin,Emax):

            """ dN/dE in units of ph/cm^s/s/MeV.
                Inputs:
                N: Integrated flux between Emin and Emax in ph/cm^2/s.
                gamma: Spectral index.
                E: Energy range in MeV. Should be array.
                Emin, Emax: Min and max energy, respectively, in MeV. 
            """
            
            return N*(gamma+1)*(E**gamma) / (Emax**(gamma+1) - Emin**(gamma+1))
        
        def make_butterfly(self,input_array,name,Emin,Emax,numbins):
           
            """ Calculate butterfly plot.
                Inputs:
                input array: input numpy array file from stack.
                name: name to use for output files.
                Emin: min energy in MeV.
                Emax: max energy in MeV.
                numbins: number of energy bins to use for butterfly plot.
            """
            
            conv = 1.60218e-6 # MeV to erg
            
            image_output = "Images/" + name + "_sed.pdf"
            data_output = "Output_Data/" + name + "_butterfly.dat"

            # Define energy range and binning for butterfly plot:
            E_range = np.logspace(np.log10(Emin),np.log10(Emax),numbins) 

            # Define flux and index.
            # Must be the same that was used to make the stacked array. 
            flux_list = np.linspace(-13,-9,num=40,endpoint=True)
            flux_list = 10**flux_list
            index_list = np.arange(1,4.1,0.1)

            # Load stacked array:
            this_array = np.load(input_array)
           
            print
            print "Stacked array:"
            print this_array.shape
            print this_array
            print

	    #find indices for max values:
	    ind = np.unravel_index(np.argmax(this_array,axis=None),this_array.shape)
            best_index = index_list[ind[0]]
            best_flux = flux_list[ind[1]]

            # Get max and significane contours for dof=2:
            max_value = np.amax(this_array)
            first = max_value - 2.3 #0.68 level
            second = max_value - 4.61 #0.90 level
            third =  max_value - 9.21 #0.99 level

            # Get indices within 1sigma contour:
            contour = np.where(this_array>=first)
         
            # Test Method 1:
            fig = plt.figure(figsize=(8,6))
            ax = plt.gca()
            plt.contour(flux_list,index_list,this_array,levels = (third,second,first),colors='black',linestyles=["-.",'--',"-"], alpha=1,linewidth=2*4.0)
            #this_array[contour] = 0
	    img = ax.pcolormesh(flux_list,index_list,this_array,cmap="inferno",vmin=0,vmax=max_value)
	    ax.set_xscale('log')
            plt.xlabel("Flux [$\mathrm{ph \ cm^{-2} \ s^{-1}}$]",fontsize=12)
            plt.ylabel("Index", fontsize=12)
            plt.show()
            plt.close()
        
            # Setup figure:
            fig = plt.figure(figsize=(8,6))
            ax = plt.gca()

            # Plot solutions within 1 sigma contour (sanity check):
            x = contour[1]
            y = contour[0]
            for i in range(0,len(x)):
                this_N = flux_list[x[i]]
                this_gamma = index_list[y[i]]*-1
                dnde = self.power_law_2(this_N,this_gamma,E_range,Emin,Emax)
                #plt.loglog(E_range,conv*E_range**2 * dnde,color="red")
            
            # Interpolate array for plotting:
            x = flux_list
            y = index_list
            z = this_array
            f = interpolate.interp2d(x, y, z, kind='linear')

            # Use finer binning to fill out butterfly plot:
            plot_flux_list = np.linspace(-13,-9,num=200,endpoint=True)
            plot_flux_list = 10**plot_flux_list
            plot_index_list = np.arange(1,4.1,0.003)

            # Plot best-fit:
            this_N = best_flux
            this_gamma = best_index*-1
            dnde = self.power_law_2(this_N,this_gamma,E_range,Emin,Emax)
            plt.loglog(E_range,conv*E_range**2 * dnde,color="black",lw=2,alpha=0.7,zorder=1)
            best_flux = conv*E_range**2 * dnde

            # Plot butterfly:
            plot_list = []
            for each in plot_flux_list:
                for every in plot_index_list:
                    
                    this_flux = each
                    this_index = every
                    this_TS = f(this_flux,this_index)
                    
                    if this_TS >= first:
                        this_N = each
                        this_gamma = every*-1
                        dnde = self.power_law_2(this_N,this_gamma,E_range,Emin,Emax)
                        plt.loglog(E_range,conv*E_range**2 * dnde,color="grey",alpha=0.3,zorder=0)
                        plot_list.append(conv*E_range**2 * dnde)

            plt.title("NGC 4374",fontsize=12,y=0.90,x=0.9)
            plt.ylabel(r'$\mathrm{E^2 dN/dE \ [erg \ cm^{-2} \ s^{-1}]}$',fontsize=12)
            plt.xlabel('Energy [MeV]',fontsize=12) #for flux
            ax.tick_params(axis='both',which='major',length=9)
            ax.tick_params(axis='both',which='minor',length=5)
            plt.xticks(fontsize=12)                        
            plt.yticks(fontsize=12)
            plt.ylim(5e-16,5e-11)
            plt.savefig(image_output,bbox_inches='tight')
            plt.show()
            plt.close()

            # Write butterfly to data using max and min values: 
            plot_list = np.array(plot_list)
            plot_list = plot_list.T
            min_list = []
            max_list = []
            for each in plot_list:
                this_min = min(each)
                this_max = max(each)
                min_list.append(this_min)
                max_list.append(this_max)
            d = {"Energy[MeV]":E_range,"Flux[erg/cm^2/s]":best_flux,"Flux_min[erg/cm^2/s]":min_list,"Flux_max[erg/cm^2/s]":max_list}
            df = pd.DataFrame(data=d,columns = ["Energy[MeV]","Flux[erg/cm^2/s]","Flux_min[erg/cm^2/s]","Flux_max[erg/cm^2/s]"])
            df.to_csv(data_output,float_format='%10.5e', sep="\t",index=False)

            return

	def evolution_plot(self):

		################################################
		#
		# Allows you to plot max TS as a funtion of source.
		#
		#################################################

		#make print statement:
		print
		print "********** Add Stacking Module **********"
		print "Running evolution_plot..."
		print

                name_file = "/zfs/astrohe/ckarwin/Stacking_Analysis/LLAGN/Preprocessed_Sources/Run_4/preprocessing_summary.txt"
		df = pd.read_csv(name_file,delim_whitespace=True,skiprows=[0,1,2,3,197,198,199])
                name_list = df["name"]
                name_list = name_list
                ts_list = df["TS"]
    
                #exclude sources:
                exclude_list = ["J1225.2+1251","J1210.4+3927","NGC_676","NGC_3516","NGC_4698","NGC_6503"]
                keep_index = ~np.isin(name_list,exclude_list)
                name_list = name_list[keep_index].tolist()
                ts_list = ts_list[keep_index].tolist()

                index_scan = np.arange(1,4.1,0.1)
                flux_scan = np.linspace(-13,-9,num=41,endpoint=True)
                flux_scan = 10**flux_scan

                max_list = []
                index_list = []
                flux_list = []
                name_plot_list = []
                for s in range(0,len(name_list)):
                        index = len(name_list) - s - 1
                        #index = s

			#load array:
			this_name = name_list[index]
			plot_name = this_name		
		        
			this_file = "Numpy_Arrays/Individual_Sources/" + this_name + "_array.npy"
			 
                        this_array = np.load(this_file)
                        name_plot_list.append(this_name)
                
			#add array
                        if s == 0:
                            total_array = this_array
                        if s > 0:
			    total_array = total_array + this_array
	
			#get best-fit values:
			max_value = np.amax(total_array)
			
			ind = np.unravel_index(np.argmax(total_array,axis=None),total_array.shape)
			best_index = ind[0]
                	best_flux = ind[1]
	
			max_list.append(max_value)
                        index_list.append(index_scan[best_index])
                        flux_list.append(flux_scan[best_flux])


		print 
		print "number of stacked sources: " + str(len(max_list))
		print 
		
		#setup figure:
		fig = plt.figure(figsize=(8,6))
		ax = plt.gca()
		#ax.set_facecolor('black')
		
		plot_range = np.arange(0,len(name_plot_list),1)
		
                plt.plot(plot_range,max_list,marker='s',ls="--",ms=8,color="black",label="Max TS (for stack)")
		

		plt.grid(color="grey",ls="-",alpha=0.5)
                plt.yticks(fontsize=12)
                plt.xticks(fontsize=12)

                #uncomment to use source names for x axis:
                #ax.set_xticks(plot_range)
		#ax.set_xticklabels(ts_list,rotation=45,fontsize=12)
                #ax.set_xticklabels(name_list,rotation=45,fontsize=12)

		ax.tick_params(axis='both',which='major',length=9)
               	ax.tick_params(axis='both',which='minor',length=5)
		#plt.title("Evolution of Stack",fontsize=14)
		plt.xlabel("Number of Stacked Sources (TS ranked)", fontsize=14)
		plt.ylabel("Max TS",fontsize=14,color="black")
                ax.tick_params(axis='y',labelcolor="black")
		#plt.legend(loc=2,frameon=True)
		plt.xlim(0,190)
		#plt.ylim(-0.5,0.5)		

		#plot second twin axis:
		#ax2 = ax.twinx()
		
		#ax2.plot(plot_range,sn,marker='^',ls="-",ms=10,color="cornflowerblue",label="best-fit flux (for stack)")
		#ax2.plot(plot_range,best_index_list,marker='^',ls="-",ms=10,color="blue",label="Spectral Index")
		
		#ax2.tick_params(axis='y',labelcolor="cornflowerblue")
	    
		#ax2.set_yscale('log')
		#plt.ylim(5e-5,5e-3)
		#plt.ylabel('Individual Background Counts',fontsize=16,color="cornflowerblue")
		#plt.ylabel("flux [$\mathrm{ph \ cm^{-2} \ s^{-1}}$]",fontsize=16,color="cornflowerblue")
		#plt.yticks(fontsize=12)
		plt.tight_layout()
	        #ax2.tick_params(axis='both',which='major',length=9)
                #ax2.tick_params(axis='both',which='minor',length=5)
		
		plt.savefig("Images/TS_evolution_full.pdf")
		plt.show()	

		return
    

###################################
#The standard analysis class.
#Inherets the joint likelihood class.
class standard_analysis(joint_likelihood):

	#####################################
        #combine profiles to a summed array:
	def combine_likelihood(self, savefile, working_directory, likelihood_directory, bin_stacking_input, make_array_image):
	
		####################
		#
		# Input definitions:
		#
		# savefile: Prefix of array to be saved. Do not include ".npy" at the end of the name; it's already included.
		#
		# working_directory: The directory of the run (not the full path). It should be the same for adding, stacking, and preprocessing.
		#
		# likelihood_directory: The directory containing the null likelihood.
		#
		# bin_stacking_input: Whether or not to stack in bins. Needs to be a list of size 2. First element is a boolean; second element is which bin to add. 
		#
		# make_array_image: Whether or not to make an array image of all TS profiles. Needs to be a list of size 3. 
		# First element is a boolean; second element is number of rows for image; third element is number of columns for image.		
		#
		####################

		###########
		print
		print "***********************"
		print "Making stack..."
		print
		
		#get current working directory:
		home = os.getcwd()

		#specify working directory:
		working_directory = str(working_directory)

		#specify output file:
		savefile = savefile

		#whether or not to stack in bins:
		bin_stacking = bin_stacking_input[0]
		this_sublist = bin_stacking_input[1]

		#whether or not to make array image:
		make_array_image_switch = make_array_image[0]
		rows = make_array_image[1]
		columns = make_array_image[2]

		#write save directories:
		if os.path.exists("Numpy_Arrays") == False:
			os.system("mkdir Numpy_Arrays")

		#perform stacking in bins:
		if bin_stacking == True:
			sublist1, sublist2 = self.make_bins() 
			if this_sublist == 1:
				sublist = sublist1
			if this_sublist == 2:
				sublist = sublist2
		if bin_stacking == False:
			sublist = self.name_list
		
		#make an array image of TS profiles for each source
		if make_array_image_switch == True:
			#setup benchmark figure:
			fig = plt.figure(figsize=(18,22))
			columns = columns
			rows = rows
	
		#make stack:

		#define counters:
		number_srcs = 0
		counter = 0
		plot_counter = -1

		#define lists:
		print_list = []
		vlist_keep = []
		zlist_keep = []
		max_TS_list = []

		#iterate through sources:
		for s in range(0,len(self.name_list)):
			
			srcname = self.name_list[s]
			plot_counter += 1

			likelihood_dir = self.preprocessing_path + "%s/%s/output/null_likelihood.txt" %(likelihood_directory,srcname)
			stacking_dir = self.stacking_path + "%s/%s" %(working_directory,srcname)
	
			if os.path.exists(stacking_dir) == False or os.path.exists(likelihood_dir) == False:
				print 
				print 'Does not exist: ' + srcname
				print 

			#here you can specify what you want to stack:
			if srcname not in self.exclusion_list and os.path.exists(likelihood_dir) == True and os.path.exists(stacking_dir) == True:
				
				os.chdir(stacking_dir)
	
				print_list.append(srcname)
				
				number_srcs += 1
	
				array_list = []

				index_list = [1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.3,3.4,3.5]

				f = open(likelihood_dir,'r')
				lines = f.readlines()
				null = float(lines[0])

				for i in range(0,len(index_list)):
					this_index = str(index_list[i])
					this_file = "%s_stacking_LLAGN_%s.txt" %(srcname,this_index)

					df = pd.read_csv(this_file,delim_whitespace=True,names=["flux","index","likelihood","quality","status"])

					flux = df["flux"]
					index = df["index"]
					likelihood = df["likelihood"].tolist()
					TS = 2*(df["likelihood"]-null)
					TS = TS.tolist()
					array_list.append(TS)

				final_array = np.array(array_list)
	
				#this_max_TS = final_array[11][26]	
				this_max_TS = np.max(final_array)
				max_TS_list.append(this_max_TS)
	
				#save each individual source array:
                		source_array_file = self.add_stacking_path + "/%s/Numpy_Arrays/Individual_Sources/" % working_directory
                		if os.path.exists(source_array_file) == False:
                        		os.system("mkdir %s" % source_array_file)
                		source_array_file += str(srcname) + "_array"
                		np.save(source_array_file,final_array)

				if counter == 0:
					summed_array = final_array
				if counter > 0:
					summed_array = np.add(summed_array,final_array)
				counter += 1

				if make_array_image_switch == True:
					
					#######################
					#plot 
	        			#setup figure:
                			fig.add_subplot(rows,columns,counter)
                			ax = plt.gca()

					#this is here for now to fix last column of plot:
					new_col = final_array.sum(1)[...,None]
					for i in range(0,new_col.shape[0]):
        					new_col[i] = 0
                			final_array = np.append(final_array,new_col,axis=1)

					ind = np.unravel_index(np.argmax(final_array,axis=None),final_array.shape)                

					max_value = np.amax(final_array)
                			min_value = np.amin(final_array)

					if max_value<1:
                				max_value = 1
	
					index_list = [-1*x for x in index_list]
					best_index = index_list[ind[0]]                
					
					flux_list = np.linspace(-13,-9,num=41,endpoint=True) #for flux stacking
                			#flux_list = np.linspace(39,43,num=41,endpoint=True) #for luminosity stacking
					for i in range(0,len(flux_list)):
                        			flux_list[i] = 10**flux_list[i]
					best_flux = flux_list[ind[1]]		

					img = ax.pcolormesh(flux_list,index_list,final_array,cmap="inferno",vmin=0,vmax=max_value)
					plt.plot(best_flux,best_index,marker="+",ms=12,color="black")               
 
					ax.set_xscale('log')
                			y_ticks = [-1.0,-1.2,-1.4,-1.6,-1.8,-2.0,-2.2,-2.4,-2.6,-2.8,-3.0,-3.2]
                			ax.set_yticks(y_ticks)
                			plt.xticks(fontsize=16)
                			plt.yticks(fontsize=16)

					#plot colorbar
                			cbar = plt.colorbar(img,fraction=0.045)
                			cbar.ax.tick_params(labelsize=14)

                			plt.title(srcname,fontsize=22,fontweight='bold',y=1.04)
                			plt.ylabel('Photon Index',fontsize=16)
                			plt.xlabel(r'$\mathregular{\gamma}$-Ray Flux [ph $\mathregular{\ cm^{-2} \ s^{-1}}$]',fontsize=16) #for flux stacking
					#plt.xlabel(r'$\mathregular{\gamma}$-Ray Luminosity [erg s$\mathregular{^{-1}}$]',fontsize=16) #for luminosity stacking

                			ax.set_aspect('auto') #set aspect ration to make square image (aspect = smaller_axis_bins/larger_axis_bins, or vice versa depending on layout)
                			ax.tick_params(axis='both',which='major',length=9)
                			ax.tick_params(axis='both',which='minor',length=5)
	
		#save image:
		if make_array_image_switch == True:
			plt.tight_layout()
			savefig = self.add_stacking_path + "%s/Images/" % working_directory
			if os.path.exists(savefig) == False:
                        	os.system("mkdir %s" % savefig)
			plt.savefig(savefig + "TS_profiles.png")
			plt.show()
			plt.close()
			
		print
		print "sources that were added in the sum:"
		print "number of sources: " + str(number_srcs)
		print print_list
		print 

		array_file = self.add_stacking_path + "%s/Numpy_Arrays/" % working_directory
		if os.path.exists(array_file) == False:
                	os.system("mkdir %s" % array_file)
		array_file += savefile
		np.save(array_file,summed_array)
	
		#return to home:
		os.chdir(home)
		
		return 	
