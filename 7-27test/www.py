import pymysql

mydb= pymysql.connect(host='localhost', port=3306, user='root', passwd='12345', db ='txf1',charset='UTF8')
cur = mydb.cursor()

#cur.execute('create table sql_table(date text not null,open double,high double,low double,close double,volume int);')
"""
cur.execute("LOAD DATA LOCAL INFILE 'C:\\Users\\USER\\Desktop\\7-25.csv' \
INTO TABLE sql_table\
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' \
LINES [TERMINATED BY '\\r\\n'] \
IGNORE 1 LINES ;")
"""

cur.execute("LOAD DATA LOCAL INFILE 'C:\\Users\\USER\\Desktop\\7-25.csv' \
INTO TABLE sql_table  \
FIELDS TERMINATED BY  ',' \
LINES TERMINATED BY  '\r\n'  \
IGNORE 1 LINES")


