import psycopg2
conn=psycopg2.connect(host="localhost",database="postgres",user="postgres",password="")
'''conn=psycopg2.connect(host="localhost", user="postgres", passwd="", db="postgres", port=3306, charset="utf8")'''    #连接对象
'''#print(conn)'''
cur = conn.cursor()   


'''游标对象'''
'''with conn.cursor() as cur:
    sql = ''''''select * from users;''''''
    cur.execute(sql)
    #lines = cur.fetchall()#将还回一个字典
    #print(lines)
    for row in cur:
        print(row)
        print(row[0],row[1])

conn.commit()'''