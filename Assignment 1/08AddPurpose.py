import pymysql

con=pymysql.connect(host='bms63uu8xatceqlnjqk1-mysql.services.clever-cloud.com',user='udvwebmtlwpuyeq2',password='v2lAKzVXVQuK9uRuTCe4',database='bms63uu8xatceqlnjqk1')
curs=con.cursor()

nm=input('Enter Modelname : ')
curs.execute("select * from MOBILES where modelname='%s'" %nm)
data=curs.fetchone()
print(data)
if data:
      pur=input('Enter Purpose:   ')

      curs.execute("update MOBILES set purpose='%s' where modelname='%s'" %(pur,nm))
      con.commit()
      print ('Purpose added Sucessfully')
else:
    print ('Mobile not found')

con.close()