import pymysql
con=pymysql.connect(host='bms63uu8xatceqlnjqk1-mysql.services.clever-cloud.com',user='udvwebmtlwpuyeq2',password='v2lAKzVXVQuK9uRuTCe4',database='bms63uu8xatceqlnjqk1')
curs=con.cursor()

no=int(input('Enter prodid : '))
curs.execute("select * from MOBILES where prodid=%d" %no)
data=curs.fetchone()
print(data)

if data:
    ask=input('Do you want to delete? yes or no : ')
    
    if ask=='yes':
       curs.execute("delete from MOBILES where prodid=%d" %no)
       con.commit()
       print('account deleted successfully')
    elif ask=='no':
       print('mobile data as is it')

else:
    print('account dose not exist')

con.close()
