import pyautogui as _g
import pynput as _p
from datetime import datetime as dt
from time import sleep
import threading
_g.PAUSE = 1
_g.FAILSAFE = True  
def get_imgpos(imgname, region=None):	return _g.locateOnScreen(imgname, region=region)
def get_imgctr(imgname, region=None):	return _g.locateCenterOnScreen(imgname, region=region)
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
def getArea():
	print('please click first coordinate...')
	is_clicked()
	s=_g.position()
	print('please click second coordinate...')
	is_clicked()
	e=_g.position()
	print(s,e)
	return s+e
def img_loop_detect(imgname, e_get, e_stop, searchArea=getArea()):
	now=dt.now()
	t=threading.currentThread()
	while True:
		if e_stop.is_set(): break
		if get_imgctr(imgname, region=searchArea):
			e_get.set()
			break
if __name__=='__main__':
	pass
	img_loop_detect('test.png')