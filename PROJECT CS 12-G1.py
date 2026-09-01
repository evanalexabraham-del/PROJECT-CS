import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Evan@2009",
    database="AIR_TRAFFIC_CONTROL"
)
mycursor=mydb.cursor()
#LOGIN VERIFICATION PART
print("===================================")
print("       ATC MANAGEMENT SYSTEM")
print("===================================")

def login():
        un=input("enter your username:  ")
        username=un.lower()
        password=input("enter your password:  ")
        query1="select * from user where username=%s and password=%s"
        values=(username,password)
        mycursor.execute(query1,values)
        result=mycursor.fetchone()
        if result:
            print("login successful")
            AircraftManagementMenu()
            
            
        else:
            print("invalid username or password")

#AIRCRAFT RELATED FUNCTION
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

#FLIGHT RELATED FUNCTION
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

#PILOT RELATED FUNCTION
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


login()
