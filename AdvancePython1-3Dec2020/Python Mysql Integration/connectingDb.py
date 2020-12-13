import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "root1234",
    database="ONLINETRAINING"
)

mycursor = connection.cursor()
# mycursor.execute("CREATE DATABASE ONLINETRAINING")
# mycursor.execute("SHOW DATABASES")
# for data in mycursor:
#     print(data)
# print(connection)
# mycursor.execute("USE ONLINETRAINING")
# mycursor.execute("create table TRAINING (ID INT, NAME VARCHAR(20),SALARY INT)")
# while True:
#     Id = int(input("Enter Id : "))
#     name = input("Enter name :")
#     salary = int(input("Enter Salary : "))
#     Insertquery = "INSERT INTO TRAINING VALUES(%s,%s,%s)"
#     value = (Id,name,salary)
#     mycursor.execute(Insertquery,value)
#     connection.commit()
mycursor.execute("delete from TRAINING WHERE ID=101")
connection.commit()
mycursor.execute("SELECT * FROM TRAINING")
# result = mycursor.fetchone()
# print(result)
result = mycursor.fetchall()
for i in result:
    print(i)
# mycursor.execute("update TRAINING SET SALARY = SALARY+2000")
# connection.commit()
