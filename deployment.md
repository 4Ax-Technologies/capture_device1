# Deployment on the edge device

The network model was trained on Nvidia's TAO Toolkit, which generates a .tlt format file that is optimised for inference on the target device.
Generate Encryption Key:
Generate an encryption key that will be used to encrypt the model during conversion. This key will also be required for decryption during inference on the target device.
Convert .tlt to .etlt:
Use the Transfer Learning Toolkit to convert your .tlt model to a key-encrypted .etlt model. This process involves specifying the encryption key generated in the previous step.
Deploy to Jetson Nano:
Transfer the encrypted .etlt model file to your Jetson Nano device. Make sure you have the necessary environment set up on the Jetson Nano for running inference with encrypted models.
Decryption Key Handling:
Ensure that the decryption key is securely stored on the Jetson Nano device. You may want to integrate mechanisms to securely load and handle the decryption key during inference.
Inference with Encrypted Model:
Develop or modify your inference application on the Jetson Nano to load and execute the encrypted .etlt model. Ensure that the decryption key is used to decrypt the model during inference.
Testing and Validation:
Test your deployment thoroughly to ensure that the encrypted model performs as expected on the Jetson Nano. Validate both the performance and security aspects of the deployment.
By following these steps, you'll be able to convert your .tlt model into a key-encrypted .etlt model for deployment on a Jetson Nano, ensuring both performance and security in your edge device deployment.
