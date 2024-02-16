# capture_device1 

capture_device1 is a framework for the semi-automated capturing of data from inaccessible locations where the use of drones is too slow and expensive. It uses an object detection network (resnet50 backbone) trained on the the 4Ax damage0.2 database to infer real-time analysis of it's surroundings and identify damage. Unlike drone footage no data cleaning is required, thus real-time analysis is possible. The framework can also operate in fully-autonomous mode, where the location infrastructure supports this mode. The Jetson Nano-based MVP was completed in 2022. In the 2024 production-ready variant the processor is the Jetson Orin Nano.

![database_collage_final](https://github.com/4Ax-Technologies/capture_device1/assets/90104815/3891e9af-66ed-4324-8eb5-f9847d1eec2d)

### Information is provided here on:

[__Gstreamer, nvarguscamerasrc & white balance__] (https://github.com/4Ax-Technologies/capture_device1/blob/main/Gstreamer%2C%20nvarguscamerasrc%20%26%20white%20balance.md)
  
__damagedetect50 network model__
  
__rc1_run.py program architecture__
