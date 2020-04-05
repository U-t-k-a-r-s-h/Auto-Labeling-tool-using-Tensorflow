# Auto-Labeling-tool-using-tensorflow
This tools lets the user to browse the images and then runs the pre-trained deep neural network model taking the image as input, which gives the output corresponding to the objects present in the image. We can also set the threshold for the detection.
# Libraries required:
PySimpleGUI,
cv2,
PIL,
numpy,
Tensorflow,
object_detection.utils (Setup the object detection protos)
# GUI (Pysimplegui)
To create the Graphical User Interface i have used pysimplegui library of python which provides an easy way for the user to navigate the images and run the model.
# Tensorflow frozen graphs
As a means of transefer learning we are directly using the tensorflow's frozen graph model which gives the already trained model ready for direct evaluation on the images.
for simplicity and fast runtime i have used the mobilenet light version of the tensorflow.
# Number of detectable classes
Currently there are 90 detectable classes which can be detected in any image.
# How to setup:
# step 1:
install tensorflow and create an environment to work
# step 2:
install the above given libraries
# step 3:
setup the object detection protobuf and add it to the path (you can check out number of tutorials for that)
# step 4:
in a single folder unzip the files of this diretory and make sure that label.pbtxt and Mobilenet.pb are there
# step 5:
open the TensorflowScript.py and make sure that # PATH_TO_LABELS is initialised with the correct path to your label.pbtxt file
# step 6: 
Run the GUI.py script and make sure that all the above steps have been successfully completed.
# step 7:
select the directory containing the image and detect the labels.
