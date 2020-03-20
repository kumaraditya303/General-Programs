__author__ = "Kumar Aditya"

import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="9304554856a",
    auth_plugin='mysql_native_password',
    database="mydatabase"
)
# hello
cursor = db.cursor()
# cursor.execute(
#      "INSERT INTO data(username,email,password,gender,phone) VALUE('hello','rahuladitya030@gmail.com','9304554856a','M',9304554856) ")
cursor.execute("SELECT username,password,email,phone,gender,id FROM data")
for i in cursor:
    print(i)
