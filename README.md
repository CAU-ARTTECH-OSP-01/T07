# T07 AI Interview Helper
> Due to the Covid, many companies have changed their recruition by having AI interview.  
# 

## #Installation

```
    pip install Flask 
    pip install Flask-Bootstrap
    pip install opencv-python
    pip install numpy
    pip install speechrecognition
    pip install sounddevice
    pip install tensorflow
    pip install cv2
    
    Also We used Oracle MySql for database 
```
    
## #.xml
> You will need 2 haarcascade file. 
```
    haarcascade_frontalface_default.xml
    haarcascade_eye.xml
```
> These two xml file is in Haarcascades file in AI_InterviewHelper file 
    


# 1. How To Use Flask 
~~~
from flask import Flask, render_template, Response, session, url_for, request,redirect
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def main():
    return render_template('/main/main.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000, debug=True)
~~~


# +,-,\* 을 통해 tab으로 출력하기

- 안녕
  - Hi
    - Hello

* 안녕
  - Hi
    - Hello

- 안녕
  - Hi
    - Hello

# 수평선 만들기

---

    프로젝트

---

    Project
