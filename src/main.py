import pyautogui, sys
import time
from getbuttonlocation import get
from screenshot import takeScreenshot

def start():

	print('Waiting for the queue shows up...')

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


	# take screenshot
	takeScreenshot()

	# it returns a tuple with 2 values
	XY = get()

	x = XY[0]
	y = XY[1]

	move(x, y)


while True:
	start()
	time.sleep(1) 
	print('\n\n')



