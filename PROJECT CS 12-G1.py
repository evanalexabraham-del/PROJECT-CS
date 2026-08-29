import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Evan@2009",
    database="AIR_TRAFFIC_CONTROL"
)
def FlightManagementMenu():
    while True:
        print("==Flight Management Menu==")
        print("1. Add New Flights")
        print("2. Display All flight details")
        print("3. Search A Flight")
        print("4. Update Flight Details")
        print("5. Remove Flight")
        print("6. Back to Main menu")
        FMMchoice=int(input("Enter Choice:"))
        if FMMchoice == 1:
            ADDFLIGHT()
        elif FMMchoice == 2:
            DISPLAYDETAILS()
        
    
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
