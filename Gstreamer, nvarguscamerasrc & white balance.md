# Gstreamer, nvarguscamerasrc & white balance

The Gstreamer manual is at: https://gstreamer.freedesktop.org/documentation/tutorials/basic/gstreamer-tools.html?gi-language=c
and https://gstreamer.freedesktop.org/documentation/  
The most concise way to glean information regarding best practice for preparing Gstreamer pipelines is to work on the Nvidia processor itself.
Use the command "$ gst-inspect-1.0 nvarguscamerasrc” to access factory details on the machine. 

A particularly significant capabability that is described in Pad Templates in the factory details is:

### wbmode         : White balance affects the color temperature of the photo

                        flags: readable, writable
                        
                        Enum "GstNvArgusCamWBMode" Default: 1, "auto"

(0): off              - GST_NVCAM_WB_MODE_OFF

(1): auto             - GST_NVCAM_WB_MODE_AUTO

(2): incandescent     - GST_NVCAM_WB_MODE_INCANDESCENT          (__2000k__)

(3): fluorescent      - GST_NVCAM_WB_MODE_FLUORESCENT          (__3000k__)

(4): warm-fluorescent - GST_NVCAM_WB_MODE_WARM_FLUORESCENT      (__2700k__)

(5): daylight         - GST_NVCAM_WB_MODE_DAYLIGHT		          (__6000k__)

(6): cloudy-daylight  - GST_NVCAM_WB_MODE_CLOUDY_DAYLIGHT	      (__6500k__)

(7): twilight         - GST_NVCAM_WB_MODE_TWILIGHT		          (__8000k__)

(8): shade            - GST_NVCAM_WB_MODE_SHADE		              (__10000k__)

(9): manual           - GST_NVCAM_WB_MODE_MANUAL

*  The (__kelvin colour temperature figures__) have been added to the factory details by 4Ax.

*  Some of the colour temperature figures vary somewhat depending on the reference source

*  It is noteworthy that a neutral __4000k__ setting is not provided (if you are looking for this perhaps try "(0): off" before using (9): manual")

*  The choice of mode setting will depend on the individual use case: location, hardware and training data.

### watch outs:

*  In the default "(1): auto" mode consider whether damage could potentially affect the white balance and thus cause a mismatch with training data: e.g crack damage to
the wall of an enclosed space could result in daylight entering the inspection area
   
*  "(9): manual" might look like an attractive option but it's default setting is unuseable: Gstreamer uses R:G:G:B values (Bayer-based) to set colour temperature 
and the default values are 0.5:0.5:0.5:0.5, which will cause under-exposed images with a strong green bias in most use cases. To work with this mode it is necessary
to adjust the values by trial and error and then re-compile the C++ file. 1.0:0.5:0.5:1.0 would be a better starting point, but some of these values will almost
certainly need to be further adjusted

*  Access __gstreamer__ samples such as userAutoWhiteBalance on the Jetson Nano at:   
/usr/src/jetson_multimedia/api/argus/samples

*  __Note deepstream__ samples for setting the streaming pipeline are at:  
/usr/src/jetson_multimedia/api/samples
