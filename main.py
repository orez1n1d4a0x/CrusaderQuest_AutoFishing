import utility as _u
import threading
from time import sleep

from pynput.mouse import Button, Controller
mouse = Controller()

def drop_bobber(pos_wheel, searchArea):
	e_imgfound=threading.Event()
	e_stop=threading.Event()
	mouse.position=tuple(pos_wheel)
	mouse.click(Button.left, 1)
	th_bobber=threading.Thread(target=_u.img_loop_detect, args=('no_bar_hover.png', pos_wheel, e_imgfound, e_stop, searchArea))
	th_bobber.start()
	e_imgfound.wait(timeout=5)
	if e_imgfound.is_set():
		mouse.click(Button.left, 1)
		print('drop')
		e_stop.set()
		# th_bobber.join()
		return True
	else: 
		e_stop.set()
		th_bobber.join()
		return False

def dropHook( pos):
	print('drop hook')
	mouse.position=tuple(pos)
	mouse.click(Button.left, 1)
def liftHook( pos):
	sleep(4.5)
	mouse.position=tuple(pos)
	mouse.click(Button.left, 1)
	print('lift hook')
def rotateHook(pos):
	sleep(2)
	print('rotate hook')
	_u.drag(pos, 1.5)
	for i in range(10):
		_u.drag(pos, 0.5)
		sleep(0.5/2.1)
		print(i)
def start():
	wheel_pos=_u.getPos('wheel')
	continue_pos=_u.getPos('continue')
	searchArea=_u.getArea()
	while True:
		if drop_bobber(wheel_pos, searchArea):
			sleep(2)
			liftHook(wheel_pos)
			rotateHook(wheel_pos)
			mouse.position=tuple(continue_pos)
			sleep(10)
			mouse.click(Button.left, 1)
			sleep(2)
if __name__=='__main__':
	pass
	start()