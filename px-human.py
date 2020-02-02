'''
This code is created by Anilcan Bulut for fun.
It returns you a pixeled image of the provided input image.
There are some parameters like kernel size, image height and width.

Kernel size: It should be an odd number like 3,5,7... 
Image dimentions: Both height and width should be dividable by kernel size. 


Algorithm: We create a kernel at first. Let say 3 by 3. Then we find the center pixel of the kernel,
and create a new square that has smaller dimension than the original one. 

After creating the square that contains center pixels with some for loops, we take only the center
pixel coordinates and their corresponding pixel value. 

At the end, we loop through the original image and find which region of the image the current
pixel coordinate is. Then give the center pixel's pixel value to the current pixel.

Have fun with the code. It's slow I know, maybe I can change the algorithm to make it fast in the future.

'''

import cv2
import numpy as np
import argparse

#argument parser is for cmd usage.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="image path")
ap.add_argument("-k", "--kernel", required=True, help="kernel size")
ap.add_argument("-a", "--height", required=True, help="height of image")
ap.add_argument("-b", "--width", required=True, help="width of image")
args = vars(ap.parse_args())

IMG_HEIGHT, IMG_WIDTH = int(args["height"]), int(args["width"])

img = cv2.imread(args["image"])
img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH))

arr = []
center_coords = []

kernel_size = int(args["kernel"])
kernel_width = (kernel_size - 1)/2

if((IMG_HEIGHT % kernel_size) != 0) or ((IMG_WIDTH % kernel_size) != 0):
	print("kernel size is wrong!")
else:

	#create the center_px square which is img_size - 2*width
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			if((i >= kernel_width) and (i < (img.shape[0] - kernel_width))) and ((j >= kernel_width) and (j < (img.shape[1] - kernel_width))):

				arr.append((img[i][j] , [i, j]))

	length = int(len(arr)/(img.shape[0] - 2*kernel_width))

	#finding the center px coordinates and storing them in a list
	for i in range(length):
		for j in range(length):
			if((i % kernel_size) == 0):
				if((j % kernel_size) == 0):
					center_coords.append([arr[i*length + j][1], arr[i*length + j][0]])

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			for k in range(len(center_coords)):
				if((i >= (center_coords[k][0][0] - kernel_width)) and (i <= (center_coords[k][0][0] + kernel_width))):
					if((j >= (center_coords[k][0][1] - kernel_width)) and (j <= (center_coords[k][0][1] + kernel_width))):
						img[i][j] = center_coords[k][1]


	cv2.imshow("result", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
