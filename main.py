import utility as _u
import threading
import time
def drop_bobber():
	e_imgfound=threading.Event()
	e_stop=threading.Event()
	x=_u.get_imgctr('wheel.png')
	_u.pos_click(*x)
	sleep(0.5)
	th_bobber=threading.Thread(target=_u.img_loop_detect, args=('to_drop_bobber.png', e_imgfound, e_stop, _u.getArea()))
	th_bobber.start()
	e_imgfound.wait(timeout=10)
	if e_imgfound.is_set():
		_u.pos_click(*x)
		print('click')
		e_stop.set()
		th_bobber.join()
		return True
	else: 
		e_stop.set()
		th_bobber.join()
		return False
	
if __name__=='__main__':
	pass
	print(drop_bobber())