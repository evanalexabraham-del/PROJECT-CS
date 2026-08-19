import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Evan@2009",
    database="AIR_TRAFFIC_CONTROL"
)
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
