import sounddevice as sd
from numpy import linalg as LA
import numpy as np
from jinja2 import Environment, FileSystemLoader
duration = 20  # seconds <- duration 자체를 짧게 끊어서 본 지속시간동안 cnt 값이 일정 수준 이상 증가하면 check가 이루어질 수 있도록 하는 것은?

global cnt
global check_cnt
cnt = 0
check_cnt = 0

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10# 초기값 10 > 5로 변화 주었을 때 출력 값이 절반 정도로 보여짐
  
    # time data는 프로그램이 실행되었을 때 시간을 나타내므로 현재 시간과는 무관한 정보
    # frames의 경우 고정된 값
    # print (int(volume_norm))
 
    a = int(volume_norm)
    global cnt
    global check_cnt

    if a <= 28: # 정적 시 값이 환경에 따라 달라지므로 매번 새로 구해야 할 필요성 존재-> 통상적으로 어느정도 큰 목소리로 말할때 30을 넘기 때문에 고정값 28+_1 을 해도 될 것 같음.
        cnt = cnt + 1
    
    if cnt == 300: # duration = 20일 경우 cnt = 771까지 기록되어질 수 있음
        check_cnt += 1
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('companies/popup.html')
        text = "You are too quiet! Now you're checked "+str(check_cnt)+" times"
        output_from_parsed_template = template.render(test=text)
        print(output_from_parsed_template)

        with open("templates\companies\popup.html", "w") as fh:
            fh.write(output_from_parsed_template)
        cnt = 0; # cnt 초기화
        
    
    #print("present count:", cnt, "present volume", a, "Check!", check_cnt) #print 되는 속도를 늦추거나 혹은 측정 속도를 늦출 수 있는 방법은?
    # if check_cnt >= 1:
        # print ("present check:", check_cnt);
    

# Stream 특성상 cnt가 계속 반복문에 걸리면서 증가하는 것이 아닌, 계속 실시간으로 print_sound 자체가 실행되는 것이기 때문에 +1만이 이루어짐. -> 전역 변수 사용으로 1차 해결

