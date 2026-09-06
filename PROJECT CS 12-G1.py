
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="sid",
    password="1234",
    database="AIR_TRAFFIC_CONTROL"
)




#AIRCRAFT RELATED FUNCTION
def ADDAIRCRAFT():
    aid=int(input("Enter 3 digit aircraft ID: "))
    airline = input("Enter airline: ")
    atype = input("Enter Aircraft type:")
    Status=input("Enter status of aircraft:")
    mydb.execute("INSERT INTO aircraft VALUES(aid, airline, atype, status);")
    mydb.commit()


def VIEWAIRCRAFT():
    print("=============AIRCRAFT DETAILS===============")
    mycursor.execute("SELECT * FROM aircraft;")
    for i in mycursor:
        print i
    
    
    
def AircraftManagementMenu():
    while True:
        print("==Aircraft Management Menu==")
        print("1. Add Aircraft Details")
        print("2. View All Aircraft")
        print("3. Search An Aircraft")
        print("4. Update Aircraft Status")
        print("5. Delete Aircraft Record")
        print("6. Back to Main Menu")
        AMMchoice=int(input("Enter Choice:"))
        if AMMchoice == 1:
            ADDAIRCRAFT()
        elif AMMchoice == 2:
            VIEWAIRCRAFT()
        elif AMMchoice == 3:
            SEARCHAIRCRAFT()
        elif AMMchoice == 4:
            UPDATEAIRCRAFT()
        elif AMMchoice == 5:
            DELETEAIRCRAFT()
        elif AMMchoice == 6:
            print("Back to Main Menu")
            break
        else:
            print("Invalid Choice")

#FLIGHT RELATED FUNCTIONS

def ADDFLIGHT():
    flightcursor=mydb.cursor()
    n=int(input("How many Flight records would you like to add? "))
    for i in range (n):
        fid=int(input('Enter Flight ID: '))
        fno=input('Enter Flight No: ')
        aid=input('Enter Aircraft ID: ')
        orig=input('Enter origin city: ')
        dest-input('Enter destination city:')
        departuretime=input('Enter time of departure: ')
        arrivaltime=input('Enter time of arrival: ')
        status=input('Enter status of flight: ')
        flightcursor.execute('insert into flights values(fid,fno,aid,orig,dest,departuretime,arrivaltime,status)')
        mydb.commit()
        print('Record Inserted')
        print()
        
def DISPLAYDETAILS():
    flightcursor.execute('SELECT * FROM FLIGHTS')
    records=flightcursor.fetchall()
    for data in records():
        print(data)

def SEARCHFLIGHT():
    fno = input("Enter Flight Number: ")
    flightcursor.execute('SELECT * FROM flights WHERE FlightNo = "' + fno + '"')
    record = flightcursor.fetchone()
    if record:
        print("Flight ID:", record[0])
        print("Flight No:", record[1])
        print("Aircraft ID:", record[2])
        print("Origin:", record[3])
        print("Destination:", record[4])
        print("Departure Time:", record[5])
        print("Arrival Time:", record[6])
        print("Status:", record[7])
    else:
        print("Flight not found")
    flightcursor.close()
    
def UPDATEFLIGHT():
    flightcursor=mydb.cursor()
    fid = int(input("Enter Flight ID: "))
    status = input("Enter new status: ")
    flightcursor.execute("UPDATE flights SET Status = '" + status + "' WHERE FlightID = " + str(fid))
    mydb.commit()
    print("Flight details updated successfully")
    flightcursor.close()

def REMOVEFLIGHT():
    flightcursor=mydb.cursor()
    fno = input("Enter Flight Number to remove: ")
    flightcursor.execute('DELETE FROM flights WHERE FlightNo = "'+fno+ '"')
    mydb.commit()
    if flightcursor.rowcount > 0:
        print("Flight deleted successfully")
    else:
        print("No flight found.")
        flightcursor.close()
    
def FlightManagementMenu():
    while True:
        print("==Flight Management Menu==")
        print("1. Add New Flights")
        print("2. Display All flight details")
        print("3. Search A Flight")
        print("4. Update Flight Details")
        print("5. Remove Flight Record")
        print("6. Back to Main menu")
        FMMchoice=int(input("Enter Choice:"))
        if FMMchoice == 1:
            ADDFLIGHT()
        elif FMMchoice == 2:
            DISPLAYDETAILS()
        elif FMMchoice == 3:
            SEARCHFLIGHT()
        elif FMMchoice == 4:
            UPDATEFLIGHT()
        elif FMMchoice == 5:
            REMOVEFLIGHT()
        elif FMMchoice == 6:
            print("Back to Main Menu")
            break
        else:
            print("Invalid Choice")

#PILOT RELATED FUNCTIONS
def ADDPILOT():
    pilotcursor = mydb.cursor()
    pilot_id = int(input("Enter Pilot ID: "))
    name = input("Enter Pilot Name: ")
    exp = int(input("Enter Experience (Years): "))
    flight_id = int(input("Enter Flight ID: "))
    contact = input("Enter Contact Number: ")
    pilotcursor.execute("INSERT INTO pilots VALUES ((pilot_id, name, exp, flight_id, contact))")
    mydb.commit()
    print("Pilot record added successfully.")
    pilotcursor.close()

def VIEWPILOT():
    pilotcursor = mydb.cursor()
    pilotcursor.execute("SELECT * FROM pilots")
    records = pilotcursor.fetchall()
    print("---PILOT RECORDS---")
    for row in records:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Exp:", row[2], "yrs")
        print("FlightID:", row[3])
        print("Contact:", row[4])
    pilotcursor.close()

def SEARCHPILOT():
    pilotcursor = mydb.cursor()
    pilotid = int(input("Enter Pilot ID to search: "))
    pilotcursor.execute("SELECT * FROM pilots WHERE PilotID = " + pilotid)
    record = cursor.fetchone()

def UPDATEPILOT():
    pilotcursor = mydb.cursor()
    pilotid = int(input("Enter Pilot ID to update: "))
    cursor.execute("SELECT * FROM pilots WHERE PilotID = "+ pilotid)
    record = cursor.fetchone()
    if record:
        print("Enter new details for the pilot:")
        new_name = input("Enter New Name: ")
        newexp = int(input("Enter New Experience (in Years): "))
        newflight_id = int(input("Enter New Flight ID: "))
        newcontact = input("Enter New Contact: ")
        cursor.execute('UPDATE pilots SET PilotName = '"+new_name+"', Experience = '"+new_exp+"', FlightID = '"+new_flight_id+"' , Contact= '"+new_contact+"'')
        pilotcursor.commit()
        pilotcursor.close()

def DELETEPILOT():
    pilotcursor = mydb.cursor()
    pilotid = int(input("Enter Pilot ID to delete: "))
    pilotcursor.execute('DELETE FROM pilots WHERE PilotID= '"+pilotid+"'')
    mydb.commit()
    pilotcursor.close()
    
def PilotInformationMenu():
    while True:
        print("==Pilot Information Menu==")
        print("1. Add Pilot Details")
        print("2. View Pilot Details")
        print("3. Search An Pilot")
        print("4. Update Pilot Details")
        print("5. Delete Pilot Record")
        print("6. Back to Main Menu")
        PIMchoice=int(input("Enter Choice:"))
        if PIMchoice == 1:
            ADDPILOT()
        elif PIMchoice == 2:
            VIEWPILOT()
        elif PIMchoice == 3:
            SEARCHPILOT()
        elif PIMchoice == 4:
            UPDATEPILOT()
        elif PIMchoice == 5:
            DELETEPILOT()
        elif PIMchoice == 6:
            print("Back to Main Menu")
            break
        else:
            print("Invalid Choice")

#ATCClearanceManagementMenu
def ATCClearanceManagementMenu():
    while True:
        print("==ATC Clearance Management Menu==")
        print("1. Add Clearance Record")
        print("2. Display Clearance Details")
        print("3. Search Clearance Details")
        print("4. Update Clearance Record")
        print("5. Delete Clearance Record")
        print("6. Back to Main Menu")
        ACMchoice=int(input("Enter Choice:"))
        if ACMchoice == 1:
            ADDCLEARANCE()
        elif ACMchoice == 2:
            DISPLAYCLEARANCE()
        elif ACMchoice == 3:
            SEARCHCLEARANCE()
        elif ACMchoice == 4:
            UPDATECLEARANCE()
        elif ACMchoice == 5:
            DELETECLEARANCE()
        elif ACMchoice == 6:
            print("Back to Main Menu")
            break
        else:
            print("Invalid Choice")


#LOGIN VERIFICATION PART
mycursor = mydb.cursor()
print("===================================")
print("       ATC MANAGEMENT SYSTEM")
print("===================================")
username = input("Enter Username: ")
password = input("Enter Password: ")
sql = "SELECT * FROM User WHERE Username = %s AND Password = %s"
values = (username, password)
mycursor.execute(sql, values)
result = mycursor.fetchone()
if result:
    print("\nLogin Successful!")
    print("Welcome", result[1])
    print("Role:", result[3])
