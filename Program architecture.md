# rc1_run.py

The rc1_run.py program draws upon a diverse suite of libraries. One of these is __4Aspyx__, the 4Ax python plugin library.

__4Aspyx__ is not currently open source and the code offered below draws upon a number of __4Aspyx__ scripts. These scripts are unique to a particular use case and are therefore
currently confidential. However the overarching architecture is clearly defined below.


open cv2 and python 3.6 & 3.8 need to be installed on capture device/Hardware/Nano

debugging needs to be completed on a Linux computer or virtual environment as opencv-python wheel will not build on (e.g) Mac OS 10.15

the pyautogui script will work for HD (1920 x 1080) displays. In the event of a customer using a different display, this would need to be instantiated. Customers would be required to standardise their hardware (i.e not allow technicians to use their personal mobile/ tablet/ laptop).    

pip install opencv-python

pip install Jetson.GPIO

	sudo groupadd -f -r gpio
 
	sudo usermod -a -G gpio ### home directory
 
pip3 install pyautogui	

On Linux (Nano), you may need to install the scrot application, and Tkinter in the following order:

	sudo apt-get install python3-tk

	sudo apt-get install python3-dev

	sudo apt-get install scrot
	
from __4Aspyx__ import:
 
*	RCdist1.py
*	RCmotor1.py
*	RClights1.py
*	RCalertLED1s.py
*	RC2cameraCap1
*	RCDamageDetectnet50

__import glob__						
__import sys__						
__import pandas__ as __pd__					
__import pathlib__

import Jetson.GPIO as GPIO
from threading import Thread
from gi.repository import Gst, GObject
import cv2
import numpy as np
import pyautogui
import Xlib
import time
import os


GPIO.setmode(GPIO.BOARD)			# gpio numbers set according to board pin layout

def configure_gpio():
  
	GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)	# LEDs GPIO  (GPIO11) set to output and low
	GPIO.setup(7,  GPIO.OUT, initial=GPIO.LOW)	# motor GPIO (GPIO7) set to output and low
	GPIO.setup(2,  GPIO.OUT, initial=GPIO.LOW)	# LED GPIO (GPIO2) set to output and low
	GPIO.setup(4,  GPIO.OUT, initial=GPIO.LOW)	# LED GPIO (GPIO4) set to output and low

configure_gpio()
