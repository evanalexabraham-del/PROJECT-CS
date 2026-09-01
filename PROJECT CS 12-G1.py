import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Evan@2009",
    database="atc"
)
mycursor=mydb.cursor()
print("===================================")
print("       ATC MANAGEMENT SYSTEM")
print("===================================")
def login():
        un=input("enter your username:  ")
        username=un.lower()
        password=input("enter your password:  ")
        query1="select * from users where username=%s and password=%s"
        values=(username,password)
        mycursor.execute(query1,values)
        result=mycursor.fetchone()
        if result:
            print("login successful")
            MAINMENU()
        else:
            print("invalid username or password")
login()

def MAINMENU():
    while True:
        print("1. Aircraft Management")
        print("2. Flight Management")
        print("3. Pilot Management")
        print("4. ATC Clearance")
        print("5. Flight Status")
        print("6. Report and Queries")
        print("7. Exit")
        choice=int(input("Enter Submenu:"))
        if choice == 1:
            AircraftManagementMenu()
        elif choice == 2:
            FlightManagementMenu()
        elif choice == 3:
            PilotInformationMenu()
        elif choice == 4:
            ATCClearanceManagementMenu()
        elif choice == 5:
            FlightStatusMenu()
        elif choice == 6:
            ReportQueryMenu():
        elif choice == 7:
            print("Program Terminated")
            break
        else:
            print("Invalid Choice")
              
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
            
#FlightStatusMenu
def FlightStatusMenu():
    while True:
        print("==Flight Status==")
        print("1. View Flights")
        print("2. Search Incoming Flights")
        print("3. Search Outgoing Flights")
        print("4. Back to Main Menu")
        FSchoice=int(input("Enter Choice:"))
        if FSchoice == 1:
            VIEWFLIGHTS()
        elif FSchoice == 2:
            SEARCHINCOMINGFLIGHTS()
        elif FSchoice == 3:
            SEARCHOUTGOINGFLIGHTS()
        elif FSchoice == 4:
            print("Taking Back to Main Menu")
            break
        else:
            print("Invalid Choice")

def ReportQueryMenu():
    while True:
        print("==Flight Status==")
        print("1. Display Flight Pilot and Aircraft Information")
        print("2. Show Aircraft Requiring Clearance")
        print("3. Search Flights Managed by a Controller")
        print("4. Display Cancelled/Delayed Flights")
        print("5. Back to Main Menu")
        RQchoice=int(input("Enter Choice:"))
        if RQchoice == 1:
            DISPLAYALLINFO()
        elif RQchoice == 2:
            NEEDINGCLEARANCE()
        elif RQchoice == 3:
            CONTROLLERMANAGEDFLIGHT()
        elif RQchoice == 4:
            CANCELDELAYFLIGHT()
        elif RQchoice == 5:
            print("Taking Back to Main Menu")
            break
        else:
            print("Invalid Choice")
        
#LOGIN VERIFICATION PART
mycursor = mydb.cursor()
print("===================================")
print("       ATC MANAGEMENT SYSTEM       ")
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
else:
    print("\nInvalid Username or Password!")
