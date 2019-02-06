import pyautogui

def takeScreenshot():

	# Take screenshot
	pic = pyautogui.screenshot()
	 
	# Save the image
	pic.save('../images/Screenshot.png') 

	print('Screenshot taked! Analyzing ...')


