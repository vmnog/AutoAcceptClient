import pyautogui, sys
from screenshot import *

def start():
	print('Nothing yet...')
	#move(962, 769)  #client button location at resolution 1920x1080
	#showXY()		#shows where the mouse location is relative to pixels
	#wait()


def showXY():
	try:
	    while True:
	        x, y = pyautogui.position()
	        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
	        print(positionStr, end='')
	        print('\b' * len(positionStr), end='', flush=True)
	        	

	except KeyboardInterrupt: #Press Ctrl+C to stop
	    print('\n\nThe software was stopped\n')


