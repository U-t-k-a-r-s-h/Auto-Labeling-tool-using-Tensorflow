import numpy as np
import tensorflow as tf
import cv2 as cv
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
import os
# Read the graph.
def Detector(img_directory,Threshold,model):
    NUM_CLASSES = 90
    os.system('cls')
    PATH_TO_LABELS = 'label.pbtxt'
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    with tf.io.gfile.GFile(model, 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())

    with tf.compat.v1.Session() as sess:
        # Restore session
        sess.graph.as_default()
        tf.import_graph_def(graph_def, name='')

        # Read and preprocess an image.
        img = cv.imread(img_directory)
        rows = img.shape[0]
        cols = img.shape[1]
        inp = cv.resize(img, (300, 300))
        inp = inp[:, :, [2, 1, 0]]  # BGR2RGB
    
        # Run the model
        out = sess.run([sess.graph.get_tensor_by_name('num_detections:0'),
                        sess.graph.get_tensor_by_name('detection_scores:0'),
                        sess.graph.get_tensor_by_name('detection_boxes:0'),
                        sess.graph.get_tensor_by_name('detection_classes:0')],
                       feed_dict={'image_tensor:0': inp.reshape(1, inp.shape[0], inp.shape[1], 3)})
    
        # Visualize detected bounding boxes.
        num_detections = int(out[0][0])
        for i in range(num_detections):
            classId = int(out[3][0][i])
            score = float(out[1][0][i])
            bbox = [float(v) for v in out[2][0][i]]
            if score > Threshold:
                x = bbox[1] * cols
                y = bbox[0] * rows
                right = bbox[3] * cols
                bottom = bbox[2] * rows
                cv.rectangle(img, (int(x), int(y)), (int(right), int(bottom)), (125, 255, 51), thickness=2)
                font = cv.FONT_HERSHEY_SIMPLEX 
  
                org = (int(x),int(y))  
                fontScale = 0.7
                color = (255, 0, 0) 
                thickness = 1
                img = cv.putText(img,str(category_index.get(classId).get('name')),org,font, fontScale,color ,thickness, cv.LINE_AA)
                print('SCORE:',score, ', Class:',category_index[classId])
    cv.imwrite('Temp.jpg',img)