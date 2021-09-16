# Generalized Code

# Face Detection
api_key = ""
api_secret = ""
image_url = "https://contentblog.abaenglish.com/wp-content/uploads/2019/05/22012203/People-singular-or-plural-People-is-or-are.jpg"

import cv2
from google.colab.patches import cv2_imshow

import requests
request_url = "https://api-us.faceplusplus.com/facepp/v3/detect"
url = f'{request_url}?api_key={api_key}&api_secret={api_secret}&image_url={image_url}'

img = cv2.imread('person.jpg')

response = requests.request("POST",url)
n = response.json()['face_num']

for i in range(n):
  d = response.json()['faces'][i]['face_rectangle']
  x = d['left']
  y = d['top']
  h = d['height']
  w = d['width']
  crop_face = img[y:y+h,x:x+w]
  cv2.imwrite(f'Person{i}.jpg',crop_face)
  cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),5)

cv2_imshow(img)
