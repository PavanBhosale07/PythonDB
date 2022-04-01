import pymysql

con=pymysql.connect(host='bms63uu8xatceqlnjqk1-mysql.services.clever-cloud.com',user='udvwebmtlwpuyeq2',password='v2lAKzVXVQuK9uRuTCe4',database='bms63uu8xatceqlnjqk1')
curs=con.cursor()
try:
   ra=int(input('Enter Ram : '))
   ro=int(input('Enter Rom : '))
   curs.execute("select * from MOBILES where ram=%d and rom=%d" %(ra,ro))
   data=curs.fetchall()
   #print(data)

   for rec in data:
      print(rec)
except:
  print('is not a valid input..input in numeric')
con.close()