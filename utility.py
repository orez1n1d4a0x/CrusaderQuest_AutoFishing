import pyautogui as _g
import pynput as _p
from datetime import datetime as dt
from time import sleep
import threading
_g.PAUSE = 1
_g.FAILSAFE = True  
def get_imgpos(imgname, region=None):	return _g.locateOnScreen(imgname, region=region)
def get_imgctr(imgname, region=None):	return _g.locateCenterOnScreen(imgname, region=region)
def loop_getimg(imgname, region=None, timeout=10):
	now=dt.now()
	while True:
		x=get_imgctr(imgname, region)
def pos_click(x,y):	_g.click(x,y)

def onClick(x, y, button, pressed):
	if pressed:	return False # to stop the thread after click
def is_clicked():
	with _p.mouse.Listener(on_click=onClick) as l:
		now=dt.now()
		while True:
			if not l.is_alive(): return
			if (dt.now()-now).seconds > 30:
				l.stop()
				return
def getPos(name):
	input( f'move to {name} postition and press enter')
	return _g.position()
def getArea():
	input('please move to first coordinate and press enter')
	s=_g.position()
	input('please move to second coordinate and press enter')
	e=_g.position()
	print(s,e)
	return s+e
def img_loop_detect(imgname, pos, e_get, e_stop, searchArea=None):
	while True:
		if not get_imgctr(imgname, region=searchArea):
			print('to drop')
			e_get.set()
			break
		if e_stop.is_set(): break
def drag( pos, t):
	from pynput.mouse import Button, Controller
	mouse = Controller()
	mouse.press(Button.left)
	sleep(t)
	mouse.release(Button.left)
if __name__=='__main__':
	pass
	img_loop_detect('test.png')