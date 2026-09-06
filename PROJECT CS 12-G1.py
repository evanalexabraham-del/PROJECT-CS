
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="sid",
    password="1234",
    database="AIR_TRAFFIC_CONTROL"
)

mycursor = mydb.cursor()



#AIRCRAFT RELATED FUNCTION
def ADDAIRCRAFT():
    aid=int(input("Enter 3 digit aircraft ID: "))
    airline = input("Enter airline: ")
    atype = input("Enter Aircraft type:")
    stat=input("Enter status of aircraft:")
    mycursor.execute("INSERT INTO aircraft VALUES(aid, airline,atype,stat;)
    mydb.commit()
    print("RECORD ADDED!")


def VIEWAIRCRAFT():
    print("=============AIRCRAFT DETAILS===============")
    mycursor.execute("SELECT * FROM aircraft;")
    for i in mycursor:
        print (i)

def SEARCHAIRCRAFT():
    ID= int(input("Enter Aircraft ID to search"))
    print("DETAILS OF AIRCRAFT SEARCHED:")
    mycursor.execute("SELECT * FROM aircraft WHERE aircraftID = ID ;")

def UPDATEAIRCRAFT():
    ID = int(input("Enter ID of aircraft whose status is to be updated:"))
    newstat = input("Enter new status:")
    mycursor.execute("UPDATE aircraft SET status = '"+newstat+"' WHERE aircraftID = '"+ID+"';")
    mydb.commit()
    print("UPDATED TABLE:")
    mycursor.execute("SELECT * FROM aircraft;")
    for i in mycursor:
        print(i)
        
    

    

    
    
    

