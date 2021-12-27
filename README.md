# T07 AI Interview Helper

> Due to the Covid, many companies have changed their recruition by having AI interview.
> Website : https://sites.google.com/view/osp-team-07/2021-02/01/team_07

## #Installation

```
    pip install Flask
    pip install Flask-Bootstrap
    pip install opencv-python
    pip install numpy
    pip install sounddevice
    pip install tensorflow
    pip install cv2
    pip install beautifulsoup4
    pip install cryptography
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

---

```
from flask import Flask, render_template, Response, session, url_for, request,redirect
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def main():
    return render_template('/main/main.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000, debug=True)
```

# 2. Using MySQL

---

> We needed 3 database table
>
> 1.  User information

```
  CREATE TABLE tbl_user(
    user_name varchar(255) not null primary key,
    user_password varchar(255) not null
    );
```

> 2.interview table

```
    CREATE TABLE interviews(
        NO int not null auto_increment primary key,
        id varchar(255) not null,
        DATE TIMESTAMP ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        blinkcnt varchar(500),
        voiceleveltext varchar(500)
    );
```

> 3.Questions table

    CREATE TABLE questions(
        NO int not null auto_increment primary key,
        companies varchar(100),
        questions varchar(500)
    );

# Question Lists

"samsung","What kind of person will you be within next 10 years?" <br/>
"samsung","What will you do if you have a different opinion with your suprior?" <br/>
"samsung","Tell me your biggest merit"<br/>
<br/><br/>
"google","Imagine if we are your nephew. \nTell us about database" <br/>
"google","What is your favorite Google product? And why?" <br/>
"google","Why do you want to work for Google?"<br/>
