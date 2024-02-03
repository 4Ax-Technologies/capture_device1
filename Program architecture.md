# rc1_run.py

The rc1_run.py program draws upon a diverse range of libraries. One of these is 4Aspyx, the 4Ax python plugin library.

4Aspyx is not currently open source and the code offered below draws upon a number of 4Aspyx scripts. These scripts are unique to a particular use case and are therefore
currently confidential. However the underlying architecture is clearly defined.


open cv2 and python 3.6 & 3.8 need to be installed on capture device/Hardware/Nano
debugging needs to be completed on Linux computer as opencv-python wheel will not build on (e.g) Mac OS 10.15
the pyautogui script will work for HD (1920 x 1080) displays. In the event of a customer using a different display, this would be instantiated. Customers would be required to standardise their hardware (i.e not allow technicians to use their personal mobile/tablet/laptop).    

pip install opencv-python
pip install Jetson.GPIO
	sudo groupadd -f -r gpio
	sudo usermod -a -G gpio # home directory
pip3 install pyautogui	

On Linux (Nano), you may need to install the scrot application, and Tkinter in the following order:

sudo apt-get install python3-tk
sudo apt-get install python3-dev		
sudo apt-get install scrot
	
from 4Aspyx import RCdist1.py, RCmotor1.py, RClights1.py, RCalertLED1s.py, RC2cameraCap1, RCDamageDetectnet50
