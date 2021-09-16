import requests
from pprint import pprint
token = ' '
with open('car.jpg', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        files=dict(upload=fp),
        headers={'Authorization':'Token '})
pprint(response.json())

# Write Token <api_key>

d = response.json()['results'][0]['box']
text = response.json()['results'][0]['plate'].upper()


font_scale = 0.5
font = cv2.FONT_HERSHEY_DUPLEX
import numpy as np
img = cv2.imread('car.jpg')
# set the rectangle background to white
rectangle_bgr = (235, 137, 52)
(text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=2)[0]
# set the text start position
text_x = d['xmin']
text_y = d['ymin']
# make the coords of the box with a small padding of two pixels
box_coords = ((text_x, text_y), (text_x + text_width + 2, text_y - text_height - 2))
cv2.rectangle(img, box_coords[0], box_coords[1], rectangle_bgr, cv2.FILLED)
cv2.rectangle(img,(d['xmin'],d['ymax']),(d['xmax'],d['ymin']),(235, 137, 52),3)
cv2.putText(img, text, (text_x, text_y), font, fontScale=font_scale, color=(255, 255, 255), thickness=2)
cv2_imshow(img)
