from datetime import datetime, timedelta
import pyautogui as _g
from time import sleep
import threading
_g.PAUSE = 1
_g.FAILSAFE = True  

def getPos(name):
	input( f'move to {name} postition and press enter')
	return _g.position()

def getimg(img):	return _g.locateOnScreen(img, confidence=0.97)

def loop_getimg(img, e_main, tlimit=10):
	now=datetime.now()
	x=None
	while (	not e_main.is_set() and 
			not x and 
			datetime.now()-now < timedelta(seconds=tlimit)
			):
		x=_g.locateOnScreen(img, confidence=0.8)
	
	return x

def img_loop_detect(imgname, e_drop, e_main):
	while not e_main.is_set():
		# if e_stop.is_set():
		# 	e_stop.clear()
		# 	print(e_stop.is_set())
		# 	break
		if not _g.locateOnScreen(imgname, confidence=0.7):
			e_drop.set()
			print('drop bobber')
			break
	print('end img_loop_detect')

if __name__=='__main__':
	pass
	# mx=getPos('start searching point')
	# print(mx)
	x=getimg('safe_zone.png')
	print(x)
	from pynput.mouse import Button, Controller
	mouse = Controller()
	mouse.position=tuple(x)
	mouse.click(Button.left)