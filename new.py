# PROGRAM : BLUR AND BRIGHT SPOT DETECTION
# AUTH- SALIL PARIHAR

########## commands for installing dependencies ##################

# sudo apt-get install python-opencv
# pip install imutils

############### command for executing code #############################################
# 'images' is a folder name 

# python new.py -i images   



#LIBRARIES
import cv2
import argparse
from imutils import paths

#ARGPARSE FOR COMMOND-LINE INTERFACES ( * give folder name throug commond line )
ap = argparse.ArgumentParser()
ap.add_argument("-i", required=True , help="nhi chahiye ")
ap.add_argument("-t", type=float, default=250.0, help="nhi chahiye")

args = vars(ap.parse_args())

#READING ALL IMAGES
for imagePath in paths.list_images(args["i"]):

	image = cv2.imread(imagePath)

	#CONVERTING IN TO GRAY-SCALE IMAGE
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#cv2.imshow("Image111", gray)


	#APPLYNG BINARY THRESHOLDING FOR BRIGHT SPOT
	bi = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)[1]
	#cv2.imshow("Image1", bi)


	#CONVERTING IN TO LAPLACIAN IMAGE FOR EDGE DETECTION
	lap = cv2.Laplacian(gray, cv2.CV_64F)
	#cv2.imshow("Image1111", lap)


	################################ gaussian blur ###################################
	#grayyy = cv2.GaussianBlur(gray, 0)
	
	#FINDING THE MAXIMUM INTENSITY OF THE IMAGE
	(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
	print(maxVal)
	#print(maxLoc)
	#print(minVal)
	#print(minLoc)
	print(bi.var())



	################################### canny ################################
	#edge= cv2.Canny(image,100,100)
	#cv2.imshow("canny", edge)


	###################################################################


	text = "Not Blurry"
	spot= "No Bright Spot"

	#CONDITION : VARIANCE OF LAPLACIAN MATRIX
	if lap.var() < args["t"]:
		text = "Blurry"

	#CONDITION : VARIANCE OF BINARY MATRIX
	if (bi.var()>5000 and bi.var()<8500) :
		spot= "Bright Spot"

	# show the image
	#cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
	cv2.putText(image, "{} ".format(text ), (15, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

	cv2.putText(image, "{}: ".format(spot), (15, 75),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)

	cv2.imshow("Image", image)
	key = cv2.waitKey(0)
















