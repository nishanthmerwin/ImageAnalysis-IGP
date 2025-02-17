

## This script will act as a wrapper forr individual functions


import numpy as np
import scipy as sp

from functions.convertToArray import convertToArray


# wrapper function accepts a location for an image file
def	wrapperIGLCM(image,thresholdAuto,thresholdManualValue,thresholdFilter,nhoodSize){
	
	# This function loads the image as a numpy array. Outputs numpy array. Then greyscale
	image = covertToArray(image)
	image = greyscale(image)
	
	
	
	# Applies a filter
	if(thresholdFilter){
		image = thresholdFilterFunction(thresholdFilter) 
	}
	
	
	# Option for automated thresholding or pick your own thresholding value
	# Outputted image will have true greyscale values for selected areas, and values of 0 if thresholded out.
	if(thresholdAuto==True){
		image thresholdAutoFunction(image) 
	}
	else(thresholdAuto=False){
		image = thresholdManualFunction(image,thresholdManualValue)
	}
	
	
	# Generating the co-occurance Matrix
	image = IGLCM_fuction(image,nhoodSize)	
	
	# Save the IGLCM name should be the same as before numpy.save (".npy")
	saveIGLCM(image)
} 


# Accepts multiple cooccurance matrices (coMat is a list of file.npy locations) (WOOT FINISHED)
def haralick(coMat){

	haralickOut = ["ImageLocation","ASM","Contrast","IDM","entropy","xmean","ymean","xstdev","ystdev","CORR","mean","variance","xPlusY","sumAverage","sumEntropy","difEntropy","inertia","clusterShade","clusterProm"]
	for i in coMat{	
		IGLCM <- np.load(i)
		# Function to apply ALL the haralick features on a single IGLCM
		# Returns array of haralick values
		hVals = haralickALL(IGLCM)
		row = [i,hVals]
		haralickOut = vstack(haralickOut,row)
	}
	
	# Function to format according to Cell Profiler Analyst (This will be in a different module), CP has a module for this.
	# haralickOut = formatCPAFUN(haralickOut)
	
	return(haralickOut)
}










