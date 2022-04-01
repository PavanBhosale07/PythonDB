import pymysql

try:
    id=int(input('Enter prodid : '))
    mod=input('Enter model : ')
    com=input('Enter company : ')
    conn= input ('Enter connectivity : ')
    r=int(input('Enter Ram : '))
    ro=int(input('Enter Rom : '))
    clr=input('Enter Color : ')
    scr=input('Enter Screen : ')
    bat=input('Enter Battery : ')
    pro=input('Enter Processor : ')
    pri=int(input('Enter Price : '))
    rat=float(input('Enter Rating : '))
    pur=input('Enter Purpose : ')

    con=pymysql.connect(host='bms63uu8xatceqlnjqk1-mysql.services.clever-cloud.com',user='udvwebmtlwpuyeq2',password='v2lAKzVXVQuK9uRuTCe4',database='bms63uu8xatceqlnjqk1')
    curs=con.cursor()
    curs.execute("insert into MOBILES values(%d,'%s','%s','%s',%d,%d,'%s','%s','%s','%s',%d,%f,'%s')" %(id,mod,com,conn,r,ro,clr,scr,bat,pro,pri,rat,pur))
    con.commit()
    print('Mobiles data stored in the cloud')

except:
    print('invalid input')

con.close()