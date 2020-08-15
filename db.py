#import mysql connector
import mysql.connector
#make a connection with localhost.
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="Nitya")
#create a instance of cursor class.
mycursor = mydb.cursor()
#show thw existing databases.
mycursor.execute("show databases")
#iterate the loop
for x in mycursor:
	print(x)
#create our own database.
mycursor.execute("create database yourdbname")
#create a table inside your database.
mycursor.execute("create table customer(name varchar(255),address varchar(255))")
#add a column to an existing table.
mycursor.execute("alter table customer add column id int auto_increment primary key")
#perform basic sql operation.
mycursor.execute("select * from customer")
#fetch all the record
result = mycursor.fetchall()
for x in result:
	print(x)
#where clause statement
mycursor.execute("select * from customer where name order by")
#fetch name by deseninding order
mycursor.execute("select * from customer where name order by name desc")
#like clause pattern matching
mycursor.execute("select * from customer where like '%bai%'")
#delete a record
mycursor.execute("delete from customer where address = 'Mumbai'")

#insert a record to the database.
query = "insert into customer(name,address)values(%s,%s)"
data = ("Nitya","Mumbai")
#execute the query.
mycursor.execute(query,data)
#make your changes to the database.
mydb.commit()
#Indicator message
print(mycursor.rowcount,"was inserted successfully")
#insert multiple record to the database.
query = "insert into customer(name,address)values(%s,%s)"
data = [
	#you can change the data as per the need.
	("Nitya","Mumbai"),
	("Nitya","Mumbai"),
	("Nitya","Mumbai"),
	("Nitya","Mumbai"),
	("Nitya","Mumbai"),
	("Nitya","Mumbai"),
	("Nitya","Mumbai"),
	("Nitya","Mumbai"),
	("Nitya","Mumbai")
]
#execute the query
mycursor.execute(query,data)
mydb.commit()
#drop the table
query = "drop table customer"
mycursor.execute(query)
print(mycursor.rowcount,"was inserted successfully")