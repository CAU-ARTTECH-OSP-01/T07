import cv2
from model import FacialExpressionModel
import sys
import numpy as np
from bs4 import BeautifulSoup 

#This program counts blinking eyes.
#Copyright (C) 2020 SatYu26

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

#Date of modification: 2021.12.20
#Modification: The accuracy of the counter was improved by adding 
#the list blinkingState, and the rectangle displaying 
#the eye was removed.

#Contact: eysl018@icloud.com

facec = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
model = FacialExpressionModel("model.json", "model_weights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX
eyestreec = cv2.CascadeClassifier('Haarcascades/haarcascade_eye_tree_eyeglasses.xml')
eyesc = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
global cnt
cnt=0
global blinkingState
blinkingState = []


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
        fr = cv2.flip(fr, 1)
        
        global cnt

        for (x, y, w, h) in faces:
            k = 1

            fc = gray_fr[y:y+h, x:x+w]
            roi = cv2.resize(fc, (48, 48))
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])            
            cv2.rectangle(fr,(x,y),(x+w,y+h),(255,0,0),2)
            eyes = eyesc.detectMultiScale(gray_fr,1.3,5,minSize=(50, 50))
            
            for (ex,ey,ew,eh) in eyes:
                k = 0

            if k == 1: # 눈 감은 상태 감지
                blinkingState.append(1)
                #print("Blinking!") -> 세부 기능 잘 실행되고 있는지 실시간 확인용 1 (눈을 감았을 경우가 잘 감지되는가?)
            else: # 눈 뜬 상태 감지
                blinkingState.append(0)
                #print("Not Blinking!") -> 실시간 확인용 2 (눈 뜬 상태가 잘 감지되는가?)
        
            if len(blinkingState) == 2:
                if blinkingState[1] - blinkingState[0] == -1:
                    cnt += 1
                    print("you've blinked " + str(cnt) + " times") # -> 실시간 확인용 3 (제대로 count되고 있는가?)
                del blinkingState[0]
                
                with open('templates/companies/popup.html') as html_file:
                    soup = BeautifulSoup(html_file.read(), features="html.parser")
                    for tag in soup.find_all(id='blinkcnt'):
                        tag.string.replace_with("you have blinked "+str(cnt)+" times")
                    new_text = soup.prettify()
                with open('templates/companies/popup.html', mode='w') as  new_html_file:
                    new_html_file.write(new_text)

            cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)

        _, jpeg = cv2.imencode('.jpg', fr)
        return jpeg.tobytes()

