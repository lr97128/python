import pymysql


def exec_query(sql):
    db = pymysql.connect(host='10.175.255.253', user='liurui', password='liurui97128224', db='mysql', port=3306)
    cur = db.cursor()
    try:
        cur.execute(sql)
        results = cur.fetchall()
        for result in results:
            print(result)
            # Host = result[0]
            # User = result[1]
            # Password = result[2]
            # print(Host, User, Password)
    except Exception as e:
        raise e
    finally:
        cur.close()
        db.close()


def exec_no_query(sql):
    db = pymysql.connect(host='10.175.255.253', user='liurui', password='liurui97128224', db='mysql', port=3306)
    cur = db.cursor()
    try:
        cur.execute(sql)
        db.commit()
        print("操作成功...")
    except Exception as e:
        db.rollback()
        raise e
    finally:
        cur.close()
        db.close()


if __name__ == '__main__':
    # sql = 'select Host,User,Password from user'
    # sql = "create database test;"
    sql = "drop database test;"
    exec_no_query(sql)
