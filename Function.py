def VIEWFLIGHTS():
    mycursor.execute("SELECT FlightID, FlightNo, Origin, Destination, DepartureTime, ArrivalTime, Status FROM flights")
    data = mycursor.fetchall()
    print("\n========== ALL FLIGHTS ==========")
    for row in data:
        print("Flight ID:", row[0])
        print("Flight No:", row[1])
        print("From:", row[2])
        print("To:", row[3])
        print("Departure:", row[4])
        print("Arrival:", row[5])
        print("Status:", row[6])
        print("--------------------------------")
  

def SEARCHINCOMINGFLIGHTS():
    mycursor.execute("SELECT FlightID, FlightNo, Origin, Destination, ArrivalTime, Status FROM flights WHERE Destination='Thiruvananthapuram'")
    data = mycursor.fetchall()
    print("\n====== INCOMING FLIGHTS ======")
    for row in data:
        print("Flight ID:", row[0])
        print("Flight No:", row[1])
        print("From:", row[2])
        print("To:", row[3])
        print("Arrival:", row[4])
        print("Status:", row[5])
        print("--------------------------------")

  
def SEARCHOUTGOINGFLIGHTS():
    mycursor.execute("SELECT FlightID, FlightNo, Origin, Destination, DepartureTime, Status FROM flights WHERE Origin='Thiruvananthapuram'")
    data = mycursor.fetchall()
    print("\n====== OUTGOING FLIGHTS ======")
    for row in data:
        print("Flight ID:", row[0])
        print("Flight No:", row[1])
        print("From:", row[2])
        print("To:", row[3])
        print("Departure:", row[4])
        print("Status:", row[5])
        print("--------------------------------")
