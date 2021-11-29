import sounddevice as sd
from numpy import linalg as LA
import numpy as np

duration = int(input('the test: '))  

global cnt
global check_cnt
cnt = 0
check_cnt = 0

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
  
    # print (int(volume_norm))
 
    a = int(volume_norm)
    global cnt
    global check_cnt

    if a <= 25: # 어떻게 수정?
        cnt = cnt + 1;
    else: 
        cnt = 0; #정적이 끊길 시 초기화
    
    if cnt == 200: 
        check_cnt += 1;
        print ("You are too quiet!","Now you're checked", check_cnt, "times");
        cnt = 0; # cnt 초기화

    print("present count:", cnt, "present volume", a, "Check!", check_cnt) 
    
with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)