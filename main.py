import utility as _u
import threading
import time
def drop_bobber():
	e_imgfound=threading.Event()
	e_stop=threading.Event()
	th_bobber=threading.Thread(target=_u.img_loop_detect, args=('do_not_drop.png', e_imgfound, e_stop, None))
	th_bobber.start()
	e_imgfound.wait(timeout=10)
	e_stop.set()
	th_bobber.join()
	if e_imgfound.is_set():	return _u.pos_click(*_u.get_imgctr('wheel.png'))
	else: return False
	
if __name__=='__main__':
	pass
	print(drop_bobber())