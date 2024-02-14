# rc1_run.py

The rc1_run.py program draws upon a diverse suite of libraries. One of these is __4Aspyx__, the 4Ax python plugin library.

__4Aspyx__ is not currently open source and the code offered below draws upon a number of __4Aspyx__ scripts. These scripts are unique to a particular use case and are therefore
currently confidential. However the overarching architecture is clearly defined below.


open cv2 and python 3.6 & 3.8 need to be installed on capture device/Hardware/Nano

debugging needs to be completed on a Linux computer or virtual environment as opencv-python wheel will not build on (e.g) Mac OS 10.15

the pyautogui script will work for HD (1920 x 1080) displays. In the event of an end-user using a different resolution display, this would need to be instantiated. Multi-user customers would be required to standardise their hardware (i.e not allow various technicians to use their personal mobile/ tablet/ laptops).    

pip install opencv-python

pip install Jetson.GPIO

	sudo groupadd -f -r gpio
 
	sudo usermod -a -G gpio ### home directory
 
pip3 install pyautogui	

On Linux (Nano), you may need to install the scrot application, and Tkinter in the following order:

	sudo apt-get install python3-tk

	sudo apt-get install python3-dev

	sudo apt-get install scrot
	
from __4Aspyx:__
 
__import RCdist1.py__  
__import RCmotor1.py__   
__import RCalertLED1s.py__  
__import RC2cameraCap1__  
__RCDamageDetectnet50__

__import glob__	  
__import sys__	  
__import pandas__ as __pd__  
__import pathlib__  
__import Jetson.GPIO__ as __GPIO__ 

from threading __import Thread__  
from gi.repository __import Gst, GObject__

__import cv2__  
__import numpy__ as __np__  
__import pyautogui__  
__import Xlib__  
__import time__  
__import os__

_### gpio numbers set according to board pin layout_  
`GPIO.setmode(GPIO.BOARD)`			

`def configure_gpio():`
  
`GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)`	_### LEDs GPIO  (GPIO11) set to output and low_

`GPIO.setup(7,  GPIO.OUT, initial=GPIO.LOW)`	_### motor GPIO (GPIO7) set to output and low_

`GPIO.setup(2,  GPIO.OUT, initial=GPIO.LOW)`	_### LED GPIO (GPIO2) set to output and low_

`GPIO.setup(4,  GPIO.OUT, initial=GPIO.LOW)`	_### LED GPIO (GPIO4) set to output and low_

`configure_gpio()`  

_### send 'next slide' command (launching) to remote (UI) slide deck_ 

class g:
xDisplay = "192.168.1.1"	_### placeholder for remote address_

pyautogui.platformModule._display = Xlib.display.Display (g.xDisplay)
pyautogui.moveTo (x=210, y=440)
pyautogui.click
time.sleep(5)

from __4Aspyx:__ import RClights1.py  

_### send 'next slide' command (scanning) to remote (UI) slide deck_

pyautogui.moveTo (x=210, y=595)  
pyautogui.click  

lights_on()
