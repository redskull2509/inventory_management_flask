import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

#Create Table
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

#Insert Row in Table users
user = (1,"kapil","kapil1")
insert_user = "INSERT INTO users VALUES(?,?,?)"

cursor.execute(insert_user,user)

#Insert Multiple Rows in the table users
users = [
    (2,"jacob","jacob1"),
    (3,"rob","rob1"),
    (4,"jack","jack1")
]

cursor.executemany(insert_user,users)

#Print Rows from table users

select_users = "SELECT * from users"
 
for user in cursor.execute(select_users):
    print (user)


connection.commit()

connection.close()



