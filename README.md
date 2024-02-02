# capture_device1 

capture_device1 is a framework for the semi-automated capturing of data from inaccessible locations where the use of drones is too slow and expensive. It uses an object detection network (resnet50 backbone) trained on the the 4Ax damage0.2 database to infer real-time analysis of it's surroundings and identify damage. Unlike drone footage no data cleaning is required, thus real-time analysis is possible. The framework can also operate in fully-autonomous mode, where the location infrastructure supports this mode. The Jetson Nano-based MVP was completed in 2022. In the 2024 production-ready variant the processor is the Jetson Orin Nano.

Information is provided here on:
  Gstreamer, nvarguscamerasrc & white balance
  damagedetect50 network model
  rc1_run.py program architecture
