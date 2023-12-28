import mysql.connector
from csv import DictWriter
from csv import DictReader
import os

conn = mysql.connector.connect (host='localhost', username='root', password='Mysql1234567@', database='flightReservationSys')
my_cursor = conn.cursor()


def newUser():  
    createLogin = input("\nCREATE YOUR USERNAME: ")
    if createLogin in users:
        print("\n|  USERNAME ALREADY EXISTS!    |\n")
        newUser()
    pas = input("\nCREATE YOUR PASSWORD: ")
    users[createLogin] = pas
    pn = input("\nENTER YOUR MOBILE NO: ")
    if len(pn) != 10:
        print("\n| INVALID MOBILE NUMBER! |\n")
        newUser()
    city = input("\nENTER YOUR CITY NAME: ")
    em = input("\nENTER YOUR EMAIL ID: ")
    print("\n|  ACCOUNT CREATED SUCCESSFULLY    |")
    oldUser()


def oldUser():
    print("\n\n\tLOGIN")
    username = input("\nUSERNAME: ")
    passw = input("\nPASSWORD: ")
    if username in users and users[username] == passw:
        print("\n|  LOGIN SUCCESSFUL    |\n\n")
        searchFA()
    else:
        print("\n|  LOGIN FAILED! USER NOT EXISTS OR PASSWORD FAILED   |")
        oldUser()

users = {}
def loginF():
    acc = input("\nDO YOU HAVE ACCOUNT (Y/N)? IF NOT THEN PRESS q TO EXIT: ")
    if acc=='y' or acc=='yes' or acc=='Y' or acc=='YES':
        oldUser()
    elif acc=='n' or acc=='no' or acc=='N' or acc=='NO':
        newUser()
    while acc != "q":
        loginF()

fnum = []
deplo = []
arrlo = []
fli = []
def flight_data():   
    departure = input("\nENTER YOUR DEPARTURE LOCAION:-")
    arrival = input("\nENTER YOUR ARRIVAL LOCATION:-")
    query2 = "SELECT AIRLINES_NAME FROM FLIGHTS WHERE DEPARTURE = '{}' AND DESTINATION = '{}'".format(departure, arrival)
    if departure == query2 and arrival == query2:
        deplo.append(departure)
        arrlo.append(arrival)
        my_cursor.execute(query2)
        print("\nYOUR REQUIRED FLIGHTS ARE")
        for b in my_cursor:
            print(b) 
        fly = input("\nENTER A FLIGHT NAME YOU WANT:")
        fli.append(fly)
        print("\nHERE ARE THE DETAILS OF YOUR FLIGHT")
        query3 = "SELECT * FROM FLIGHTS WHERE AIRLINES_NAME = '{}' AND DEPARTURE = '{}' AND DESTINATION = '{}' ".format(fly, departure, arrival)
        my_cursor.execute(query3)
        for c in my_cursor:
            return print(c)
    else:
        print("\n| NO FLIGHTS AVAILABLE ON THIS  DEPARTURE AND DESTINATION LOCATIONS |\n\n")
        flight_data()

nam=[]
ag=[]
gen=[]
emid=[]
ci=[]

def read_csv():
    with open('userdata.csv') as csvreader:
        reader = DictReader(csvreader)
        for row in reader:
            print(row)
    os.remove(r'userdata.csv')
    return print("------------------------------------")

def pass_data():
    name = input("\nENTER A NAME OF A PASSENGER: ")
    if not name.isalpha():
        print("\n| PLEASE ENTER ONLY ALPHABETICAL CHARACTERS FOR YOUR USERNAME. |\n")
        pass_data()
    age = int(input(f"\nENTER THE AGE OF {name}: "))
    gender = input("\nMALE/FEMALE: ")
    email = input("\nENTER YOUR EMAIL ID: ")
    city = input("\nENTER YOUR CITY: ")
    nam.append(name)
    ag.append(age)
    gen.append(gender)
    emid.append(email)
    ci.append(city)
    
    with open('userdata.csv', 'a', newline='') as csvfile:
        csvwriter = DictWriter(csvfile, fieldnames=['name', 'age', 'gender', 'email', 'city'])
        # csvwriter.writeheader()
        csvwriter.writerow({'name':name, 'age':age, 'gender':gender, 'email':email, 'city':city})
    return print("\n-------DATA ENTERED SUCCESSFULLY-------\n\n")

flo = []
tdep = []
tarr= []
an = []
de = []
ds = []
td = []
ta = []
payment = []

def searchFA():
    print("\nHOW YOU WANT TO SEARCH YOUR FLIGHT?")
    print("\n\n\t\t1. FLIGHT NUMBER")
    print("\n\n\t\t2. DEPARTURE and DESTINATION")

    ans = int(input("\nCHOOSE ANY ONE OPTION TO CONTINUE (1/2): "))
    if ans==1:
        fnum = (input("\nENTER FLIGHT NUMBER: "))
        query = "SELECT * FROM FLIGHTS WHERE FLIGHT_NO = '{}' ".format(fnum)
        if fnum == query:
            my_cursor.execute(query)
            print("\nYOUR FLIGHT DETAILS")
            print("\n('FLIGHT ID', 'FLIGHT NAME', 'DEPARTURE', 'DESTINATION', 'FLIGHT NUMBER', 'DEPARTURE TIME', 'ARRIVAL TIME', 'CHARGES')")
            for a in my_cursor:
                print(a)
        else:
            print("\n| NO FLIGHTS AVAILABLE ON THIS FLIGHT NUMBER! |\n\n")
            searchFA()
    else:
        flight_data()
    con = input("\nWOULD YOU LIKE TO VIEW PASSENGER DETAILS (Y/N): ")
    if con=='n' or con=='N' or con=='no' or con=='NO':
        home()
    else:
        print("--------PASSENGER LIST---------")
        print("\n1 MEGHNA 28 Female megM@gmail.com Pune\n2, RIA 26 Female ria123@gmail.com Chennai\n3 PRIYANKA 29 Female priyanka@gmail.com New Delhi\n4 NANCY 27 Female nancy123@gmail.com Chennai\n5 AYAN 30 Male ayanofficial@gmail.com Mumbai\n6 RISHABH 26 Male rish99@gmail.com Pune\n7 SHRUTI 31 Female officialshruti@gmail.com New Delhi\n8 ROHAN 30 Male rohanSen99@gmail.com Pune\n9 TANISHA 26 Female tan122@gmail.com Pune\n10 KARTIK 29 Male kartik25@gmail.com Chennai")
    mhome = input("\nPRESS (H) FOR MAIN MENU:")
    if mhome=='h' or mhome=='H':
        home()

def searchFP():
    print("\nHOW YOU WANT TO SEARCH YOUR FLIGHT?")
    print("\n\n\t\t1. FLIGHT NUMBER")
    print("\n\n\t\t2. DEPARTURE AND DESTINATION")

    ans = int(input("\nCHOOSE ANY ONE OPTION TO CONTINUE (1/2): "))
    if ans==1:
        fnum = (input("\nENTER FLIGHT NUMBER: "))
        query = "SELECT * FROM FLIGHTS WHERE FLIGHT_NO = '{}' ".format(fnum)
        if fnum == query:
            my_cursor.execute(query)
            print("\nYOUR FLIGHT DETAILS")
            print("\n('FLIGHT ID', 'FLIGHT NAME', 'DEPARTURE', 'DESTINATION', 'FLIGHT NUMBER', 'DEPARTURE TIME', 'ARRIVAL TIME', 'CHARGES')")
            for a in my_cursor:
                print(a)
        else:
            print("\n| NO FLIGHTS AVAILABLE ON THIS FLIGHT NUMBER! |\n\n")
            searchFP()
    else:
        flight_data()
    
    con = input("\nTO BOOK TICKET PRESS 'Y': ")
    if con=='n' or con=='N' or con=='no' or con=='NO':
        home()
    else:
        passenger = int(input("\nENTER A NUMBER OF PASSANGERS: "))
        for d in range(passenger):
            pass_data()
        print("\nCHECK YOUR DETAILS BELOW")
        read_csv()
        print("\nCHOOSE THE CLASS YOU WANT: ")
        print("1.ECONOMY CLASS")
        print("2.BUSINESS CLASS (+20% CHARGES)")
        print("3.FIRST CLASS (+40% CHARGES)")

        cl = int(input("\nENTER CLASS NO (1/2/3): "))

        if ans==1 and cl==1:
            query7 = "SELECT AIRLINES_NAME FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query7)
            for i in my_cursor:
                an.append(i)

            query8 = "SELECT DEPARTURE FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query8)
            for j in my_cursor:
                de.append(j)

            query9 = "SELECT DESTINATION FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query9)
            for k in my_cursor:
                ds.append(k) 

            query10 = "SELECT TIME_OF_DEPARTURE FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query10)
            for l in my_cursor:
                td.append(l)

            query11 = "SELECT TIME_OF_ARRIVAL FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query11)
            for m in my_cursor:
                ta.append(m)
            query12 = "SELECT (CHARGES)*{} FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format (passenger, fnum)
            my_cursor.execute(query12)
            print(f"\nnames = {nam}               age = {ag}         gender = {gen}")
            print(f" flight name = {an}         departure = {de}       destination = {ds}")
            print(f" flight number = {fnum}      departure time = {td}        arrival time = {ta}")
            print("class = economy class")
            for n in my_cursor:
                payment.append(n)
                print(f"\nYOU HAVE TO PAY ₹{n}")

        elif ans==1 and cl==2:
            query7 = "SELECT AIRLINES_NAME FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query7)
            for i in my_cursor:
                an.append(i)

            query8 = "SELECT DEPARTURE FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query8)
            for j in my_cursor:
                de.append(j)

            query9 = "SELECT DESTINATION FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query9)
            for k in my_cursor:
                ds.append(k) 

            query10 = "SELECT TIME_OF_DEPARTURE FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query10)
            for l in my_cursor:
                td.append(l)

            query11 = "SELECT TIME_OF_ARRIVAL FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query11)
            for m in my_cursor:
                ta.append(m)
            query13 = "SELECT (CHARGES +CHARGES*0.2)*{} FROM FLIGHTS WHERE flight_no = '{}' ".format (passenger, fnum)
            my_cursor.execute(query13)
            print(f"\nnames = {nam}               age = {ag}           gender = {gen}")
            print(f"flight name = {an}         departure = {de}       destination = {ds}")
            print(f"flight number = {fnum}      departure time = {td}        arrival time = {ta}")
            print("class = business class")
            for o in my_cursor:
                payment.append(o)
                print(f"\nYOU HAVE TO PAY ₹{o}") 

        elif ans==1 and cl==3:
            query7 = "SELECT AIRLINES_NAME FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query7)
            for i in my_cursor:
                an.append(i)

            query8 = "SELECT DEPARTURE FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query8)
            for j in my_cursor:
                de.append(j)

            query9 = "SELECT DESTINATION FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query9)
            for k in my_cursor:
                ds.append(k) 

            query10 = "SELECT TIME_OF_DEPARTURE FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query10)
            for l in my_cursor:
                td.append(l)

            query11 = "SELECT TIME_OF_ARRIVAL FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(fnum)
            my_cursor.execute(query11)
            for m in my_cursor:
                ta.append(m)
            query14 = "SELECT (CHARGES +CHARGES*0.4)*{} FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format (passenger, fnum)
            my_cursor.execute(query14)
            print(f"\nnames = {nam}               age = {ag}           gender = {gen}")
            print(f"flight name = {an}         departure = {de}       destination = {de}")
            print(f"flight number = {fnum}      departure time = {td}        arrival time = {ta}     ")
            print("class = first class")
            for p in my_cursor:
                payment.append(p)
                print(f"\nYOU HAVE TO PAY ₹{p}")


        elif ans==2 and cl==1:
            query4 = "SELECT FLIGHT_NO FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query4)
            for f in my_cursor:
                flo.append(f)

            query5 = "SELECT TIME_OF_DEPARTURE FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query5)
            for g in my_cursor:
                tdep.append(g)

            query6 = "SELECT TIME_OF_ARRIVAL FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query6)
            for h in my_cursor:
                tarr.append(h)
            query15 = "SELECT CHARGES*{} FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (passenger, fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query15)
            print(f"\nnames = {nam}               age = {ag}           gender = {gen}")
            print(f"flight name = {fli}         departure = {deplo}       destination = {arrlo}")
            print(f"flight number = {flo}      departure time = {tdep}        arrival time = {tarr}     ")
            print("class = economy class")
            for q in my_cursor:
                payment.append(q)
                print(f"\nYOU HAVE TO PAY ₹{q}") 

        elif  ans==2 and cl==2:
            query4 = "SELECT FLIGHT_NO FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query4)
            for f in my_cursor:
                flo.append(f)

            query5 = "SELECT TIME_OF_DEPARTURE FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query5)
            for g in my_cursor:
                tdep.append(g)

            query6 = "SELECT TIME_OF_ARRIVAL FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query6)
            for h in my_cursor:
                tarr.append(h)
            query16 = "SELECT (CHARGES +CHARGES*0.2)*{} FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (passenger, fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query16)
            print(f"\nnames = {nam}               age = {ag}           gender = {gen}")
            print(f"flight name = {fli}         departure = {deplo}       destinatio = {arrlo}")
            print(f"flight number = {flo}      departure time = {tdep}        arrival time = {tarr}     ")
            print("class = business class")
            for r in my_cursor:
                payment.append(r)
                print(f"\nYOU HAVE TO PAY ₹{r}")  

        elif ans==2 and cl==3:
            query4 = "SELECT FLIGHT_NO FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query4)
            for f in my_cursor:
                flo.append(f)

            query5 = "SELECT TIME_OF_DEPARTURE FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query5)
            for g in my_cursor:
                tdep.append(g)

            query6 = "SELECT TIME_OF_ARRIVAL FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query6)
            for h in my_cursor:
                tarr.append(h)
            query17 = "SELECT (CHARGES +CHARGES*0.4)*{} FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (passenger, fli[0], deplo[0], arrlo[0])
            my_cursor.execute(query17)
            print(f"\nnames = {nam}               age = {ag}           gender = {gen}")
            print(f"flight name = {fli}         departure = {deplo}       destination = {arrlo}")
            print(f"flight number = {flo}      departure time = {tdep}        arrival time = {tarr}     ")
            print("class = first class")
            for s in my_cursor:
                payment.append(s)
                print(f"\nYOU HAVE TO PAY ₹{s}")
        
        print("\nHOW YOU WANT TO PAY ?")
        print("1.GOOGLE PAY")
        print("2.AMAZON PAY")
        print("3.PAYPAL")
        print("4.APPLE PAY")
        print("5.CREDIT CARD")
        print("6.DEBIT CARD")
        print("7.BANK TRANSFER")

        pay2 = int(input("\nENTER YOUR PAYMENT METHOD (1/2/3/4........):-"))

        if pay2==1:
            print("\n-------------------GOOGLE PAY---------------------------")
            print(F"PAID ₹{payment[0]}")
            print("\n\t\tTRANSACTION SUCCESSFUL")
            
        if pay2==2:
            print("\n-------------------AMAZON PAY---------------------------")
            print(F"PAID ₹{payment[0]}")
            print("\n\t\tTRANSACTION SUCCESSFUL")
                
        if pay2==3:
            print("\n-------------------PAYPAL---------------------------")
            print(F"PAID ₹{payment[0]}")
            print("\n\t\tTRANSACTION SUCCESSFUL")

        if pay2==4:
            print("\n-------------------APPLE PAY---------------------------")
            print(F"PAID ₹{payment[0]}")
            print("\n\t\tTRANSACTION SUCCESSFUL")

        if pay2==5 or pay2==6:
            print("\n-------------------CARD payment---------------------------")
            print(F"PAID ₹{payment[0]}")
            print("\n\t\tTRANSACTION SUCCESSFUL")
        print("\n--------T H A N K S!  F O R  U S I N G  F L I G H T  B O O K I N G  S Y S T E M--------------")
          
def home():
    print("\n\n\n\n--------------------W E L C O M E  T O  F L I G H T  R E S E R V A T I O N  S Y S T E M--------------------\n\n")

    print("\n\n\t\t1. ADMIN \n\n\t\t2. PASSENGER \n")

    option = int(input("\nCHOOSE ANY ONE OPTION TO CONTINUE (1/2): "))
    if option==1:
        loginF()
    elif option==2:
        searchFP()

home()
conn.close()