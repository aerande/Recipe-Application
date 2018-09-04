import pymysql.cursors


def connect():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='recipe_app',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
