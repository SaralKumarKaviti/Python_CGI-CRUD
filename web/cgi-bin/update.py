import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")

conn=sqlite3.connect("cgi-bin/data.db")
cur=conn.cursor()

form=cgi.FieldStorage()
rno=form.getvalue("rno")
name=form.getvalue("name")
dept=form.getvalue("dept")
print(rno,name,dept)

query="update emp SET rno='"+rno+"',name='"+name+"'where rno="+rno
print(query)

try:
    rs=cur.execute(query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("updated succesfully")
conn.close()
#cur.close()
    
