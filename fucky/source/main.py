#!/usr/bin/python
# advent of code level six with tkinter

import Tkinter
import re

tracker = [[False for x in range(1000)]] * 1000

winnie = Tkinter.Tk() # background window holding widgets

# create widgets and shit
c = Tkinter.Canvas(winnie, bg="black", height=1000, width=1000)

#c.create_rectangle(0,0,10,10, fill="red")

c.pack()

winnie.mainloop()

filey = open("input6.txt", "r")

while(True):
	liney = filey.readline()
	coords = map(int, re.findall(r'\d+', liney))
	if (liney[1] == 'o'):
		onofftoggle = 2 # toggle
	elif (liney[6] == 'n'):
		onofftoggle = 0 # on
	else:
		onofftoggle = 1 # off
	c.after(2000, drawLights, onofftoggle, coords)

def drawLights(on_off_toggle, coords):
	if (len(coords) != 4):
		return

	if (on_off_toggle == 0):
		#turn on square with coords
		c.create_rectangle(coords[0],coords[1],coords[2],coords[3], fill="red")
	elif (on_off_toggle == 1):
		c.create_rectangle(coords[0],coords[1],coords[2],coords[3], fill="black")
	else:
		toggle_em(coords)
	update_tracker(on_off_toggle, coords)

def update_tracker(num, coords):
	for x in range(coords[0], (coords[1] + 1)):
		for y in range(coords[2], (coords[3] + 1)):
			if (num == 0):
				if (tracker[x][y] == False):
					tracker[x][y] == True
			elif (num == 1):
				if (tracker[x][y] == True):
					tracker[x][y] == False
			else:
				tracker[x][y] = not tracker[x][y]

def toggle_em(coords):
	for x in range(coords[0], (coords[1] + 1)):
		for y in range(coords[2], (coords[3] + 1)):
			if (tracker[x][y] == False):
				c.create_rectangle(coords[x],coords[x+1],coords[y],coords[y+1], fill="red")
			else:
				c.create_rectangle(coords[x],coords[x+1],coords[y],coords[y+1], fill="black")


