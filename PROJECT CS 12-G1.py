
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
    aid = int(input("Enter 3 digit aircraft ID: "))
    airline = input("Enter airline: ")
    atype = input("Enter Aircraft type: ")
    stat = input("Enter status of aircraft: ")

    mycursor.execute(
        "INSERT INTO aircraft VALUES (%s, %s, %s, %s)",
        (aid, airline, atype, stat)
    )
    mydb.commit()
    print("RECORD ADDED!")
def VIEWAIRCRAFT():
    print("=============AIRCRAFT DETAILS===============")
    mycursor.execute("SELECT * FROM AIRCRAFT;")
    data= mycursor.fetchall()
    print("AIRCRAFT ID\tAIRLINE\tAIRCRAFT TYPE\tSTATUS")
    for i in data:
        print(i[0],"\t", i[1], "\t",i[2], "\t",i[3])
    print("============================================")
    

def SEARCHAIRCRAFT():
    ID = int(input("Enter Aircraft ID to search: "))
    print("DETAILS OF AIRCRAFT SEARCHED:")

    mycursor.execute("SELECT * FROM aircraft WHERE aircraftID = %s", (ID,))
    res = mycursor.fetchone()

    if result:
        print(res)
    else:
        print("AIRCRAFT NOT FOUND!")

def UPDATEAIRCRAFT():
    ID = int(input("Enter ID of aircraft whose status is to be updated:"))
    newstat = input("Enter new status:")
    mycursor.execute("UPDATE aircraft SET status = %s WHERE aircraftID = %s;", (newstat, ID))
    mydb.commit()
    print("Aircraft added successfully!")

def DELETEAIRCRAFT():
    ID = int(input("Enter ID of aircraft to delete:"))
    mycursor.execute("DELETE FROM aircraft WHERE aircraftID = %s;",(ID,))
    print("Aircraft deleted")

def DISPLAYALLINFO():
    fno=int(input("Enter Flight number to search:"))
    mycursor.execute("SELECT PilotName from pilots,flights where flights.flightno = pilots.flightno AND flightno = %s;",(fno,))
    print("Pilot of flight:")
    for i in mycursor:
        print(i)
    mycursor.execute("SELECT * FROM aircraft,flights WHERE aircraft.aircraftid = flights.aircraftid AND flightno = %s;",(fno,))
    data = mycursor.fetchall()
    print("Details of aircraft:")
    print("AircraftID\tAirline\tAircraft Type\tStatus")
    for i in data:
        print(i[0],"\t", i[1], "\t",i[2], "\t",i[3])
    

    
    
    

