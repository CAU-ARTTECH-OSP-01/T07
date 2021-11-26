"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import time
import numpy as np
import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
blinkingState = []
count = 0
start = time.time()
# 출처: https://blockdmask.tistory.com/549 [개발자 지망생]

# 출력문: n초동안 m번 깜박였습니다. n초동안 평균 눈 깜박임 회수는 20 / 60 * n입니다. 
# if문: 평균보다 많이 깜박였으니 이 부분에 유의하세요.

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""
    
    if gaze.is_blinking():            
        text = "Blnking"
        blinkingState.append(1)
    else:
        blinkingState.append(0)
        
    if len(blinkingState) == 2:
        if blinkingState[1] - blinkingState[0] == -1:
            count += 1
            print("카운트 됨")
        else:
            print("blinkingState = [" + str(blinkingState[0]) + ", " + str(blinkingState[1]) + "]")
        del blinkingState[0]

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    # 눈동자 좌표 좌측 상단에 표시
    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
       break
   
webcam.release()
end = time.time()
average = (20/60*(end-start))
print(f"{end - start:.2f}초동안 " + str(count) + "번 깜빡였습니다.")
print("해당 시간동안의 평균 눈깜박임 횟수는" + f" {average: .2f}회입니다.")
if count > average:
    print("평균보다 눈을 더 많이 깜박이고 있으니 유의하세요.")
cv2.destroyAllWindows()
