import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
IMAGE_SIZE=800
MAZE_SIZE=600
SQUARE_SIZE=100

#img = cv.imread('public_test_images\maze_0.png')
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#_, threshold = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
#cv.imshow('maze', img)
#cv.imshow('maze', gray)
#cv.waitKey(0)

def detect_medicine_packages(maze_img):
    medicine_packages = []

	##############	ADD YOUR CODE HERE	##############
    gray = cv.cvtColor(maze_img, cv.COLOR_BGR2GRAY)
    _, threshold = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(
    threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
  
    i = 0
    #cv.imshow('maze', maze_img)
    cv.imshow('maze', threshold)
    cv.waitKey(0)
    print(contours)
    for contour in contours:
  
    # here we are ignoring first counter because 
    # findcontour function detects whole image as shape
        if i == 0:
            i = 1
            continue
  
    # cv2.approxPloyDP() function to approximate the shape
        approx = cv.approxPolyDP(
        contour, 0.01 * cv.arcLength(contour, True), True)
      
    # using drawContours() function
        cv.drawContours(maze_img, [contour], 0, (0, 0, 255), 5)
    
        # finding center point of shape
        M = cv.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
    
        # putting shape name at center of each shape
        if len(approx) == 3:
            cv.putText(maze_img, 'Triangle', (x, y),
                        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
        elif len(approx) == 4:
            cv.putText(maze_img, 'Quadrilateral', (x, y),
                        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
        elif len(approx) == 5:
            cv.putText(maze_img, 'Pentagon', (x, y),
                        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
        elif len(approx) == 6:
            cv.putText(maze_img, 'Hexagon', (x, y),
                        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
        else:
            cv.putText(maze_img, 'circle', (x, y),
                        cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        cv.imshow('shapes', maze_img)
        cv.waitKey(0)
        cv.destroyAllWindows()
	##################################################

    return medicine_packages

if __name__ == "__main__":

    # path directory of images in test_images folder
	
	#Just keep the maze
    img = cv.imread('public_test_images\maze_0.png')
    img=img[95:705,95:705]

    #MAZE_SIZE=len(maze_image)
    #SQUARE_SIZE=MAZE_SIZE//6
	
    #print('\n============================================')
    #print('\nFor maze_' + str(file_num) + '.png')

	# detect and print the arena parameters from the image
    arena_parameters = detect_medicine_packages(img)

    print("Arena Prameters: " , arena_parameters)

	# display the maze image
    cv.imshow("image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')
	
    # if choice == 'y':

    # 	for file_num in range(1, 15):
			
	# 		# path to maze image file
    #         img_file_path = img_dir_path + 'maze_' + str(file_num) + '.png'
			
	# 		# read image using opencv
    #         maze_image = cv.imread(img_file_path)
	
    #         print('\n============================================')
    #         print('\nFor maze_' + str(file_num) + '.png')
			
	# 		# detect and print the arena parameters from the image
    #         arena_parameters = detect_medicine_packages(maze_image)

    #         print("Arena Parameter: ", arena_parameters)
				
	# 		# display the test image
    #         cv.imshow("image", maze_image)
    #         cv.waitKey(2000)
    #         cv.destroyAllWindows()