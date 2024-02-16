# Deployment on the edge device

The network model was trained on Nvidia's TAO Toolkit, which generates a .tlt format file that is optimised for inference on the target device.  

The training process included the generation of an encryption key, which is used to encrypt the model during conversion to an .etlt file to be used in the edge capture device. 
The same key is required for decryption during inference. The TAO Toolkit provides a link for downloading the converter.  


The encrypted .etlt model file was then transferred to the Jetson Nano inside the edge device with the decryption key securely stored on board. Security protocols for loading 
the key are handled within the RCalertLEDs1.py script. The capture device was then tested for performance and security.

