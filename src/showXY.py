# Execute this function to know the mouse location in pixels
# Most useful for debug stuff

import pyautogui

def showXY():
	try:
	    while True:
	        x, y = pyautogui.position()
	        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
	        print(positionStr, end='')
	        print('\b' * len(positionStr), end='', flush=True)
	        	

	except KeyboardInterrupt: #Press Ctrl+C to stop
	    print('\n\nThe software was stopped\n')


showXY()
