import sounddevice as sd
from flask import Flask, render_template, Response, session, request, redirect, url_for
from flask_bootstrap import Bootstrap
from camera import VideoCamera
import pymysql
from PythonApplication1 import print_sound
from voicerecognition import voiceReco

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

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



@app.route('/aud')
def audio():
    with sd.Stream(callback=print_sound):
        duration = 20
        sd.sleep(duration * 1000)
    return render_template("/companies/test.html")

@app.route('/')
def main():
    print("main page: get")
    
    if 'username' in session:
        username = session['username']

        return render_template('/main/main.html', logininfo = username)
    else:
         username = None
         return render_template('/login/login.html', logininfo = username )
    



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

@app.route('/mypage', methods=['GET'])
def mypage():
    if 'loggedin' in session:
        conn = connectsql()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECt * FROM tbl_user WHERE user_name =%s', (session['username']))
        account = cursor.fetchone()
        return render_template('/main/mypage.html', account=account)
    
    return redirect(url_for('login'))

@app.route('/popup', methods=["GET"])
def popup():
    if 'loggedin' in session:
        conn = connectsql()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECt * FROM tbl_user WHERE user_name =%s', (session['username']))
        account = cursor.fetchone()
        return render_template('/companies/popup.html', account=account)
    return redirect(url_for('login'))

@app.route('/questions', methods=["GET","POST"])
def questions():
    if request.method=='POST':
        id = request.form['id']
        blinkcnt = request.form['blinkcnt']
        voiceleveltext = request.form['voiceleveltext']
        conn = connectsql()
        cursor = conn.cursor()
        sql = "INSERT INTO INTERVIEWS (id, blinkcnt, voiceleveltext) VALUES (%s, %s, %s)"
        value = (id, blinkcnt, voiceleveltext)
        cursor.execute(sql, value)
 
        data = cursor.fetchall()
        conn.commit()
        return redirect(url_for('questions'))

    else:
        conn = connectsql()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "select questions from questions order by rand() limit 1"
        cursor.execute(sql)
        data_questions = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template('/companies/questions.html',data_questions=data_questions)


@app.route('/interview/<user_name>', methods=['GET','POST'])
def interview(user_name):
    conn = connectsql()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select * from interviews"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('/main/interview.html',data_list=data_list)

@app.route('/logout')
# username 세션 해제
def logout():
    session.pop('loggedin',None)
    session.pop('username', None)
    return redirect(url_for('main'))

@app.route('/login', methods=['GET','POST'])
# GET -> 로그인 페이지 연결
# POST -> 로그인 시 form에 입력된 id, pw를 table에 저장된 id, pw에 비교후 일치하면 로그인, id,pw 세션유지
def login():
    if request.method == 'POST':
        userid = request.form['id']
        userpw = request.form['pw']

        logininfo = request.form['id']
        conn = connectsql()
        cursor = conn.cursor()
        query = "SELECT * FROM tbl_user WHERE user_name = %s AND user_password = %s"
        value = (userid, userpw)
        cursor.execute(query, value)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        
        for row in data:
            data = row[0]
        
        if data:
            session['loggedin'] = True
            session['username'] = request.form['id']
            session['password'] = request.form['pw']
            return render_template('/main/main.html', logininfo = logininfo)
        else:
            return render_template('/login/loginError.html')
    else:
        return render_template ('/login/login.html')

@app.route('/regist', methods=['GET', 'POST'])
# GET -> 회원가입 페이지 연결
# 회원가입 버튼 클릭 시, 입력된 id가 tbl_user의 컬럼에 있을 시 에러팝업, 없을 시 회원가입 성공
def regist():
    if request.method == 'POST':
        userid = request.form['id']
        userpw = request.form['pw']

        conn = connectsql()
        cursor = conn.cursor()
        query = "SELECT * FROM tbl_user WHERE user_name = %s"
        value = userid
        cursor.execute(query, value)
        data = (cursor.fetchall())
        #import pdb; pdb.set_trace()
        if data:
            conn.rollback() # 이건 안 써도 될 듯
            return render_template('/login/registError.html') 
        else:
            query = "INSERT INTO tbl_user (user_name, user_password) values (%s, %s)"
            value = (userid, userpw)
            cursor.execute(query, value)
            data = cursor.fetchall()
            conn.commit()
            return render_template('/login/registSuccess.html')
        cursor.close()
        conn.close()
    else:
        return render_template('/login/regist.html')       
    
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000, debug=True)