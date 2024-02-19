# DamageDetectnet50

![database_collage_final](https://github.com/4Ax-Technologies/capture_device1/assets/90104815/3891e9af-66ed-4324-8eb5-f9847d1eec2d)

## DamageDetectnet50 is a detectnet_v2 50 layer network model retrained on 4Ax's damage0.2 database 

__damage0.2__ comprises a mixture of real-world curated images and diffusion-generated synthetic data. In training the database was further
augmented using standard data augmentation techniques.

### Training
Damage used for training included cracking of various types and sizes, deep scorching caused by lightning strikes and a range of delamination 
instances. 100+ network hyperparameters were tuned through iterative tweaks to the configuration file. Initially "healthy" and "damage" 
classes were used, but it turns out that end-users are only interested in whether damage is present: "healthy" is considered the norm. Therefore 
the damage0.2  database uses a single class, where each image has a matching label, consisting of coordinates of the damage bounding box. In 
practice this is the x and y pixel coordinates of the top left and bottom right corners. Early (2 class) training limited the number of training 
epochs to 10, but by the time the single class strategy was adopted precision scores in the evaluation phase of 90%+ were routinely achieved. 
The number of training epochs was therefore gradually increased along with corresponding reductions to the learning rate over a greater proportion 
of training in the earlier and very late stages until 93% was routinely achieved during 30+ epochs of training, best performance generally occurred 
between the 10th and 25th epochs. 

At this point only 2 main parameters were still being tweaked, one of which was the pixel resolution to which the model resized training data 
before training commenced. Moving from 1/4 x 1/4 of the capture device resolution, through 1/3 x 1/3, then 1/2 x 1/2 resizing brought significant
improvements in precision while remaining within operating capabilities.  

### Testing and results
The top five performing models in precision evaluation were then tested with the holdback test dataset and the resulting images in each case 
were assessed. It was noted that a single 1/3 x 1/3 50 epoch instance achieved a precision score of 95.108%, while the next 4 models were all 
1/2 x 1/2 60 epoch models and yielded results between 93.5988% and 93.6243%. The holdback test subset consisted of a 50/50 split of "healthy" and 
"damage" data.

The results demonstrated that for this specific use case accuracy (getting the class right) was significantly more important than precision (drawing 
the bounding box in exactly the right place). In an autonomous vehicle application precision would be more important. The 95.108% model demonstrated 
a disappointingly high predisposition to false negative inferences (nearly 50% of the time) when presented with data containing damage; it was also 
similarly imprecise when it came to classifying healthy data, again inferring nearly 50% false positives.

A 93.5988% precision model delivered 100% accuracy, but this achievement was undermined by an unacceptably high tendency (nearly 60%) 
to infer false positives (predicting damage when there was none). This would quickly become irritating for the inspection technician, who would 
feel personally validated when occasionally being required to step in to overrule the network, but not in 60% of cases.

The best results were achieved by one of the two 93.6243% precision models. While it also exhibited 100% accuracy, it demonstrated a much lower 
tendency (below 20%) to infer false positives. Occasionally the bounding box that the model overlaid onto damage did not intersect precisely. 
However the accuracy of the highest-performing retrained DamageDetectnet50 network is remarkable, clearly demonstrating the value of transfer 
learning when applied to a detectnet_v2 network, and overall the implementation of this network would represent a significant lightening of the 
current burden on human resources in the particular use case.
