The Gstreamer manual is at: https://gstreamer.freedesktop.org/documentation/tutorials/basic/gstreamer-tools.html?gi-language=c
https://gstreamer.freedesktop.org/documentation/
The most efficient way to glean information regarding best practice for preparing Gstreamer pipelines is to work on the Nvidia processor itself.
Use the command "$ gst-inspect-1.0 nvarguscamerasrc” to access factory details on the machine. 

A particularly significant capabability that is described in Pad Templates in the factory details is:

wbmode         : White balance affects the color temperature of the photo
                        flags: readable, writable
                        Enum "GstNvArgusCamWBMode" Default: 1, "auto"

(0): off              - GST_NVCAM_WB_MODE_OFF
(1): auto             - GST_NVCAM_WB_MODE_AUTO
(2): incandescent     - GST_NVCAM_WB_MODE_INCANDESCENT		  2000k
(3): fluorescent      - GST_NVCAM_WB_MODE_FLUORESCENT	          3000k
(4): warm-fluorescent - GST_NVCAM_WB_MODE_WARM_FLUORESCENT	  2700k
(5): daylight         - GST_NVCAM_WB_MODE_DAYLIGHT		  6000k
(6): cloudy-daylight  - GST_NVCAM_WB_MODE_CLOUDY_DAYLIGHT	  6500k
(7): twilight         - GST_NVCAM_WB_MODE_TWILIGHT		  8000k
(8): shade            - GST_NVCAM_WB_MODE_SHADE		          10000k
(9): manual           - GST_NVCAM_WB_MODE_MANUAL

The kelvin colour temperature figures have been added.
Some of these figures are somewhat contested by rival online resources
It is unfortunate (some might say an oversight) not to provide a neutral 4000k setting (try "(0): off"
The choice of mode setting will depend on the individual use case: location, hardware and training data.

2 watch outs:
*  Consider whether damage could potentially cause a mismatch with training data if in "(1): auto" mode
*  The default setting for "(9): manual" is unuseable: Gstreamer uses R:G:G:B values (Bayer-based) to set colour temperature 
and the default values are 0.5:0.5:0.5:0.5, which will cause under-exposed images with a strong green bias in most cases
