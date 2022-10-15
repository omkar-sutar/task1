'''
*****************************************************************************************
*
*                ===============================================
*                   Pharma Bot (PB) Theme (eYRC 2022-23)
*                ===============================================
*
*  This script is to implement Task 1A of Pharma Bot (PB) Theme (eYRC 2022-23).
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:        2851    [ Team-ID ]
# Author List:    Omkar Sutar, Aniruddha Godbole, Madhura Herlekar, Priyanka Kate    [ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:            task_1a.py
# Functions:        detect_traffic_signals, detect_horizontal_roads_under_construction, detect_vertical_roads_under_construction,
#                    detect_medicine_packages, detect_arena_parameters
#                     [ Comma separated list of functions in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv)                    ##
##############################################################
from turtle import position
import cv2
import numpy as np
from copy import deepcopy
##############################################################

# Constants
IMAGE_SIZE = 800
MAZE_SIZE = 600
SQUARE_SIZE = 100

################# ADD UTILITY FUNCTIONS HERE #################


def get_shapes(img):
    shapes=[]
    img = deepcopy(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # setting threshold of gray image
    _, threshold = cv2.threshold(gray, 251, 255, cv2.THRESH_BINARY)

    # using a findContours() function
    contours, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    i = 0

    
    # list for storing names of shapes
    for contour in contours:

        # here we are ignoring first counter because
        # findcontour function detects whole image as shape
        if i == 0:
            i = 1
            continue

    

    # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(
            contour, 0.03 * cv2.arcLength(contour, True), True)
        # print(approx.shape)
        # for _ in approx:
        #     for pix in _:
        #         img[pix[1]:pix[1]+20,pix[0]:pix[0]+20]=np.zeros((20,20,3),dtype=np.uint8)

        # using drawContours() function
        cv2.drawContours(img, [contour], -1, (0, 0, 255), 5)


    # finding center point of shape
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])

    # putting shape name at center of each shape
        if len(approx) == 3:
            shape="Triangle"

        elif len(approx) == 4:
            shape="Square"

        else:
            shape="Circle"

        color=None
        if list(img[y][x])==[0,127,255]:
            color="Orange"
        elif list(img[y][x])==[255,255,0]:
            color="Skyblue"
        elif list(img[y][x])==[0,255,0]:
            color="Green"
        elif list(img[y][x])==[180,0,255]:
            color="Pink"

        shapes.append([color,shape,[x,y]])
    # displaying the image after drawing contours
    # cv2.imshow('shapes', img)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return shapes

##############################################################


def detect_traffic_signals(maze_image):
    """
    Purpose:
    ---
    This function takes the image as an argument and returns a list of
    nodes in which traffic signals are present in the image

    Input Arguments:
    ---
    `maze_image` :    [ numpy array ]
                    numpy array of image returned by cv2 library
    Returns:
    ---
    `traffic_signals` : [ list ]
                    list containing nodes in which traffic signals are present

    Example call:
    ---
    traffic_signals = detect_traffic_signals(maze_image)
    """
    traffic_signals = []

    ##############    ADD YOUR CODE HERE    ##############
    indices = ["A", "B", "C", "D", "E", "F", "G"]

    for row in range(3, MAZE_SIZE+1, SQUARE_SIZE-1):
        for col in range(4, MAZE_SIZE+1, SQUARE_SIZE-1):
            # maze_image[row][col]=np.array([0,255,0])
            if (maze_image[row][col] == np.array([0, 0, 255])).all():
                letter = indices[col//100]
                number = row//100 + 1
                position = f"{letter}{number}"
                traffic_signals.append(position)

    ##################################################

    return traffic_signals


def detect_horizontal_roads_under_construction(maze_image):
    """
    Purpose:
    ---
    This function takes the image as an argument and returns a list
    containing the missing horizontal links

    Input Arguments:
    ---
    `maze_image` :    [ numpy array ]
                    numpy array of image returned by cv2 library
    Returns:
    ---
    `horizontal_roads_under_construction` : [ list ]
                    list containing missing horizontal links

    Example call:
    ---
    horizontal_roads_under_construction = detect_horizontal_roads_under_construction(
        maze_image)
    """
    horizontal_roads_under_construction = []

    ##############    ADD YOUR CODE HERE    ##############
    indices = ["A", "B", "C", "D", "E", "F", "G"]
    for row in range(2, MAZE_SIZE, SQUARE_SIZE):
        for col in range(SQUARE_SIZE, MAZE_SIZE+1, SQUARE_SIZE):
            # coordinates of the midpoint of road
            midpoint = [row, col-(SQUARE_SIZE//2)]
            if (maze_image[midpoint[0]][midpoint[1]] == np.array([255, 255, 255])).all():
                number = row//SQUARE_SIZE + 1  # 1 based indexing
                letter_left = indices[midpoint[1]//SQUARE_SIZE]
                letter_right = indices[midpoint[1]//SQUARE_SIZE + 1]
                position = f"{letter_left}{number}-{letter_right}{number}"
                horizontal_roads_under_construction.append(position)

    ##################################################
    return horizontal_roads_under_construction


def detect_vertical_roads_under_construction(maze_image):
    """
    Purpose:
    ---
    This function takes the image as an argument and returns a list
    containing the missing vertical links

    Input Arguments:
    ---
    `maze_image` :    [ numpy array ]
                    numpy array of image returned by cv2 library
    Returns:
    ---
    `vertical_roads_under_construction` : [ list ]
                    list containing missing vertical links

    Example call:
    ---
    vertical_roads_under_construction = detect_vertical_roads_under_construction(
        maze_image)
    """
    vertical_roads_under_construction = []

    ##############    ADD YOUR CODE HERE    ##############

    indices = ["A", "B", "C", "D", "E", "F", "G"]
    for row in range(SQUARE_SIZE, MAZE_SIZE+1, SQUARE_SIZE):
        for col in range(2, MAZE_SIZE+1, SQUARE_SIZE):
            midpoint = [row-(SQUARE_SIZE//2), col]
            if (maze_image[midpoint[0]][midpoint[1]] == np.array([255, 255, 255])).all():
                letter = indices[midpoint[1]//SQUARE_SIZE]
                number_up = midpoint[0]//SQUARE_SIZE+1
                number_down = number_up+1
                position = f"{letter}{number_up}-{letter}{number_down}"
                vertical_roads_under_construction.append(position)

    ##################################################
    return vertical_roads_under_construction


def detect_medicine_packages(maze_image):
    """
    Purpose:
    ---
    This function takes the image as an argument and returns a nested list of
    details of the medicine packages placed in different shops

    ** Please note that the shop packages should be sorted in the ASCENDING order of shop numbers
       as well as in the alphabetical order of colors.
       For example, the list should first have the packages of shop_1 listed.
       For the shop_1 packages, the packages should be sorted in the alphabetical order of color ie Green, Orange, Pink and Skyblue.

    Input Arguments:
    ---
    `maze_image` :    [ numpy array ]
                    numpy array of image returned by cv2 library
    Returns:
    ---
    `medicine_packages` : [ list ]
                    nested list containing details of the medicine packages present.
                    Each element of this list will contain
                    - Shop number as Shop_n
                    - Color of the package as a string
                    - Shape of the package as a string
                    - Centroid co-ordinates of the package
    Example call:
    ---
    medicine_packages = detect_medicine_packages(maze_image)
    """
    medicine_packages = []

    ##############    ADD YOUR CODE HERE    ##############

    maze_image = deepcopy(maze_image)
    maze_image2 = deepcopy(maze_image)

    maze_image = maze_image[20:-20, 20:-20]

    # remove black

    black_lo = np.array([0, 0, 0])
    black_hi = black_lo

    mask1 = cv2.inRange(maze_image, black_lo, black_hi)

    blue_lo = blue_hi = np.array([255, 0, 0])
    mask2 = cv2.inRange(maze_image, blue_lo, blue_hi)

    red_lo = np.array([0, 0, 255])
    red_hi = red_lo

    mask3 = cv2.inRange(maze_image, red_lo, red_hi)
    mask = cv2.bitwise_or(mask1, cv2.bitwise_or(mask2, mask3))
    maze_image[mask > 0] = (255, 255, 255)

    shop_num=1
    for row in range(0, maze_image.shape[0], SQUARE_SIZE-5):
        for col in range(0, maze_image.shape[0], SQUARE_SIZE-5):
            img = maze_image[row:row+SQUARE_SIZE-5, col:col+SQUARE_SIZE-5]
            img = cv2.resize(img, (1000, 1000),
                             interpolation=cv2.INTER_NEAREST)
            shapes=get_shapes(img)
            for shape in shapes:
                if len(shape)>0:
                    ans=[f"Shop_{shop_num}"]+shape
                    medicine_packages.append(ans)



##################################################

    return medicine_packages


def detect_arena_parameters(maze_image):
    """
    Purpose:
    ---
    This function takes the image as an argument and returns a dictionary
    containing the details of the different arena parameters in that image

    The arena parameters are of four categories:
    i) traffic_signals : list of nodes having a traffic signal
    ii) horizontal_roads_under_construction : list of missing horizontal links
    iii) vertical_roads_under_construction : list of missing vertical links
    iv) medicine_packages : list containing details of medicine packages

    These four categories constitute the four keys of the dictionary

    Input Arguments:
    ---
    `maze_image` :    [ numpy array ]
                    numpy array of image returned by cv2 library
    Returns:
    ---
    `arena_parameters` : { dictionary }
                    dictionary containing details of the arena parameters

    Example call:
    ---
    arena_parameters = detect_arena_parameters(maze_image)
    """
    arena_parameters = {}

    ##############    ADD YOUR CODE HERE    ##############

    # Just keep the maze
    maze_image = maze_image[95:705, 95:705]

    MAZE_SIZE = len(maze_image)
    SQUARE_SIZE = MAZE_SIZE//6

    arena_parameters['horizontal_roads_under_construction'] = detect_horizontal_roads_under_construction(maze_image)
    arena_parameters['vertical_roads_under_construction'] = detect_vertical_roads_under_construction(maze_image)
    arena_parameters['traffic_signals'] = detect_traffic_signals(maze_image)
    arena_parameters['medicine_packages']=detect_medicine_packages(maze_image)
    ##################################################

    return arena_parameters

######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########


if __name__ == "__main__":

    # path directory of images in test_images folder
    img_dir_path = "public_test_images/"

    # path to 'maze_0.png' image file
    file_num = 0
    img_file_path = img_dir_path + 'maze_' + str(file_num) + '.png'

    # read image using opencv
    maze_image = cv2.imread(img_file_path)

    print('\n============================================')
    print('\nFor maze_' + str(file_num) + '.png')

    # detect and print the arena parameters from the image
    arena_parameters = detect_arena_parameters(maze_image)

    print("Arena Prameters: ", arena_parameters)

    # # display the maze image
    # cv2.imshow("image", maze_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    choice = input(
        '\nDo you want to run your script on all test images ? => "y" or "n": ')

    if choice == 'y':

        for file_num in range(1, 15):

            # path to maze image file
            img_file_path = img_dir_path + 'maze_' + str(file_num) + '.png'

            # read image using opencv
            maze_image = cv2.imread(img_file_path)
            print(maze_image.shape)

            print('\n============================================')
            print('\nFor maze_' + str(file_num) + '.png')

            # detect and print the arena parameters from the image
            arena_parameters = detect_arena_parameters(maze_image)

            print("Arena Parameter: ", arena_parameters)

            # # display the test image
            # cv2.imshow("image", maze_image)
            # cv2.waitKey(2000)
            # cv2.destroyAllWindows()

# madhura
# omkar sutar
# priyanka

# omkar
# priyanka
# aniruddha
