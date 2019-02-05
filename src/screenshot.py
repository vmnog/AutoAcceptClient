from mouse import *
import time, sys, pyautogui as p

def wait():
	move(962, 769)  #client button location at resolution 1920x1080
	click()


def move(x, y):
	p.moveTo(x, y)
	print('The button showed up!')
	#print(f'The mouse was moved to {x}, {y}') #debug stuff

def click():
	p.click
	print('The button was clicked!')
