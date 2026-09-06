def VIEWFLIGHTS():
    mycursor.execute("SELECT FlightID, FlightNo, Origin, Destination, DepartureTime, ArrivalTime, Status FROM flights")
    data = mycursor.fetchall()
    print("\n========== ALL FLIGHTS ==========")
    for row in data:
        print(row)
  
def SEARCHINCOMINGFLIGHTS():
    mycursor.execute("SELECT FlightID, FlightNo, Origin, Destination, ArrivalTime, Status FROM flights WHERE Destination='Thiruvananthapuram'")
    data = mycursor.fetchall()
    print("\n====== INCOMING FLIGHTS ======")
    for row in data:
        print(row)

def SEARCHOUTGOINGFLIGHTS():
    mycursor.execute("SELECT FlightID, FlightNo, Origin, Destination, DepartureTime, Status FROM flights WHERE Origin='Thiruvananthapuram'")
    data = mycursor.fetchall()
    print("\n====== OUTGOING FLIGHTS ======")
    for row in data:
        print(row)
