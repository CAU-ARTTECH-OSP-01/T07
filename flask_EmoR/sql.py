import pymysql

def dbInterview(data_list):
    db = pymysql.connect(
                    host='localhost',
                    port = 3306,
                    user='root',
                    passwd='tiger',
                    db = 'mypage',
                    charset='utf8')

    cursor = db.cursor()
    sql = "select * from interview"
    cursor.execute(sql)
    db.commit()

    data_list = cur.fetchall()
    print(data_list[0])
    db.close()
