import utility as _u
import threading
from time import sleep
def drop_bobber(pos_wheel, searchArea):
	e_imgfound=threading.Event()
	e_stop=threading.Event()
	_u.pos_click(*pos_wheel)
	sleep(0.5)
	th_bobber=threading.Thread(target=_u.img_loop_detect, args=('no_bar_hover.png', e_imgfound, e_stop, searchArea))
	th_bobber.start()
	e_imgfound.wait(timeout=10)
	if e_imgfound.is_set():
		_u.pos_click(*pos_wheel)
		e_stop.set()
		th_bobber.join()
		return True
	else: 
		e_stop.set()
		th_bobber.join()
		return False
def fishing(pos_wheel, searchArea):
	from datetime import datetime as dt
	now=dt.now()
	while True:
		e_release=threading.Event()
		th_wheel=threading.Thread(target=_u.mouse_drag, args=(pos_wheel, pos_wheel, e_release))
		th_wheel.start()
		while not _u.get_imgctr('tension_hover.png', region=searchArea):
			if (dt.now()-now).seconds >=30:	break
		e_release.set()
		th_wheel.join()
		if (dt.now()-now).seconds >=30:	break
def startloop():
	searchArea=_u.getArea()
	pos_wheel=_u.get_imgctr('wheel.png')
	if not pos_wheel:
		import sys
		print("can't find wheel")
		sys.exit(1)
	while True:
		try:
			if drop_bobber( pos_wheel, searchArea):
				fishing(pos_wheel, searchArea)
			else:	continue
		except KeyboardInterrupt:
			break

if __name__=='__main__':
	pass
	print(startloop())