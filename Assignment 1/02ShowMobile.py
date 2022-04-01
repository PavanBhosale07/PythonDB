import pymysql

con=pymysql.connect(host='bms63uu8xatceqlnjqk1-mysql.services.clever-cloud.com',user='udvwebmtlwpuyeq2',password='v2lAKzVXVQuK9uRuTCe4',database='bms63uu8xatceqlnjqk1')
curs=con.cursor()
curs.execute('select * from MOBILES')
data=curs.fetchall()
#print(data)


for rec in data:
    print(rec)

con.close()