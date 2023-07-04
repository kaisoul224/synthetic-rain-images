#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import sys
import random
import math
import os

degtorad = 0.01745329252
radtodeg = 1 / degtorad

# returns a list of lines
def rand_lines(w, h, a, l, nrs):
    lines = []

    for i in range(nrs):
        # randomize starting and ending points for 2D lines
        sx = random.randint(0, w - 1)
        sy = random.randint(0, h - 1)
        le = random.randint(1, l)
        ang = a + random.randint(0, 10)
        ex = sx + int(le * math.sin(ang * degtorad))
        ey = sy + int(le * math.cos(ang * degtorad))

        # move the endpoints inside the image frame
        if ex < 0: ex = 0
        if ex > w - 1: ex = w - 1
        if ey < 0: ey = 0
        if ey > w - 1: ey = h - 1

        # add line to list
        lines.append({'sx': sx, 'sy': sy, 'ex': ex, 'ey': ey})

    return lines


def add_rain(img, angle, drop_length, drop_thickness, drop_nrs, blur=4, intensity=100):
    # create placehplder for rain
    rain = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype='uint16')

    # generate random lines
    lines = rand_lines(rain.shape[1], rain.shape[0], angle, drop_length, drop_nrs)

    # draw lines to the image
    for l in lines:
        cv2.line(rain, (l['sx'], l['sy']), (l['ex'], l['ey']), (intensity, intensity, intensity), drop_thickness)

    # add blur to the lines
    rain = cv2.blur(rain, (blur, blur))

    return rain + img




def export_rain_images():
    images = []
    for filename in os.listdir(source_path):
        imgPath = os.path.join(source_path, filename)
        file = imgPath
        # read image
        try:
            img = cv2.imread(str(file))
        except:
            print("Could not open file")
            next

        # height, width, number of channels in image
        height = img.shape[0]
        width = img.shape[1]

        # =============== config =================
        # Angle given as integer between (-90 < angle < 90)
        # angle = 100 -> random
        angle = 100
        # The max length of rain drops in pixels(the actual length is random up to length)
        # should be matched somehow to the image resolution
        length = 20
        # Rain drop width
        thickness = 1
        # Number of raindrops to be added
        drop_nrs = 1000
        # Size of blur filter
        blur = 4
        # Intensity(grayscale) of rain streaks
        intensity = 100




        # road
        if height == 360 and width == 640 :
            angle = 100
            length = 70
            thickness = 1
            drop_nrs = 1800
            blur = 3
            intensity = 100
        elif height == 450 and width == 800:
            angle = 0
            length = 100
            thickness = 1
            drop_nrs = 500
            blur = 9
            intensity = 120
        # normal
        elif height == 512 and width == 384:
            angle = 100
            length = 70
            thickness = 1
            drop_nrs = 1750
            blur = 3
            intensity = 120
        elif height == 384 and width == 512:
            angle = 100
            length = 70
            thickness = 1
            drop_nrs = 1750
            blur = 3
            intensity = 120
        elif height == 728 and width == 1296:
            angle = 100
            length = 120
            thickness = 1
            drop_nrs = 3000
            blur = 3
            intensity = 120
        elif height==120 and width == 160:
            angle = 100
            length = 30
            thickness = 1
            drop_nrs = 350
            blur = 3
            intensity = 120


        # donkey car
        # 160 x 120
        # 1-2-3:    100 30 1 200 9 120
        # 4-5-6:    100 30 1 250 7 120
        # 7-8-9:    100 30 1 300 5 120
        # 10-11-12: 100 30 1 350 3 120

        # road
        # 800 x 450
        # 1-2-3:    100 100 1 1000 9 120
        # 4-5-6:    100 100 1 1300 7 120
        # 7-8-9:    100 100 1 1600 5 120
        # 10-11-12: 100 100 1 1900 3 120
        # 640 x 360 --------
        # 1-2-3:    100 70 1 1000 9 120
        # 4-5-6:    100 70 1 1250 7 120
        # 7-8-9:    100 70 1 1500 5 120
        # 10-11-12: 100 70 1 1800 3 120

        # normal
        # 512 x 384---------
        # 1-2-3:    100 70 1 1000 9 120
        # 4-5-6:    100 70 1 1250 7 120
        # 7-8-9:    100 70 1 1500 5 120
        # 10-11-12: 100 70 1 1750 3 120
        # 384 X 512----------
        # 1-2-3:    100 70 1 1000 9 120
        # 4-5-6:    100 70 1 1250 7 120
        # 7-8-9:    100 70 1 1500 5 120
        # 10-11-12: 100 70 1 1750 3 120
        # 1296 x 728----------
        # 1-2-3:    100 70 1 1750 9 120
        # 4-5-6:    100 70 1 2250 7 120
        # 7-8-9:    100 70 1 2700 5 120
        # 10-11-12: 100 70 1 3000 3 120

        # if one/some of the parameters were not given: randomize for each image
        if angle == 100:
            rangle = random.randint(-60, 60)
        else:
            rangle = angle

        if length == -1:
            rlength = random.randint(10, 30)
        else:
            rlength = length

        if thickness == -1:
            rthickness = random.randint(1, 2)
        else:
            rthickness = thickness

        if drop_nrs == -1:
            rdrop_nrs = random.randint(500, 2000)
        else:
            rdrop_nrs = drop_nrs

        # print(file)

        # add rain
        rainy = add_rain(img, rangle, rlength, rthickness, rdrop_nrs, blur, intensity)

        # print(file)

        # save rainy image
        print(save_path + file[7:-4] + '_' + num + '.jpg')
        cv2.imwrite(save_path + file[7:-4] + '_' + num + '.jpg', rainy)

    return images

num = '1'

source_path = "./imgs"
save_path = "./result/"

def main(argv):
    export_rain_images()

if (__name__ == "__main__"):
    main(sys.argv[1:])