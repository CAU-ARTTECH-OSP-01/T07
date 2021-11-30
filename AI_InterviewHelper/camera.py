import cv2
from model import FacialExpressionModel
import sys
import numpy as np
from bs4 import BeautifulSoup 


facec = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
model = FacialExpressionModel("model.json", "model_weights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX
eyestreec = cv2.CascadeClassifier('Haarcascades/haarcascade_eye_tree_eyeglasses.xml')
eyesc = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
global cnt
cnt=0


class VideoCamera(object):
    def __init__(self):
        #self.video = cv2.VideoCapture('facial_exp.mkv')
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    # returns camera frames along with bounding boxes and predictions
    def get_frame(self):
        _, fr = self.video.read()
        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        faces = facec.detectMultiScale(gray_fr, 1.3, 5)

        global cnt

        for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w]

            roi = cv2.resize(fc, (48, 48))
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])            
            cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)
            eyes = eyesc.detectMultiScale(gray_fr,1.3,5,minSize=(50, 50))
            if len(eyes)>=2:
                for(ex,ey,ew,eh) in eyes:
                    cnt= cnt + 1
                    #print("you've blinked ",int(cnt/2)," times")
                    blinktxt= "you've blinked "+str(cnt/2)+" times"
                    with open('templates/companies/popup.html') as html_file:
                        soup = BeautifulSoup(html_file.read(), features="html.parser")
                        for tag in soup.find_all(id='blinkcnt'):
                            tag.string.replace_with("you have blinked "+str(int(cnt/2))+" times")
                        new_text = soup.prettify()
                    with open('templates/companies/popup.html', mode='w') as  new_html_file:
                        new_html_file.write(new_text)
            cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
            
            

        _, jpeg = cv2.imencode('.jpg', fr)
        return jpeg.tobytes()

