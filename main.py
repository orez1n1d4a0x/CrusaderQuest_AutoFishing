import utility as _u
import threading
from datetime import datetime, timedelta
from time import sleep

import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True  

from pynput.mouse import Button, Controller
from pynput import keyboard
mouse = Controller()
e_main=threading.Event()
e_drop=threading.Event()
e_stop=threading.Event()

def mouse_click(pos):
	mouse.psition=tuple(pos)
	mouse.click(Button.left, 1)
def mouse_release(pos):
	mouse.psition=tuple(pos)
	mouse.release(Button.left)
def mouse_press(pos):
	mouse.psition=tuple(pos)
	mouse.press(Button.left)

def checking_bobber(pos_wheel):
	sleep(1)
	mouse_click(pos_wheel) # throwing bobber
	thd_bobber=threading.Thread(target=_u.img_loop_detect, args=('no_bar_hover_2.png', e_drop, e_main))
	sleep(1)
	thd_bobber.start()
	e_drop.wait(timeout=5)
	if e_drop.is_set():
		e_drop.clear()
		print(e_drop.is_set())
		mouse_click(pos_wheel) # confirm bobber
		# e_stop.set()
		return True
	else:
		# e_stop.set()
		thd_bobber.join() # wait thd_bobber close
		return False

def liftBobber( pos):
	if _u.loop_getimg('on_the_hook.png', e_main, tlimit=10):
		mouse_click(pos)
		print('lift bobber')

def fishing(wheel_pos):
	now=datetime.now()
	while not _u.getimg('continue_button.png') and datetime.now()-now < timedelta(seconds=60):
		if e_main.is_set():	break
		if _u.getimg('safe_zone.png'):
			mouse_release(wheel_pos)
			sleep(0.1)
		else:
			mouse_press(wheel_pos)
			sleep(0.15)
	mouse_release(wheel_pos)
def start():
	
	def on_release(key):
		print('{0} released'.format(key))
		if key == keyboard.Key.ctrl_l:
			print('Stop listener')
			e_main.set()
			return False
	listener = keyboard.Listener(
    	on_release=on_release)
	listener.start()
	wheel_pos=_u.getPos('wheel')
	continue_pos=_u.getPos('continue')
	sleep(1)
	while not e_main.is_set():
		if checking_bobber(wheel_pos):
			sleep(3)
			liftBobber(wheel_pos)
			sleep(2)
			fishing(wheel_pos)
			sleep(1)
			mouse_click(continue_pos)
			# sleep(10)
			# mouse.position=tuple(continue_pos)
			# mouse.click(Button.left, 1)
			# sleep(2)
if __name__=='__main__':
	pass
	start()