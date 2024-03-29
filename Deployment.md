# Deployment on the edge device

The network model was trained on Nvidia's [TAO Toolkit](https://developer.nvidia.com/tao-toolkit), which generates a .tlt format file that is optimised for inference on the target device.  

The training process included the generation of an encryption key, which is used to encrypt the model during conversion to an .etlt file to be used in the edge capture device. 
The same key is required for decryption during inference. The TAO Toolkit provides a link for downloading the converter.  
![security_key](https://github.com/4Ax-Technologies/capture_device1/assets/90104815/4684477d-1018-47ba-85d8-16b3754d4d73)
The encrypted .etlt model file was then transferred to the Jetson Nano inside the edge device with the decryption key securely stored on board. Security protocols for loading 
the key are handled within the RCalertLEDs1.py script. The capture device was then tested for performance and security.

### Performance  

After verifying that performance on the original holdback dataset was unchanged, the network was deployed on new data. Performance similar to that described in 
[__Network model.md__](https://github.com/4Ax-Technologies/capture_device1/blob/main/Network%20model.md) was achieved here on the new data.

### Security

No security issues have currently been identified. Monitoring of this will be ongoing.

