import pymysql

con=pymysql.connect(host='bms63uu8xatceqlnjqk1-mysql.services.clever-cloud.com',user='udvwebmtlwpuyeq2',password='v2lAKzVXVQuK9uRuTCe4',database='bms63uu8xatceqlnjqk1')
curs=con.cursor()

id=int(input('Enter Prodid : '))
curs.execute("select * from MOBILES where prodid=%d" %(id))
data=curs.fetchone()

if data:
   pri=int(input('Enter Price : '))
   curs.execute("update MOBILES set price=%d where prodid=%d" %(pri,id))
   con.commit()
   print('Mobile data updated')
else:
   print('Mobile dose not exist')

con.close()