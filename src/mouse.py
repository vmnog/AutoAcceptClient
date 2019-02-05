import pyautogui, sys
import keyboard

#move to the button move(x, y)
def move(x, y):
	pyautogui.moveTo(x, y)
	print(f'The mouse was moved to {x}, {y}')

def showXY():
	print('Press Ctrl-C to quit.')
	i = 0
	try:
	    while True:
	        x, y = pyautogui.position()
	        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
	        print(positionStr, end='')
	        print('\b' * len(positionStr), end='', flush=True)
	        
	        if (keyboard.is_pressed('q')):
	        	i += 1
	        	print('\nQ pressed for ' + str(i) + ' times' + '\r', end='', flush=True)
	        	

	except KeyboardInterrupt:
	    print('\n\nThe software was stopped\n')



