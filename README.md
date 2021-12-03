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
```
> Also We used Oracle MySql for database 
    <img src="https://user-images.githubusercontent.com/93374409/144154665-89458a8b-9ff9-4299-9117-794a5d3d0d06.png" width="300" height="auto">
    
    
    
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


# Using MySql 
    We needed 3 database table
    - 1. User information 
    ~~~
    CREATE TABLE tbl_user(
        user_name not null varchar2(255) primary key,
        user_pw not null varchar2(255) 
    )
    ~~~
    <br>
    - 2.interview table
    ~~~
    CREATE TABLE interview(
        NO int not null auto_increment primary key,
        id varchar2(255) not null, //<- this is going to be joining with the tbl_user table
        DATE timestamp not null,
        context varchar(100)
        );
    ~~~

    <br>
    - 3.Questions table
    ~~~
        CREATE TABLE questions(
            NO int not null auto_increment primary key,
            companies varchar(100),
            questions varchar(500)
        );
    ~~~



# 수평선 만들기

---

    프로젝트

---

    Project
