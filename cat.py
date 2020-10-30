import pyautogui
import math
import time

# if you wanna check your cursor position please use above function
# X, Y = pyautogui.position()
# print(X, Y)

defX = 501
defY = 423

def home_click():
	pyautogui.click(defX, defY)

def to_right():
	pyautogui.drag(20, 0, 0.21, button='left')

def to_down():
	pyautogui.drag(0, 20, 0.12, button='left')

def caret():
	pyautogui.mouseDown(button='left')
	pyautogui.moveTo(defX+30, defY-40, 0.1)
	pyautogui.moveTo(defX+50, defY+20, 0.1)
	pyautogui.mouseUp(button='left')

def v():
	pyautogui.mouseDown(button='left')
	pyautogui.moveTo(defX+30, defY+40, 0.1)
	pyautogui.moveTo(defX+50, defY-20, 0.1)
	pyautogui.mouseUp(button='left')

def voltex():
	pyautogui.mouseDown(button='left')
	for i in range(0, 10):
		j = (((i/10)*2)*math.pi)
		x = math.cos(j)
		y = math.sin(j)
		pyautogui.moveTo(defX + (defY/3)*x, defY + (defY/3)*y, 0.00001)
	pyautogui.mouseUp(button='left')

def o():
	pass

def heart():
	pass

for i in range(0, 100):
	home_click()
	to_right()
	home_click()
	to_down()
	home_click()
	caret()
	home_click()
	v()
	home_click()
	voltex()
	time.sleep(0.02)

# home_click()
# home_click()
# drag_to_right()
