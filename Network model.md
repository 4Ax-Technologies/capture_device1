# DamageDetectnet50

DamageDetectnet50 is a detectnet_v2 50 layer network model retrained on 4Ax's damage0.2 database using appropriate data augmentation.

Damage used for training included cracking of various types and sizes, deep scorching caused by lightning strikes and a range of delamination 
instances. Approximately 100 configuration variables were tested through iterative tweaks to the configuration file. "Healthy" and "damage" 
classes were used initially, but it turns out that end-users are only interested in whether damage is present. Therefore the damage0.2 database 
uses a single class, where each image has a matching label, consisting of coordinates of the damage bounding box. In practice this is the x and 
y coordinates (in pixels) of the top left and bottom right corners. Early (2 class) training limited the number of training epochs to 10, but by 
the time the single class was implemented precision scores in the evaluation phase of 90%+ were routinely bring achieved. The number of train 
epochs was therefore gradually increased until 93% was routinely achieved during 30 epochs of training, generally occurring between the 10th and 
25th epochs. 

At this point only 2 main parameters were still being tweaked, one of which was the pixel resolution to which the model resized training data 
before training commenced. Moving from 1/4 x 1/4 of the capture device resolution, through 1/3 x 1/3, then 1/2 x 1/2 resizing brought significant
improvements in precision while remaining within operating capabilities. 

The top five performing models in precision evaluation were then tested with the holdback test material and the resulting images in each case 
were assessed. It was noted that a single 1/3 x 1/3 50 epoch instance achieved a precision score of 95.108%, while the next 4 models were all 
1/2 x 1/2 60 epoch models and yielded results between 93.6243% and 93.5988%. The results demonstrated that for this specific used case accuracy 
(getting the class right) was more important than precision (drawing the bounding box in exactly the right place). In an autonomous vehicle 
application precision would be more important.

The test folder contained a 50/50 split of "healthy" and "damage" data. The 95.108% model demonstrated a disappointingly high predisposition 
(nearly 50% of the time) to false negative inferences when presented with data containing damage; it was also similarly imprecise when it came 
to classifying healthy data, with nearly 50% false positives.

A 93.5988% precision model delivered 100% accuracy, but this achievement was somewhat undermined by an unacceptably high tendency (nearly 60%) 
to infer false positives (predicting damage when there was none).

The best results were achieved by one of the two 93.6243% precision models. It exhibited 100% accuracy. It exhibited a more modest tendency 
(around 20%) towards inferring false positives. Occasionally the bounding box that the model overlaid onto damage did not intersect precisely. 
However the accuracy is remarkable and overall the implementation of this network would represent a significant lightening of the current burden 
on human resources in the particular use case.
