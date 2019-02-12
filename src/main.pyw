import pyautogui, sys
import time
from getbuttonlocation import *
from screenshot import takeScreenshot
from plyer import notification

def note(msg):
	notification.notify(
    title='AutoAcceptQueue',
    message=msg,
    app_name='AutoAccept',
    app_icon='../images/icon.ico'
)

# move the mouse to a specifc location
def move(x, y):
	#print('The button showed up!')
	pyautogui.moveTo(x, y)	
	#print(f'The mouse was moved to {x}, {y}') #debug stuff
	click()
	time.sleep(5)
	start()
	
	
# mouse clicks
def click():
	pyautogui.click()
	#print('The button was clicked!')
	note('The queue was accepted')


def start():
	# take screenshot
	takeScreenshot()
	# it returns a tuple with 2 values
	XY = get()
	if XY is None:
		#print("Button not found yet...")
		return 0
	else:
		x = XY[0]
		y = XY[1]
		move(x, y)
note('Waiting for the queue')
i = 0
while True:
	i += 1
	print(i, end='')
	print('\b' * i, end='', flush=True)
	start()
	time.sleep(1) 
