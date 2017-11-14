import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
import cv2
import os
# Import everything needed to edit/save/watch video clips
from moviepy.editor import VideoFileClip
from IPython.display import HTML

def blur_gaussian(img, kernel_size):
	return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
	
def roi(img, vertices):

	#define a numpy array with the dimensions of img, but comprised of zeros
	mask = np.zeros_like(img)
	
	#Uses 3 channels or 1 channel for color depending on input image
	if len(img.shape) > 2:
		channel_count = img.shape[2]
		ignore_mask_color = (255,) * channel_count
	else:
		ignore_mask_color = 255
	
	#creates a polygon with the mask color
	cv2.fillPoly(mask, np.int32([vertices]), ignore_mask_color)
	
	#returns the image only where the mask pixels are not zero
	masked_image = cv2.bitwise_and(img, mask)
	return masked_image
	
def drawlines(img, lines, color=[255, 0, 0], thickness=3):
	for line in lines:
		for x1, y1, x2, y2 in line:
			cv2.line(img, (x1,y1), (x2, y2), color, thickness)
			
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
	#img should be the output of a canny transform
	lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
	line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
	drawlines(line_img, lines)
	return line_img
	
def processImage(image):
		shape = np.array([[0, image.shape[0]], [image.shape[1], image.shape[0]], [(0.55*image.shape[1]), (0.62*image.shape[0])], [(0.45*image.shape[1]), (0.62*image.shape[0])]])

		blur = blur_gaussian(image, 5)
		gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
		canny = cv2.Canny(gray, 50, 170)
		masked = roi(canny, shape)
		myline = hough_lines(masked, 1, np.pi/180, 20, 10, 900)
		weightedSum = cv2.addWeighted(myline, 0.8, image, 1, 0)
		
		plt.imshow(weightedSum)		
		plt.show()

if __name__ == "__main__": 
		os.listdir("test_images/")

		image = plt.imread('test_images/whiteCarLaneSwitch.jpg')
		processImage(image)
		
