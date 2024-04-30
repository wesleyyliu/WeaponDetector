Overview:
This project is a weapon detection model based off of the yolov5s object detection model. It is capable of real-time object detection at around 30-60fps with a GPU (on my CPU it is around 10-15 fps). The model is currently trained to detect knives, pistols, and rifles, and place bounding boxes around them.

The training data is pulled from two sources: 
https://github.com/ari-dasci/OD-WeaponDetection
https://github.com/Deepknowledge-US/US-Real-time-gun-detection-in-CCTV-An-open-problem-dataset/tree/gh-pages

The training data is around 7000 images and took a few days to train on multiple Google Colab sessions.

Code Structure:
datasetConversion.ipynb is a notebook that is used to filter the CCTV training data, since the training data is not very organized. As outlined in the notebook, it changes classes to fit my model training, separates the XML annotations into two different folders of jpgs and annotations, and also chooses around 10% of the dataset randomly since there were too many sample before. I then uploaded the filtered dataset to github to easily import to my Colab session (instead of uploading to drive, which is an alternative option).

WeaponDetection.ipynb is a notebook used to actually train the yolov5s object detection model. It uses a lot of short scripts and functions to coalesce all of the XML files into the right format, since some of them were not compatible with each other or were mislabeled. I then used PyLabel to convert the XML annotations into YOLO annotations that were compatible with the yolov5s training model, and then also used PyLabel to split the training data into train, validation, and test splits. I then trained the model.

detection.py is a short python function that runs the detect.py script in the yolov5 model to run inference on images and other files.

app.py is a quick flask app that accepts user file submissions, runs inferences, and then displays the result.

test.py has some tests to test the functionality of app.py

best.pt is the best model weights from my training.

Installation Instructions:

Simply activate the virtual environment, and then in the terminal, type:
export FLASK_APP=app.py
flask run

Then copy the development server link to the browser and submit files to run inferences on.
# WeaponDetector
# WeaponDetector
# WeaponDetector
