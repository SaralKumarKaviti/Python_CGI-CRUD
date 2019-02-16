import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")

conn=sqlite3.connect("bits.db")
cur=conn.cursor()

form=cgi.FieldStorage()
rno=form.getvalue("rno")
name=form.getvalue("name")
dept=form.getvalue("dept")
#print(rno,name,dept)

sql="insert into emp values('"+rno+"','"+name+"','"+dept+"')"
#print(sql)

try:
    rs=cur.execute(sql)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("succesfully inserted")
conn.close()
cur.close()
