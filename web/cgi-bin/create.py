import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")

conn=sqlite3.connect("bits.db")
cur=conn.cursor()
query="create table emp(rno integer,name text,dept text)"
#query="insert into emp values(1,'saral','IT')"
try:
    cur.execute(query)
except Exception as e:
    print(e)
else:
    conn.commit()
    
    print("created successfully")
finally:
    conn.close()
    
