#step1 : Import library
import mysql.connector as con

#step2 : call connect method and get a connection from database
dbCon = con.connect(host='localhost',database='student',user='root',passwd='Admin@123')

#step3 : create a cursor
cur = dbCon.cursor()

#step4: execute query using cursor
#rollno = input('Enter Rollno : ' )
#name  = input('Enter name : ')
#cur.execute("insert into students values("+ rollno +",'"+ name +"')")

#to view structure of table
#cur.execute("Desc students")
#for i in cur:
 #   print(i)

#to view all records
cur.execute('select * from students')
#for i in cur:
 #   print(i)

#fetchall method and rowcount
#rec = cur.fetchall()
#no=cur.rowcount
#for i in rec:
    #print(i)
#print(no)

#fetchmany(size) method
rec = cur.fetchmany(2)
no=cur.rowcount
for i in rec:
   print(i)
print(rec)
print(no)

#fetchone method
#rec = cur.fetchone()
#no=cur.rowcount
#print(rec)
#print(no)

#special records
#cur.execute('select * from students where name="Kunjal"')
#for i in cur:
 #   print(i)



#step5: close cursor
#cur.close()

#step6: commit transactions
#dbCon.commit()

#step7: close connection
dbCon.close()

print('Hi')
