#!/usr/bin/python
# -*- coding: utf8 -*-

#Author Παναγιώτης Πράττης/Panagiotis Prattis

'''
'''

from PIL import Image, ImageDraw
import random
import math

width = height = 1024;
nCircles = 20;
minRadius = 10;
maxRadius = 100;#you should reduce the max radius in order for the outcome to be clearer

# Create image with white background
im = Image.new("RGB", (width, height), "white");
draw = ImageDraw.Draw(im);

# Function to draw a circle
def draw_circle(posX, posY, radius):
	draw.ellipse((posX-radius, posY-radius, posX+radius, posY+radius),
	             outline ='red')

# this array will contain the positions and radius of the circles for later calculations
circles = []


#this is the code for completely random circles which aren't always inside the final image
#for i in range(0, nCircles):
	#x = random.randint(0,width)
	#y = random.randint(0,height)
	#r = random.randint(minRadius,maxRadius)
	#draw_circle(x, y, r)
	#circles.append([x,y,r])

# Draw circles
for i in range(0, nCircles):
	r = random.randint(minRadius,maxRadius)
	x = random.randint(r,width-r)
	y = random.randint(r,height-r)
	draw_circle(x, y, r)
	circles.append([x,y,r])


# Formula for calculating if two circles intersect, 
# given two circles (x0,y0,R0) and (x1,y1,R1):
#(R0-R1)^2 <= (x0-x1)^2+(y0-y1)^2 <= (R0+R1)^2

intersections = []

for i in range(nCircles):
	x0 = circles[i][0]
	y0 = circles[i][1]
	r0 = circles[i][2]
	for j in range(i+1, nCircles):
		x1 = circles[j][0]
		y1 = circles[j][1]
		r1 = circles[j][2]
		distance = math.pow(x0-x1, 2) + math.pow(y0-y1, 2)
		#if( math.pow(x0-x1, 2) + math.pow(y0-y1, 2) <= math.pow(r0+r1 ,2) and math.pow(x0-x1, 2) + math.pow(y0-y1, 2) >= math.pow(r0-r1 ,2)):
		if( math.pow(r0-r1, 2) <= distance and distance <= math.pow(r0+r1, 2) ):
			if i not in intersections:
				intersections.append(i)
			if j not in intersections:
				intersections.append(j)
        
print "There are " + `len(intersections)` + " circles that intersect."


# Save image
im.save('output.png')
im.show()


