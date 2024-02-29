pip install opencv-python

pip install Jetson.GPIO

#	sudo groupadd -f -r gpio  
#	sudo usermod -a -G gpio  home directory_ 
 
pip3 install pyautogui	

# On Linux (Nano), you may need to install the scrot application and Tkinter, in the following order:

#	sudo apt-get install python3-tk     
#	sudo apt-get install python3-dev  
#	sudo apt-get install scrot  

import os 
import cv2
import time  
import numpy as np  
import glob	  
import sys	  
import pandas as pd  
import pathlib  
import Xlib  
import Jetson.GPIO as GPIO  
import pyautogui  
from threading import Thread  
from gi.repository import Gst, GObject  
import 4Aspyx

# gpio numbers set according to board pin layout_  

GPIO.setmode(GPIO.BOARD)

def configure_gpio():
  
  	GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)	### LEDs GPIO  (GPIO11) set to output and low  
	GPIO.setup(7,  GPIO.OUT, initial=GPIO.LOW)	### motor GPIO (GPIO7) set to output and low  
	GPIO.setup(2,  GPIO.OUT, initial=GPIO.LOW)	### LED GPIO (GPIO2) set to output and low  
	GPIO.setup(4,  GPIO.OUT, initial=GPIO.LOW)	### LED GPIO (GPIO4) set to output and low

configure_gpio()

# send 'next slide' command (launching) to remote (UI) slide deck 

class g:
xDisplay = "192.168.1.1"	### placeholder for remote address

pyautogui.platformModule._display = Xlib.display.Display (g.xDisplay)
pyautogui.moveTo (x=210, y=440)
pyautogui.click
time.sleep(5)

from 4Aspyx: import RClights1.py

# send 'next slide' command (scanning) to remote (UI) slide deck

pyautogui.moveTo (x=210, y=595)
pyautogui.click

lights_on()

from __4Aspyx: import RCdist1.py

print (d)		### d = number of seconds of capture device travel

from 4Aspyx: import RC2cameraCap.py

# RC2cameraCap.py captures synch frames from 2 CSI cameras and saves to separate folders

# send 'next slide' command (running) to remote (UI) slide deck

pyautogui.moveTo (x=210, y=750)
pyautogui.click

from 4Aspyx:import RCalertLED1s.py
from 4Aspyx: import RCmotor1.py

# these light green LED; run motor; alert if damage data is present by switching green LED off and red LED on;
# finally the motor is run in reverse, returning the capture device to it's point of origin

# send 'next slide' command (completed) to remote (UI) slide deck

pyautogui.moveTo (x=210, y=950)
pyautogui.click

time.sleep(10)

# send 'next slide' command (reset to first slide: 4Ax Technologies) to remote (UI) slide deck

pyautogui.moveTo (x=210, y=270)
pyautogui.click


GPIO.cleanup()



