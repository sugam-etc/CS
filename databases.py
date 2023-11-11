import sqlite3 as sq

connection = sq.connect("abc.db")
cursor = connection.cursor()  #will be doing everything on it

students_data = [
    #Index[0],FullName[1],Address[2],Username[3],password[4],modeoflogin[5],grades[6],rollno[7]
    (1,'Sugam Bastola' , 'XYZ','Sugam','123','12','734','1'),
    (2,'Santosh Subedi', 'XYZ','Santosh','123','12','734','1'),
    (3,'Sandesh Subedi','XYZ','Sandesh','123','12','734','1'),
    (4,'Dipak Chhetri','XYZ','Dipak','123','12','734','1'),
    (5,'Utsav Sharma','XYZ','Utsav','123','12','734','1'),
    (6,'Rajib Poudel','XYZ','Rajib','123','12','734','1'),
]
cursor.execute("create table if not exists students ( symbol , full_name , address, username , password,grades,rollno,mode_of_login)")
cursor.executemany("insert into students values (?,?,?,?,?,?,?,?)",students_data)


#Displaying Data
for item in cursor.execute("select * from students"):
    if(username == item[3] and password == item[4]):
        print('Login Success')
        break
    else:
        print('Login Failed')
        break

connection.close()