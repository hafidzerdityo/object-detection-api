from ultralytics import YOLO
import ultralytics
import os 
import numpy as np
from io import BytesIO
from PIL import Image
import base64
import cv2
from PIL import Image


os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
ultralytics.checks()

model = YOLO('./saved_models/best_rumah.pt')

# def convert_image_b64str(path):
#     with open(path, "rb") as img_file:
#         img_b64 = base64.b64encode(img_file.read())
#     img_str = img_b64.decode('ascii')
#     return img_str

def predict_house(img_path_or_matrix) -> dict:
    dict_output = {
        'confidence': '',
        'result': '',
        'bboxes': ''
    }
    results = model.predict(img_path_or_matrix, conf=0.4, verbose=False)  
    try:
        dict_output['confidence'] = results[0].boxes.conf.tolist()
    except:
        dict_output['confidence'] = [0]
    boxes = results[0].boxes
    box = boxes  
    dict_output['bboxes'] = box.xyxy.tolist()

    if dict_output['bboxes']:
        dict_output['result'] = True 
    else:
        dict_output['result'] = False

    return dict_output

def predict_house_b64(img_b64str: str, b64_return: bool) -> dict:
    dict_output = {
        'bboxes': '',
        'confidence': '',
        'result': '',
        'image_predicted_b64': ''
    }
    try:
        orgimg = Image.open(BytesIO(base64.b64decode(img_b64str)))
    except:
        return {'error': 'cannot identify the given base64 string'}
    results = model.predict(orgimg, max_det=50, conf=0.5)  

    dict_output['confidence'] = results[0].boxes.conf.tolist()
    boxes = results[0].boxes
    box = boxes 
    dict_output['bboxes'] = box.xyxy.tolist()
    if dict_output['bboxes']:
        dict_output['result'] = True 
    else:
        dict_output['result'] = False

    
    if dict_output['result']:
        if b64_return:
            annotation_color = (53, 23, 247)
            img = cv2.cvtColor(np.array(orgimg), cv2.COLOR_RGB2BGR)
            for each_box, each_conf in zip(dict_output['bboxes'], dict_output['confidence']):
                x1,y1,x2,y2 = each_box
                cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), annotation_color, 3)
                cv2.putText(img,f"House: {round(each_conf* 100,2)}%",(int(x1), int(y1) - 10),fontFace = cv2.FONT_HERSHEY_SIMPLEX,fontScale = 0.6,color = annotation_color,thickness=2)
            img = cv2.imencode('.jpg', img)[1].tobytes()
            b64_str_out = base64.b64encode(img).decode('ascii')
            dict_output['image_predicted_b64'] =  b64_str_out
    return dict_output


