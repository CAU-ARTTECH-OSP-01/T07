from flask import Flask, render_template, Response
from flask_bootstrap import Bootstrap
from camera import VideoCamera
import pymysql

app = Flask(__name__)
Bootstrap(app)

def connectsql():
    db = pymysql.connect(
                    host='localhost',
                    port = 3306,
                    user='root',
                    passwd='tiger',
                    db = 'mypage',
                    charset='utf8')
    return db

@app.route('/facialExpression')
def index():
    TITLE = 'Facial Expressions Recognition'
    return render_template('index.html', TITLE=TITLE)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def main():
    print("main page: get")
    return render_template('/main/main.html')


@app.route('/testCategories', methods=['GET'])
def testCate():
    print("testCategories: get")
    return render_template('/main/testCategories.html')

@app.route('/companies', methods=['GET'])
def companies():
    return render_template('/main/companies.html')

@app.route('/samsung', methods=['GET'])
def samsung():
    return render_template('/companies/samsung.html')

@app.route('/ai/mypage', methods=['GET'])
def mypage():
    return render_template('/main/mypage.html')

@app.route('/popup')
def popup():
    return render_template('/companies/popup.html')

@app.route('/questions')
def questions():
    conn = connectsql()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select questions from questions order by rand() limit 1"
    cursor.execute(sql)
    

    data_questions = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('/companies/questions.html',data_questions=data_questions)


@app.route('/interview', methods=['GET','POST'])
def interview():
    conn = connectsql()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select NO, DATE, context from interview"
    cursor.execute(sql)
    

    data_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('/main/interview.html',data_list=data_list)



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000, debug=True)
