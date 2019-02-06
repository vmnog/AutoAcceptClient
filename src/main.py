import pyautogui, sys
import time
from getbuttonlocation import *
from screenshot import takeScreenshot

# move the mouse to a specifc location
def move(x, y):
	print('The button showed up!')
	pyautogui.moveTo(x, y)	
	#print(f'The mouse was moved to {x}, {y}') #debug stuff
	click()
	
# mouse clicks
def click():
	pyautogui.click
	print('The button was clicked!')
	exit()
	


def start():

	print('\nWaiting for the queue shows up...')

	# take screenshot
	takeScreenshot()

	# it returns a tuple with 2 values
	XY = get()

	if XY is None:
		print("Button not found yet...")
	else:
		x = XY[0]
		y = XY[1]
		move(x, y)


i = 0
while True:
	i += 1
	print('\n\n Checking time nº ' + str(i) + '\n\n')
	start()
	time.sleep(1) 

# start()



