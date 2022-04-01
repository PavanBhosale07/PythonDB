import pymysql

con=pymysql.connect(host='bms63uu8xatceqlnjqk1-mysql.services.clever-cloud.com',user='udvwebmtlwpuyeq2',password='v2lAKzVXVQuK9uRuTCe4',database='bms63uu8xatceqlnjqk1')
curs=con.cursor()

no=input('Enter ModelName : ')
curs.execute("select * from MOBILES where modelname='%s'" %no)
data=curs.fetchone()
if data:
   print('Data Found')
   print(data)
else:
    print('Data Not Found')
con.close()