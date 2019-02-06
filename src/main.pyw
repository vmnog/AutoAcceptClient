import pyautogui, sys
import time
from getbuttonlocation import *
from screenshot import takeScreenshot
from plyer import notification

# move the mouse to a specifc location
def move(x, y):
	#print('The button showed up!')
	pyautogui.moveTo(x, y)	
	#print(f'The mouse was moved to {x}, {y}') #debug stuff
	click()
	
	
# mouse clicks
def click():
	pyautogui.click()
	#print('The button was clicked!')
	notification.notify(
    	title='AutoAcceptQueue',
   	 	message='The Queue was accept.',
    	app_name='AutoAccept',
    	app_icon='../images/icon.ico'
	)
	exit()


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


notification.notify(
    title='AutoAcceptQueue',
    message='Running, waiting for the queue ',
    app_name='AutoAccept',
    app_icon='../images/icon.ico'
)

print('\nWaiting for the queue shows up...')
i = 0
while True:
	i += 1
	print(i, end='')
	print('\b' * i, end='', flush=True)
	start()
	time.sleep(1) 

# start()



