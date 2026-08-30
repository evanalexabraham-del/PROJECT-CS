import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Evan@2009",
    database="AIR_TRAFFIC_CONTROL"
)

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
else:
    print("\nInvalid Username or Password!")
