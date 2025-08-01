import mysql.connector

#THIS WIll connect to database TEST
mydb = mysql.connector.connect(host="localhost", user="meet", passwd="Meet1234@", database="test")

#getting Cursor
mycursor = mydb.cursor()

# executing Code Using cursore
mycursor.execute("select * from student")

for i in mycursor:
    print(i)



results = mycursor.fetchall()

# printing the output
for j in results:
    print(j)

results = mycursor.fetchone()

for j in results:
    print(j)