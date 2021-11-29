import pymysql

def dbInterview(data_list):
    db = pymysql.connect(
                    host='localhost',
                    port = 3306,
                    user='root',
                    passwd='hojin0215!',
                    db = 'userlist',
                    charset='utf8')

    cursor = db.cursor()
    sql = "select * from interview"
    cursor.execute(sql)
    db.commit()

    data_list = cursor.fetchall()
    print(data_list[0])
    db.close()
