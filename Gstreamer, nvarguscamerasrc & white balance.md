# Gstreamer, nvarguscamerasrc & white balance

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

(2): incandescent     - GST_NVCAM_WB_MODE_INCANDESCENT          (__2000k__)

(3): fluorescent      - GST_NVCAM_WB_MODE_FLUORESCENT          (__3000k__)

(4): warm-fluorescent - GST_NVCAM_WB_MODE_WARM_FLUORESCENT      (__2700k__)

(5): daylight         - GST_NVCAM_WB_MODE_DAYLIGHT		          (__6000k__)

(6): cloudy-daylight  - GST_NVCAM_WB_MODE_CLOUDY_DAYLIGHT	      (__6500k__)

(7): twilight         - GST_NVCAM_WB_MODE_TWILIGHT		          (__8000k__)

(8): shade            - GST_NVCAM_WB_MODE_SHADE		              (__10000k__)

(9): manual           - GST_NVCAM_WB_MODE_MANUAL

*  The (__kelvin colour temperature figures__) have been added to the factory details by 4Ax.

*  Some of the colour temperature figures may vary somewhat depending on the online source

*  It is unfortunate (some might say an oversight) not to provide a neutral 4000k setting (try "(0): off")

*  The choice of mode setting will depend on the individual use case: location, hardware and training data.

### 2 watch outs:

*  Consider whether damage could potentially affect the white balance and thus cause a mismatch with training data if in
"(1): auto" mode
   
*  "(9): manual" might look like an attractive option but it's default setting is unuseable: Gstreamer uses R:G~even~:G~odd~:B values (Bayer-based) to set colour temperature 
and the default values are 0.5:0.5:0.5:0.5, which will cause under-exposed images with a strong green bias in most use cases
